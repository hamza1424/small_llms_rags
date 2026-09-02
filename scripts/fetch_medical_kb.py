#!/usr/bin/env python3
"""
Fetch a lean medical knowledge base aligned to gold-question templates.

Gold questions look like:
  - What is (are) <Disease>?
  - Who is at risk for <Disease>?
  - What are the symptoms of <Disease>?
  - What are the treatments for <Disease>?
  - How to prevent / diagnose <Disease>?
  - What causes <Disease>?

Target per focus area:
  - 2 Wikipedia overview / management articles
  - up to 7 unique PubMed abstracts covering definition, risk, symptoms, treatment
"""

import sys
import json
import csv
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from rag.web_scraper import PubMedFetcher, WikipediaFetcher

PUBMED_PER_FOCUS = 7
PUBMED_MAX_RESULTS_PER_QUERY = 3

# Top 10 focus areas with question-aligned PubMed queries + Wikipedia pages
FOCUS_AREAS_CONFIG = {
    "Breast Cancer": {
        "pubmed_queries": [
            "breast cancer overview definition causes etiology patient education",
            "breast cancer risk factors prevention who is at risk screening",
            "breast cancer symptoms signs diagnosis treatment management options",
        ],
        "wiki_titles": [
            "Breast cancer",
            "Management of breast cancer",
        ],
    },
    "Prostate Cancer": {
        "pubmed_queries": [
            "prostate cancer overview definition causes etiology patient education",
            "prostate cancer risk factors prevention who is at risk screening PSA",
            "prostate cancer symptoms signs diagnosis treatment management options",
        ],
        "wiki_titles": [
            "Prostate cancer",
            "Management of prostate cancer",
        ],
    },
    "Stroke": {
        "pubmed_queries": [
            "stroke overview definition ischemic hemorrhagic causes etiology",
            "stroke risk factors prevention warning signs who is at risk",
            "stroke symptoms FAST diagnosis acute treatment management",
        ],
        "wiki_titles": [
            "Stroke",
            "Ischemic stroke",
        ],
    },
    "Skin Cancer": {
        "pubmed_queries": [
            "skin cancer melanoma overview definition causes etiology",
            "skin cancer risk factors ultraviolet prevention who is at risk",
            "skin cancer symptoms signs diagnosis treatment management options",
        ],
        "wiki_titles": [
            "Skin cancer",
            "Melanoma",
        ],
    },
    "Alzheimer's Disease": {
        "pubmed_queries": [
            "Alzheimer's disease overview definition causes etiology pathophysiology",
            "Alzheimer's disease risk factors prevention who is at risk",
            "Alzheimer's disease symptoms diagnosis treatment management options",
        ],
        "wiki_titles": [
            "Alzheimer's disease",
            "Management of Alzheimer's disease",
        ],
    },
    "Colorectal Cancer": {
        "pubmed_queries": [
            "colorectal cancer overview definition causes etiology patient education",
            "colorectal cancer risk factors screening colonoscopy prevention",
            "colorectal cancer symptoms diagnosis treatment options management",
        ],
        "wiki_titles": [
            "Colorectal cancer",
            "Colonoscopy",
        ],
    },
    "Lung Cancer": {
        "pubmed_queries": [
            "lung cancer overview definition NSCLC SCLC causes etiology",
            "lung cancer risk factors smoking who is at risk screening prevention",
            "lung cancer symptoms diagnosis treatment options management",
        ],
        "wiki_titles": [
            "Lung cancer",
            "Non-small-cell lung carcinoma",
        ],
    },
    "High Blood Cholesterol": {
        "pubmed_queries": [
            "high blood cholesterol hypercholesterolemia overview definition causes etiology",
            "high cholesterol risk factors causes cardiovascular disease prevention",
            "high cholesterol symptoms diagnosis statin treatment lifestyle management",
        ],
        "wiki_titles": [
            "Hypercholesterolemia",
            "Statin",
        ],
    },
    "Heart Attack": {
        "pubmed_queries": [
            "heart attack myocardial infarction overview definition causes etiology",
            "heart attack risk factors who is at risk prevention lifestyle",
            "heart attack symptoms warning signs diagnosis emergency treatment management",
        ],
        "wiki_titles": [
            "Myocardial infarction",
            "Management of myocardial infarction",
        ],
    },
    "Heart Failure": {
        "pubmed_queries": [
            "heart failure overview definition HFrEF HFpEF causes etiology",
            "heart failure causes risk factors who is at risk prevention",
            "heart failure symptoms diagnosis treatment management guidelines",
        ],
        "wiki_titles": [
            "Heart failure",
            "Management of heart failure",
        ],
    },
}

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "scraped_kb"


