"""
Medical Knowledge Base Web Scraper / API Fetcher
Fetches open-access clinical literature from PubMed (via NCBI E-utilities)
and Wikipedia Medical Articles (via MediaWiki REST API).
"""

import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional


class PubMedFetcher:
    """
    Fetches medical research abstracts from NCBI PubMed API.
    """
    ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def __init__(self, email: str = "researcher@example.com", tool: str = "ms_research_rag"):
        self.email = email
        self.tool = tool
        self.headers = {"User-Agent": f"{tool}/1.0 ({email})"}

    def search_pmids(self, query: str, max_results: int = 20) -> List[str]:
        """Search PubMed for query and return list of PMIDs."""
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": max_results,
            "tool": self.tool,
            "email": self.email
        }
        url = f"{self.ESEARCH_URL}?{urllib.parse.urlencode(params)}"
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                id_list = data.get("esearchresult", {}).get("idlist", [])
                return id_list
        except Exception as e:
            print(f"[PubMedFetcher] Error searching PMIDs for '{query}': {e}")
            return []

    def fetch_abstracts(self, pmids: List[str]) -> List[Dict]:
        """Fetch article metadata and abstract text for given PMIDs."""
        if not pmids:
            return []

        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "xml",
            "tool": self.tool,
            "email": self.email
        }
        url = f"{self.EFETCH_URL}?{urllib.parse.urlencode(params)}"

        articles = []
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                xml_data = resp.read()
                root = ET.fromstring(xml_data)

                for article in root.findall(".//PubmedArticle"):
                    pmid_elem = article.find(".//MedlineCitation/PMID")
                    pmid = pmid_elem.text if pmid_elem is not None else "Unknown"

                    title_elem = article.find(".//ArticleTitle")
                    title = "".join(title_elem.itertext()).strip() if title_elem is not None else ""

                    abstract_texts = []
                    for abs_elem in article.findall(".//Abstract/AbstractText"):
                        label = abs_elem.attrib.get("Label", "")
                        text = "".join(abs_elem.itertext()).strip()
                        if label:
                            abstract_texts.append(f"{label}: {text}")
                        else:
                            abstract_texts.append(text)
                    abstract = "\n".join(abstract_texts)

                    journal_elem = article.find(".//Journal/Title")
                    journal = journal_elem.text if journal_elem is not None else ""

                    year_elem = article.find(".//JournalIssue/PubDate/Year")
                    if year_elem is None:
                        year_elem = article.find(".//JournalIssue/PubDate/MedlineDate")
                    year = year_elem.text if year_elem is not None else ""

                    if title and abstract:
                        articles.append({
                            "pmid": pmid,
                            "title": title,
                            "abstract": abstract,
                            "journal": journal,
                            "year": year,
                            "source": "PubMed Abstract",
                            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                        })
        except Exception as e:
            print(f"[PubMedFetcher] Error fetching XML for PMIDs: {e}")

        return articles

    def search_and_fetch(self, query: str, max_results: int = 20) -> List[Dict]:
        """Convenience method to search and fetch abstracts in one go."""
        pmids = self.search_pmids(query, max_results=max_results)
        time.sleep(0.4) # Respect NCBI API rate limits
        return self.fetch_abstracts(pmids)


class WikipediaFetcher:
    """
    Fetches clean text medical articles from Wikipedia MediaWiki API.
    """
    WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

    def __init__(self, user_agent: str = "MedicalRAGResearch/1.0"):
        self.headers = {"User-Agent": user_agent}

    def fetch_article(self, title: str) -> Optional[Dict]:
        """Fetch article extract and summary for a Wikipedia title."""
        params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": "1",
            "exlimit": "1",
            "titles": title,
            "format": "json",
            "redirects": "1"
        }
        url = f"{self.WIKI_API_URL}?{urllib.parse.urlencode(params)}"
        
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers=self.headers)
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    pages = data.get("query", {}).get("pages", {})
                    for page_id, page in pages.items():
                        if page_id == "-1":
                            print(f"[WikipediaFetcher] Page not found: '{title}'")
                            return None
                        page_title = page.get("title", title)
                        extract = page.get("extract", "")
                        
                        # Split intro summary (first paragraph/section) vs body
                        sections = extract.split("\n\n==")
                        intro = sections[0].strip() if sections else ""

                        clean_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_title.replace(' ', '_'))}"

                        return {
                            "page_id": page_id,
                            "title": page_title,
                            "summary": intro,
                            "full_text": extract,
                            "url": clean_url,
                            "source": "Wikipedia Medical Article"
                        }
            except Exception as e:
                if ("429" in str(e) or "Too Many Requests" in str(e)) and attempt < 3:
                    sleep_time = 3.0 * (attempt + 1)
                    print(f"[WikipediaFetcher] 429 Rate limited for '{title}', sleeping {sleep_time}s (attempt {attempt+1})...")
                    time.sleep(sleep_time)
                    continue
                print(f"[WikipediaFetcher] Error fetching article '{title}': {e}")
                return None
        return None

    def fetch_multiple_articles(self, titles: List[str]) -> List[Dict]:
        """Fetch multiple Wikipedia articles with generous rate limit pauses."""
        results = []
        for t in titles:
            art = self.fetch_article(t)
            if art:
                results.append(art)
            time.sleep(2.0)
        return results
