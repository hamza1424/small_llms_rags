from __future__ import annotations


def compute_bertscore(
    prediction: str,
    reference: str,
    model_type: str = "roberta-base",
    batch_size: int = 8,
) -> dict[str, float]:
    """Compute BERTScore between a prediction and reference."""
    from bert_score import score as bertscore_score
    from rag.memory_utils import cleanup_after_inference

    try:
        p_tensor, r_tensor, f1_tensor = bertscore_score(
            [prediction],
            [reference],
            model_type=model_type,
            lang="en",
            verbose=False,
            batch_size=batch_size,
        )
        return {
            "precision": float(p_tensor[0]),
            "recall": float(r_tensor[0]),
            "f1": float(f1_tensor[0]),
        }
    finally:
        cleanup_after_inference(clear_cache_dirs=False)

