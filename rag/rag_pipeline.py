import os
import yaml
import requests
from typing import List, Dict, Any, Tuple
from rag.document_loader import load_and_chunk_pdfs
from rag.embedder import MedicalEmbedder
from rag.vector_store import MedicalVectorStore
from rag.retriever import MedicalRetriever

def load_config(config_path: str = "configs/rag_config.yaml") -> Dict[str, Any]:
    """
    Load configuration from yaml file.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

class MedicalRAGPipeline:
    """
    Main pipeline orchestrating the RAG components and LLM querying.
    """
    def __init__(self, config_path: str = "configs/rag_config.yaml"):
        """
        Initialize the RAG pipeline components from the configuration.
        """
        self.config = load_config(config_path)
        
        # Initialize embedder
        emb_model = self.config['retrieval']['embedding_model']
        device = self.config['retrieval'].get('device')
        self.embedder = MedicalEmbedder(model_name=emb_model, device=device)
        
        # Initialize vector store
        db_path = self.config['vector_store']['path']
        collection_name = self.config['vector_store']['collection_name']
        self.vector_store = MedicalVectorStore(
            db_path=db_path,
            collection_name=collection_name,
            embedder=self.embedder
        )
        
        # Initialize retriever
        self.retriever = MedicalRetriever(vector_store=self.vector_store)
        
        # Ollama settings
        self.ollama_base_url = self.config['ollama']['base_url']

    def ingest_documents(self) -> int:
        """
        Scan knowledge base folder, load PDFs, split them, and add to vector store.
        """
        kb_folder = self.config['knowledge_base']['folder']
        chunk_size = self.config['knowledge_base']['chunk_size']
        chunk_overlap = self.config['knowledge_base']['chunk_overlap']
        
        print(f"Starting ingestion from folder: {kb_folder}")
        chunks = load_and_chunk_pdfs(
            pdf_folder=kb_folder,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        if not chunks:
            print("No document chunks loaded.")
            return 0
            
        added_count = self.vector_store.add_chunks(chunks, clear_existing=True)
        return added_count

    def ingest_csv_documents(
        self,
        csv_file: str = "data/gold_data.csv",
        text_column: str = "answer",
        max_rows: int | None = None,
        focus_area: str | None = None,
        clear_existing: bool = True,
    ) -> int:
        """
        Load gold dataset CSV answers, format as document chunks, and add to vector store.
        """
        from rag.document_loader import load_and_chunk_csv

        print(f"Starting CSV ingestion from file: {csv_file}")
        chunks = load_and_chunk_csv(
            csv_path=csv_file,
            text_column=text_column,
            max_rows=max_rows,
            focus_area=focus_area,
        )

        if not chunks:
            print("No CSV document chunks loaded.")
            return 0

        added_count = self.vector_store.add_chunks(chunks, clear_existing=clear_existing)
        return added_count


    def build_rag_prompt(self, question: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """
        Build an enriched clinical prompt with retrieved context.
        """
        contexts = [item['text'] for item in retrieved_chunks]
        context_str = "\n\n".join(contexts)
        
        prompt = f"""You are a clinical expert. Use the following medical information to answer the question accurately.
If the context does not contain enough information, say so clearly. Be direct and answer in 6 sentences or less.

Context:
{context_str}

Question: {question}

Answer:"""
        return prompt

    def build_plain_prompt(self, question: str) -> str:
        """
        Build a plain prompt matching the same instruction system but without context.
        """
        prompt = f"""You are a clinical expert. Answer the following medical question directly.
Answer in 6 sentences or less. If uncertain, say so. Never recommend unsafe actions.

Question: {question}

Answer:"""
        return prompt

    def query_ollama(self, prompt: str, model: str, temperature: float = 0.2) -> str:
        """
        Send a generation request to the local Ollama instance.
        """
        url = f"{self.ollama_base_url.rstrip('/')}/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }
        
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except requests.exceptions.RequestException as e:
            return f"Ollama API Connection Error: {str(e)}"

    def run_rag_query(self, question: str, model: str, temperature: float = 0.2, top_k: int = 3) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Execute a full RAG query: retrieve context, enrich prompt, and generate answer.
        """
        # Step 1: Retrieve context
        retrieved_chunks = self.retriever.retrieve_context(question, top_k=top_k)
        
        # Step 2: Build enriched prompt
        prompt = self.build_rag_prompt(question, retrieved_chunks)
        
        # Step 3: Call LLM
        answer = self.query_ollama(prompt, model, temperature)
        
        return answer, retrieved_chunks

    def run_plain_query(self, question: str, model: str, temperature: float = 0.2) -> str:
        """
        Execute a plain query without retrieval context.
        """
        prompt = self.build_plain_prompt(question)
        return self.query_ollama(prompt, model, temperature)
