from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_chunk_pdfs(
    pdf_folder: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> List:
    """
    Load PDFs and perform text chunking using RecursiveCharacterTextSplitter.

    Args:
        pdf_folder: Folder containing PDF files.
        chunk_size: Size of text chunks.
        chunk_overlap: Overlap between adjacent chunks.

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