import re
from pathlib import Path
from typing import List, Literal

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_pdf_page_text(text: str) -> List[str]:
    """
    Normalizes PDF extracted text:
    - Normalizes double newlines (or more) into a distinct paragraph marker `\n\n`.
    - Converts single newlines (soft line wraps within a paragraph) into spaces.
    """
    if not text:
        return []
    # Normalize newline variations and multiple blank lines to double newlines
    text = re.sub(r'\r\n|\r', '\n', text)
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    paragraphs = text.split('\n\n')
    cleaned_paragraphs = []

    for p in paragraphs:
        # Convert single line wraps inside a paragraph into single spaces
        cleaned_p = re.sub(r'\s*\n\s*', ' ', p).strip()
        if cleaned_p:
            cleaned_paragraphs.append(cleaned_p)

    return cleaned_paragraphs


def split_text_by_sentences(text: str, max_chunk_size: int = 1000) -> List[str]:
    """
    Splits an oversized paragraph cleanly along sentence boundaries (. ! ?).
    """
    sentence_endings = re.compile(r'(?<=[.!?])\s+')
    sentences = sentence_endings.split(text)

    chunks = []
    curr_chunk = []
    curr_len = 0

    for sentence in sentences:
        s_len = len(sentence)
        if curr_len + s_len > max_chunk_size and curr_chunk:
            chunks.append(" ".join(curr_chunk))
            curr_chunk = []
            curr_len = 0
        curr_chunk.append(sentence)
        curr_len += s_len + 1

    if curr_chunk:
        chunks.append(" ".join(curr_chunk))

    return chunks


def split_documents_by_paragraphs(
    documents: List[Document],
    min_chunk_size: int = 200,
    max_chunk_size: int = 1000,
    target_chunk_size: int = 600,
    chunk_overlap: int = 50,
) -> List[Document]:
    """
    Splits LangChain Document objects by true paragraphs with adaptive merging/splitting.
    """
    final_chunks = []

    for doc in documents:
        page_paragraphs = clean_pdf_page_text(doc.page_content)

        current_paragraph_group = []
        current_length = 0

        for p in page_paragraphs:
            p_len = len(p)

            # Case 1: Oversized single paragraph -> split by sentence boundaries
            if p_len > max_chunk_size:
                if current_paragraph_group:
                    merged_text = "\n\n".join(current_paragraph_group)
                    final_chunks.append(Document(page_content=merged_text, metadata=doc.metadata.copy()))
                    current_paragraph_group = []
                    current_length = 0

                sub_chunks = split_text_by_sentences(p, max_chunk_size=max_chunk_size)
                for sub_c in sub_chunks:
                    final_chunks.append(Document(page_content=sub_c, metadata=doc.metadata.copy()))
                continue

            # Case 2: Accumulate paragraphs until target/max size threshold
            if current_length + p_len > target_chunk_size and current_length >= min_chunk_size:
                merged_text = "\n\n".join(current_paragraph_group)
                final_chunks.append(Document(page_content=merged_text, metadata=doc.metadata.copy()))

                if chunk_overlap > 0 and current_paragraph_group and len(current_paragraph_group[-1]) <= chunk_overlap * 2:
                    current_paragraph_group = [current_paragraph_group[-1], p]
                    current_length = len(current_paragraph_group[0]) + p_len + 2
                else:
                    current_paragraph_group = [p]
                    current_length = p_len
            else:
                current_paragraph_group.append(p)
                current_length += p_len + 2

        if current_paragraph_group:
            merged_text = "\n\n".join(current_paragraph_group)
            final_chunks.append(Document(page_content=merged_text, metadata=doc.metadata.copy()))

    return final_chunks


def load_and_chunk_pdfs(
    pdf_folder: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    strategy: Literal["paragraph", "recursive"] = "paragraph",
    min_paragraph_size: int = 200,
    max_paragraph_size: int = 1000,
) -> List:
    """
    Load PDFs and perform text chunking using selected strategy.

    Args:
        pdf_folder: Folder containing PDF files.
        chunk_size: Target size of text chunks.
        chunk_overlap: Overlap between adjacent chunks.
        strategy: "paragraph" (adaptive paragraph-based) or "recursive" (RecursiveCharacterTextSplitter).
        min_paragraph_size: Minimum character length for paragraph chunks.
        max_paragraph_size: Maximum character length for paragraph chunks.

    Returns:
        List of chunked documents.
    """

    all_chunks = []
    pdf_path = Path(pdf_folder)

    if not pdf_path.exists():
        raise FileNotFoundError(f"{pdf_folder} does not exist.")

    pdf_files = list(pdf_path.glob("*.pdf"))

    if not pdf_files:
        print("No PDFs found.")
        return []

    print(f"Using chunking strategy: '{strategy}'")

    if strategy == "recursive":
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    for pdf_file in pdf_files:
        try:
            print(f"\nProcessing: {pdf_file.name}")

            loader = PyPDFLoader(str(pdf_file))
            documents = loader.load()

            print(f"Loaded {len(documents)} pages")

            if strategy == "paragraph":
                chunks = split_documents_by_paragraphs(
                    documents,
                    min_chunk_size=min_paragraph_size,
                    max_chunk_size=max_paragraph_size,
                    target_chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                )
            else:
                chunks = splitter.split_documents(documents)

            print(f"Created {len(chunks)} chunks")

            all_chunks.extend(chunks)

        except Exception as e:
            print(f"Failed: {pdf_file.name}")
            print(e)

    print(f"\nTotal Chunks: {len(all_chunks)}")

    return all_chunks



