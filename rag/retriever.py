from typing import List, Dict, Any

from rag.vector_store import MedicalVectorStore
from rag.reranker import CrossEncoderReranker


class MedicalRetriever:

    def __init__(self, vector_store: MedicalVectorStore):
        self.vector_store = vector_store
        self.reranker = CrossEncoderReranker()

    def retrieve_context(
        self,
        question: str,
        top_k: int = 3,
        initial_k: int = 20
    ) -> List[Dict[str, Any]]:

        results = self.vector_store.query(
            question,
            top_k=initial_k
        )

        retrieved_items = []

        if not results or "documents" not in results:
            return []

        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]
        dists = results.get("distances", [[]])[0]

        for idx in range(len(docs)):
            retrieved_items.append({
                "text": docs[idx],
                "metadata": metas[idx] if idx < len(metas) else {},
                "distance": dists[idx] if idx < len(dists) else 0.0,
            })

        reranked = self.reranker.rerank(
            question,
            retrieved_items,
            top_k=top_k
        )

        return reranked