def save_structured_data(all_pubmed: list, all_wiki: list):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pubmed_json_path = OUTPUT_DIR / "pubmed_abstracts.json"
    pubmed_csv_path = OUTPUT_DIR / "pubmed_abstracts.csv"
    with open(pubmed_json_path, "w", encoding="utf-8") as f:
        json.dump(all_pubmed, f, indent=2, ensure_ascii=False)

    if all_pubmed:
        keys = ["focus_area", "pmid", "title", "journal", "year", "abstract", "url"]
        with open(pubmed_csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for row in all_pubmed:
                writer.writerow({k: row.get(k, "") for k in keys})

    wiki_json_path = OUTPUT_DIR / "wikipedia_articles.json"
    wiki_csv_path = OUTPUT_DIR / "wikipedia_articles.csv"
    with open(wiki_json_path, "w", encoding="utf-8") as f:
        json.dump(all_wiki, f, indent=2, ensure_ascii=False)

    if all_wiki:
        keys = ["focus_area", "title", "summary", "full_text", "url"]
        with open(wiki_csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for row in all_wiki:
                writer.writerow({k: row.get(k, "") for k in keys})

    print(f"Saved JSON & CSV outputs to {OUTPUT_DIR}")


def generate_readable_markdown(all_pubmed: list, all_wiki: list):
    md_path = OUTPUT_DIR / "MEDICAL_KNOWLEDGE_BASE_SUMMARY.md"
    focus_list = ", ".join(FOCUS_AREAS_CONFIG.keys())

    md_lines = [
        "# Medical Knowledge Base - Question-Aligned Top 10 Focus Areas",
        "",
        "Scraped from **Wikipedia** and **PubMed** to support gold-style questions such as "
        "*What is…?*, *Who is at risk…?*, *What are the symptoms…?*, *What are the treatments…?*, "
        f"*How to prevent/diagnose…?* for: **{focus_list}**.",
        "",
        "Target per focus area: **2 Wikipedia articles** + **up to 7 PubMed abstracts**.",
        "",
        "---",
        "",
    ]

    for area in FOCUS_AREAS_CONFIG.keys():
        md_lines.append(f"## Focus Area: {area}")
        md_lines.append("")

        area_wiki = [w for w in all_wiki if w.get("focus_area") == area]
        md_lines.append(f"### Wikipedia Medical Overviews ({len(area_wiki)} Articles)")
        md_lines.append("")
        for idx, wiki in enumerate(area_wiki, 1):
            md_lines.append(f"#### {idx}. [{wiki['title']}]({wiki['url']})")
            md_lines.append("**Source**: Wikipedia Article")
            md_lines.append("")
            md_lines.append("**Summary / Overview**:")
            md_lines.append(wiki["summary"])
            md_lines.append("")
            md_lines.append("<details>")
            md_lines.append(f"<summary>Click to expand Full Article Text for {wiki['title']}</summary>")
            md_lines.append("")
            md_lines.append(wiki["full_text"])
            md_lines.append("")
            md_lines.append("</details>")
            md_lines.append("")

        md_lines.append("---")
        md_lines.append("")

        area_pubmed = [p for p in all_pubmed if p.get("focus_area") == area]
        md_lines.append(f"### PubMed Research Abstracts ({len(area_pubmed)} Abstracts)")
        md_lines.append("")
        for idx, pm in enumerate(area_pubmed, 1):
            md_lines.append(f"#### {idx}. [{pm['title']}]({pm['url']})")
            md_lines.append(
                f"- **PMID**: {pm['pmid']} | **Journal**: {pm['journal']} ({pm['year']})"
            )
            md_lines.append("")
            md_lines.append("**Abstract**:")
            md_lines.append(f"> {pm['abstract'].replace(chr(10), chr(10) + '> ')}")
            md_lines.append("")

        md_lines.append("---")
        md_lines.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Generated human-readable Markdown KB at: {md_path}")


def main():
    print("=== Question-aligned lean KB scrape (2 Wiki + up to 7 PubMed / focus) ===")
    pubmed_fetcher = PubMedFetcher()
    wiki_fetcher = WikipediaFetcher()

    all_pubmed = []
    all_wiki = []

    for focus_area, config in FOCUS_AREAS_CONFIG.items():
        print(f"\n---> Processing Focus Area: {focus_area}")

        print(f"  Fetching Wikipedia articles ({len(config['wiki_titles'])} topics)...")
        wiki_results = wiki_fetcher.fetch_multiple_articles(config["wiki_titles"])
        for res in wiki_results:
            res["focus_area"] = focus_area
            all_wiki.append(res)
        print(f"  Successfully fetched {len(wiki_results)} Wikipedia articles.")

        seen_pmids = set()
        area_pubmed = []
        for q_idx, query in enumerate(config["pubmed_queries"], 1):
            if len(area_pubmed) >= PUBMED_PER_FOCUS:
                break
            remaining = PUBMED_PER_FOCUS - len(area_pubmed)
            fetch_n = min(PUBMED_MAX_RESULTS_PER_QUERY, remaining)
            print(
                f"  Fetching PubMed [{q_idx}/{len(config['pubmed_queries'])}] "
                f"(max {fetch_n}): '{query}'"
            )
            pubmed_results = pubmed_fetcher.search_and_fetch(query, max_results=fetch_n)
            for res in pubmed_results:
                if len(area_pubmed) >= PUBMED_PER_FOCUS:
                    break
                pmid = res.get("pmid")
                if pmid and pmid not in seen_pmids:
                    seen_pmids.add(pmid)
                    res["focus_area"] = focus_area
                    area_pubmed.append(res)

        all_pubmed.extend(area_pubmed)
        print(
            f"  Collected {len(area_pubmed)} unique PubMed abstracts for {focus_area}."
        )

    save_structured_data(all_pubmed, all_wiki)
    generate_readable_markdown(all_pubmed, all_wiki)
    print(
        f"\n=== Done: {len(all_wiki)} Wikipedia + {len(all_pubmed)} PubMed "
        f"across {len(FOCUS_AREAS_CONFIG)} focus areas ==="
    )


if __name__ == "__main__":
    main()