def load_and_chunk_csv(
    csv_path: str,
    text_column: str = "answer",
    max_rows: int | None = None,
    focus_area: str | None = None,
) -> List:
    """
    Load CSV data and convert every answer entry into a Document chunk.
    """
    import pandas as pd
    from langchain_core.documents import Document

    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(path)
    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in CSV. Available: {df.columns.tolist()}")

    if focus_area and "focus_area" in df.columns and focus_area.lower() != "all":
        df = df[df["focus_area"].str.lower() == focus_area.lower()]

    if max_rows and max_rows > 0:
        df = df.head(max_rows)

    documents = []
    for idx, row in df.iterrows():
        ans_text = str(row[text_column]).strip()
        if not ans_text or ans_text.lower() == "nan":
            continue

        q_text = str(row["question"]).strip() if "question" in df.columns else ""
        source = str(row["source"]).strip() if "source" in df.columns else "Gold CSV"
        cat = str(row["focus_area"]).strip() if "focus_area" in df.columns else ""

        # Only the answer is included as knowledge base chunk content
        content = ans_text

        doc = Document(
            page_content=content,
            metadata={
                "source": source,
                "focus_area": cat,
                "question": q_text,
                "answer": ans_text,
                "row_id": int(idx),
            }
        )
        documents.append(doc)

    print(f"Loaded {len(documents)} CSV answer chunks from {path.name}.")
    return documents


def load_and_chunk_scraped_kb(
    kb_folder: str = "data/scraped_kb",
    focus_area: str | None = None,
    source_type: str = "all",
    chunk_size: int = 600,
    chunk_overlap: int = 50,
) -> List:
    """
    Load external scraped PubMed abstracts and Wikipedia articles,
    chunk Wikipedia long texts into paragraphs, and format into Document objects.
    """
    import json
    from pathlib import Path
    from langchain_core.documents import Document

    path = Path(kb_folder)
    if not path.exists():
        raise FileNotFoundError(f"Scraped KB folder not found: {kb_folder}")

    wiki_path = path / "wikipedia_articles.json"
    pubmed_path = path / "pubmed_abstracts.json"

    documents = []

    # 1. Load Wikipedia Articles
    if source_type.lower() in ["all", "wikipedia"] and wiki_path.exists():
        with open(wiki_path, "r", encoding="utf-8") as f:
            wiki_data = json.load(f)

        for item in wiki_data:
            cat = item.get("focus_area", "")
            if focus_area and focus_area.lower() != "all" and cat.lower() != focus_area.lower():
                continue

            full_text = item.get("full_text", "").strip()
            title = item.get("title", "Wikipedia Article")
            url = item.get("url", "")

            if full_text:
                raw_doc = Document(
                    page_content=full_text,
                    metadata={
                        "source": f"Wikipedia ({title})",
                        "title": title,
                        "focus_area": cat,
                        "url": url,
                        "type": "Wikipedia"
                    }
                )
                # Split large Wikipedia articles into adaptive paragraph chunks
                para_chunks = split_documents_by_paragraphs(
                    [raw_doc],
                    min_chunk_size=150,
                    max_chunk_size=1000,
                    target_chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                )
                documents.extend(para_chunks)

    # 2. Load PubMed Abstracts
    if source_type.lower() in ["all", "pubmed"] and pubmed_path.exists():
        with open(pubmed_path, "r", encoding="utf-8") as f:
            pubmed_data = json.load(f)

        for item in pubmed_data:
            cat = item.get("focus_area", "")
            if focus_area and focus_area.lower() != "all" and cat.lower() != focus_area.lower():
                continue

            title = item.get("title", "")
            abstract = item.get("abstract", "").strip()
            pmid = item.get("pmid", "")
            journal = item.get("journal", "")
            year = item.get("year", "")
            url = item.get("url", "")

            if title and abstract:
                content = f"Title: {title}\nJournal: {journal} ({year})\nAbstract:\n{abstract}"
                doc = Document(
                    page_content=content,
                    metadata={
                        "source": f"PubMed (PMID:{pmid})",
                        "title": title,
                        "focus_area": cat,
                        "pmid": pmid,
                        "journal": journal,
                        "year": year,
                        "url": url,
                        "type": "PubMed Abstract"
                    }
                )
                documents.append(doc)

    print(f"Loaded {len(documents)} external KB document chunks from {kb_folder}.")
    return documents