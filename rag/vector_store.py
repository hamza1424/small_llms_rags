import os
import chromadb
from typing import List, Dict, Any
from rag.embedder import MedicalEmbedder

class MedicalVectorStore:
    """
    Manages vector storage in ChromaDB, including ingestion and querying.
    """
    def __init__(
        self, 
        db_path: str = "./chroma_db", 
        collection_name: str = "medical_knowledge",
        embedder: MedicalEmbedder = None
    ):
        """
        Initialize ChromaDB persistent client and collection.
        """
        self.db_path = db_path
        self.collection_name = collection_name
        self.embedder = embedder or MedicalEmbedder()
        
        # Ensure directory exists
        os.makedirs(db_path, exist_ok=True)
        
        # Initialize client
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def add_chunks(self, chunks: List[Any], clear_existing: bool = True) -> int:
        """
        Embed and store document chunks in ChromaDB.
        
        Args:
            chunks: List of LangChain Document objects.
            clear_existing: If True, deletes existing collection contents before adding.
            
        Returns:
            Number of successfully added chunks.
        """
        if not chunks:
            print("No chunks provided to add.")
            return 0
            
        if clear_existing:
            self.clear_collection()
            
        print(f"Embedding and storing {len(chunks)} chunks in collection '{self.collection_name}'...")
        
        # Extract contents and metadata
        documents = [chunk.page_content for chunk in chunks]
        metadatas = []
        for chunk in chunks:
            # Clean metadata to ensure only simple types (str, int, float, bool)
            meta = {}
            for k, v in chunk.metadata.items():
                if isinstance(v, (str, int, float, bool)):
                    meta[k] = v
                else:
                    meta[k] = str(v)
            metadatas.append(meta)
            
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        
        # Batch generation of embeddings (more efficient than one-by-one)
        embeddings = self.embedder.encode(documents)
        
        # Add to ChromaDB in batches (Chroma has limits on batch size, but len(chunks) for our pdf is small)
        batch_size = 200
        for i in range(0, len(chunks), batch_size):
            end_idx = min(i + batch_size, len(chunks))
            self.collection.add(
                ids=ids[i:end_idx],
                embeddings=embeddings[i:end_idx],
                documents=documents[i:end_idx],
                metadatas=metadatas[i:end_idx]
            )
            
        print(f"Successfully added {len(chunks)} chunks.")
        return len(chunks)

    def query(self, query_text: str, top_k: int = 3) -> Dict[str, Any]:
        """
        Query vector store for top_k most similar chunks.
        
        Args:
            query_text: The user question.
            top_k: Number of relevant results to return.
            
        Returns:
            Dict containing retrieved documents, metadata, and distances.
        """
        # Embed the query
        query_embedding = self.embedder.encode(query_text)
        
        # Search the database
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results

    def clear_collection(self):
        """
        Delete all items in the current collection.
        """
        try:
            # ChromaDB doesn't have a direct truncate, so we delete by deleting the collection and recreating it
            self.client.delete_collection(self.collection_name)
            self.collection = self.client.get_or_create_collection(self.collection_name)
            print(f"Collection '{self.collection_name}' has been cleared.")
        except Exception as e:
            print(f"Error clearing collection: {str(e)}")

    def get_chunk_count(self) -> int:
        """
        Get the total number of items stored in the collection.
        """
        try:
            return self.collection.count()
        except Exception:
            return 0
