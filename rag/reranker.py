# rag/reranker.py

from sentence_transformers import CrossEncoder


class CrossEncoderReranker:
    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):
        self.model = CrossEncoder(model_name)

    def rerank(self, query, documents, top_k=3):
        """
        documents -> List[dict]
        """

        if not documents:
            return []

        pairs = [
            (query, doc["text"])
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        for doc, score in zip(documents, scores):
            doc["cross_score"] = float(score)

        documents.sort(
            key=lambda x: x["cross_score"],
            reverse=True
        )

        return documents[:top_k]