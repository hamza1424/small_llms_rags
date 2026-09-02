import os
import re
import time
import pandas as pd
from difflib import SequenceMatcher
from typing import List, Dict, Any, Tuple, Optional, Callable
import nltk
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from rouge_score import rouge_scorer
from rag.bert_scorer import compute_bertscore

# Ensure nltk tokenizer is downloaded silently if needed
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

# Baseline metrics from reference repository (llm_medical_reproducibility-1.0.0)
BASELINE_SCORES = {
    "llama3.1:8b": {
        "token_f1_avg": 0.288,
        "string_similarity_avg": 0.054,
        "bleu_avg": 0.034,
        "rouge_l_avg": 0.171,
        "bertscore_f1_avg": 0.848,
    },
    "medaibase/medgemma1.5:4b": {
        "token_f1_avg": 0.234,
        "string_similarity_avg": 0.046,
        "bleu_avg": 0.017,
        "rouge_l_avg": 0.143,
        "bertscore_f1_avg": 0.842,
    },
    "gemma3:12b": {
        "token_f1_avg": 0.231,
        "string_similarity_avg": 0.049,
        "bleu_avg": 0.019,
        "rouge_l_avg": 0.142,
        "bertscore_f1_avg": 0.842,
    }
}

DEFAULT_REF_PATH = "data/gold_data.csv"
FIXED_50_PATH = "data/benchmark_50_fixed.csv"
TOP_3_FOCUS_AREAS = ["Breast Cancer", "Prostate Cancer", "Stroke"]


def load_benchmark_questions(
    csv_path: str = DEFAULT_REF_PATH,
    focus_areas: Optional[List[str]] = None,
    num_questions: int = 50,
    sample_seed: int = 42,
    use_fixed_50: bool = False
) -> pd.DataFrame:
    """
    Load and randomly sample benchmark questions from selected focus area(s) in gold_data.csv,
    or load the exact fixed 50 benchmark dataset from data/benchmark_50_fixed.csv if use_fixed_50=True.
    """
    if use_fixed_50 or csv_path == FIXED_50_PATH:
        target_path = FIXED_50_PATH
        if not os.path.exists(target_path):
            alt_path = os.path.join(os.path.dirname(__file__), "..", "data", "benchmark_50_fixed.csv")
            if os.path.exists(alt_path):
                target_path = alt_path
        if os.path.exists(target_path):
            f_df = pd.read_csv(target_path)
            if "category" not in f_df.columns and "focus_area" in f_df.columns:
                f_df = f_df.rename(columns={"answer": "gold_answer", "focus_area": "category"})
            return f_df[["question_id", "question", "gold_answer", "category", "source"]]

    if not os.path.exists(csv_path):
        # Fallback to alternative paths if relative directory differs
        alt_path = os.path.join(os.path.dirname(__file__), "..", "data", "gold_data.csv")
        if os.path.exists(alt_path):
            csv_path = alt_path
        else:
            raise FileNotFoundError(f"Gold data file not found at: {csv_path}")
    
    df = pd.read_csv(csv_path)
    
    if "focus_area" in df.columns:
        if focus_areas and "All" not in focus_areas:
            clean_focus = [fa.strip().lower() for fa in focus_areas if fa]
            filtered = df[df["focus_area"].astype(str).str.strip().str.lower().isin(clean_focus)].copy()
        else:
            filtered = df.copy()
            
        if filtered.empty:
            filtered = df.copy()
            
        filtered["question_id"] = [f"q{i+1}" for i in filtered.index]
        
        # Sample num_questions randomly
        n_sample = min(num_questions, len(filtered))
        sampled = filtered.sample(n=n_sample, random_state=sample_seed).reset_index(drop=True)
        sampled = sampled.rename(columns={"answer": "gold_answer", "focus_area": "category"})
        return sampled[["question_id", "question", "gold_answer", "category", "source"]]
    else:
        # Fallback if reference scored_responses.csv is passed directly
        q_df = df[['question_id', 'question', 'gold_answer', 'category']].drop_duplicates(subset=['question_id']).reset_index(drop=True)
        if num_questions and num_questions < len(q_df):
            q_df = q_df.sample(n=num_questions, random_state=sample_seed).reset_index(drop=True)
        return q_df



def get_baseline_scores() -> Dict[str, Dict[str, float]]:
    """
    Returns baseline zero-shot model scores from the reproducibility repository.
    """
    return BASELINE_SCORES


def normalize_text(text: str) -> str:
    """
    Normalizes text for n-gram and token string matching.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


def compute_token_f1(prediction: str, gold: str) -> float:
    """
    Computes token-level precision/recall F1 score between prediction and gold answer.
    """
    pred_tokens = normalize_text(prediction).split()
    gold_tokens = normalize_text(gold).split()
    if not pred_tokens and not gold_tokens:
        return 1.0
    if not pred_tokens or not gold_tokens:
        return 0.0

    pred_counts: Dict[str, int] = {}
    gold_counts: Dict[str, int] = {}
    for tok in pred_tokens:
        pred_counts[tok] = pred_counts.get(tok, 0) + 1
    for tok in gold_tokens:
        gold_counts[tok] = gold_counts.get(tok, 0) + 1

    common = 0
    for tok, n_pred in pred_counts.items():
        n_gold = gold_counts.get(tok, 0)
        common += min(n_pred, n_gold)

    if common == 0:
        return 0.0
    precision = common / len(pred_tokens)
    recall = common / len(gold_tokens)
    return float((2 * precision * recall) / (precision + recall))


def compute_bleu(prediction: str, gold: str) -> float:
    """
    Computes BLEU score using NLTK sentence_bleu.
    """
    norm_pred = normalize_text(prediction).split()
    norm_gold = normalize_text(gold).split()
    if not norm_pred or not norm_gold:
        return 0.0
    smoother = SmoothingFunction().method1
    return float(sentence_bleu([norm_gold], norm_pred, smoothing_function=smoother))


def compute_rouge_l(prediction: str, gold: str) -> float:
    """
    Computes ROUGE-L F1 score using rouge_score.
    """
    norm_pred = normalize_text(prediction)
    norm_gold = normalize_text(gold)
    if not norm_pred or not norm_gold:
        return 0.0
    scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
    score = scorer.score(norm_gold, norm_pred)["rougeL"]
    return float(score.fmeasure)


def compute_string_similarity(prediction: str, gold: str) -> float:
    """
    Computes Levenshtein ratio / SequenceMatcher ratio between normalized strings.
    """
    norm_pred = normalize_text(prediction)
    norm_gold = normalize_text(gold)
    return float(SequenceMatcher(None, norm_pred, norm_gold).ratio())


def batch_bertscore(
    predictions: List[str],
    references: List[str],
    model_type: str = "roberta-base",
    batch_size: int = 8
) -> List[float]:
    """
    Batch BERTScore computation returning list of F1 scores.
    """
    from bert_score import score as bertscore_score
    from rag.memory_utils import cleanup_after_inference

    try:
        _, _, f1_tensor = bertscore_score(
            predictions,
            references,
            model_type=model_type,
            lang="en",
            verbose=False,
            batch_size=batch_size,
        )
        return [float(x) for x in f1_tensor.tolist()]
    finally:
        cleanup_after_inference(clear_cache_dirs=False)


def run_rag_benchmark_50(
    pipeline,
    selected_model: str,
    focus_areas: Optional[List[str]] = None,
    num_questions: int = 50,
    temperature: float = 0.2,
    top_k: int = 3,
    progress_callback: Optional[Callable[[int, int, str], None]] = None,
    use_fixed_50: bool = False
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Runs 100% real-time live evaluation across sampled benchmark questions for:
      1. Medical RAG System (Ours with context)
      2. Llama 3.1 8B (Plain Zero-Shot Live)
      3. MedGemma 1.5 4B (Plain Zero-Shot Live)
      4. Gemma 3 12B (Plain Zero-Shot Live)
    Calculates Token F1, String Similarity, BLEU, ROUGE-L, and BERTScore F1 dynamically for all models in real time.
    """
    questions_df = load_benchmark_questions(
        focus_areas=focus_areas,
        num_questions=num_questions,
        use_fixed_50=use_fixed_50
    )
    total_q = len(questions_df)
    
    results = []
    rag_answers = []
    llama_answers = []
    medgemma_answers = []
    gemma_answers = []
    gold_answers = []
    
    llama_model_id = "llama3.1:8b"
    medgemma_model_id = "medaibase/medgemma1.5:4b"
    gemma_model_id = "gemma3:12b"

    for idx, row in questions_df.iterrows():
        q_id = row['question_id']
        q_text = row['question']
        gold_ans = row['gold_answer']
        category = row.get('category', 'general')
        
        if progress_callback:
            progress_callback(idx + 1, total_q, f"Real-Time Evaluation Q{idx+1}/{total_q} [{q_id}]: \"{q_text[:65]}...\"")
            
        # 1. RAG Query (Ours)
        start_time = time.time()
        rag_ans, retrieved_chunks = pipeline.run_rag_query(
            question=q_text,
            model=selected_model,
            temperature=temperature,
            top_k=top_k
        )
        duration_rag = time.time() - start_time
        
        # 2. Llama 3.1 8B (Plain Zero-Shot Live)
        start_llama = time.time()
        llama_ans = pipeline.run_plain_query(q_text, llama_model_id, temperature)
        duration_llama = time.time() - start_llama
        
        # 3. MedGemma 1.5 4B (Plain Zero-Shot Live)
        start_medgemma = time.time()
        medgemma_ans = pipeline.run_plain_query(q_text, medgemma_model_id, temperature)
        duration_medgemma = time.time() - start_medgemma

        # 4. Gemma 3 12B (Plain Zero-Shot Live)
        start_gemma = time.time()
        gemma_ans = pipeline.run_plain_query(q_text, gemma_model_id, temperature)
        duration_gemma = time.time() - start_gemma

        # Collect text outputs
        rag_answers.append(rag_ans)
        llama_answers.append(llama_ans)
        medgemma_answers.append(medgemma_ans)
        gemma_answers.append(gemma_ans)
        gold_answers.append(gold_ans)
        
        # Compute individual metrics
        res_item = {
            "question_id": q_id,
            "question": q_text,
            "gold_answer": gold_ans,
            "category": category,
            "rag_answer": rag_ans,
            "token_f1": compute_token_f1(rag_ans, gold_ans),
            "string_similarity": compute_string_similarity(rag_ans, gold_ans),
            "bleu": compute_bleu(rag_ans, gold_ans),
            "rouge_l": compute_rouge_l(rag_ans, gold_ans),
            "latency_s": duration_rag,
            "num_chunks_retrieved": len(retrieved_chunks),
            # Llama 3.1 8B Plain Live
            "llama_answer": llama_ans,
            "llama_token_f1": compute_token_f1(llama_ans, gold_ans),
            "llama_string_similarity": compute_string_similarity(llama_ans, gold_ans),
            "llama_bleu": compute_bleu(llama_ans, gold_ans),
            "llama_rouge_l": compute_rouge_l(llama_ans, gold_ans),
            "llama_latency_s": duration_llama,
            # MedGemma 1.5 4B Plain Live
            "medgemma_answer": medgemma_ans,
            "medgemma_token_f1": compute_token_f1(medgemma_ans, gold_ans),
            "medgemma_string_similarity": compute_string_similarity(medgemma_ans, gold_ans),
            "medgemma_bleu": compute_bleu(medgemma_ans, gold_ans),
            "medgemma_rouge_l": compute_rouge_l(medgemma_ans, gold_ans),
            "medgemma_latency_s": duration_medgemma,
            # Gemma 3 12B Plain Live
            "gemma_answer": gemma_ans,
            "gemma_token_f1": compute_token_f1(gemma_ans, gold_ans),
            "gemma_string_similarity": compute_string_similarity(gemma_ans, gold_ans),
            "gemma_bleu": compute_bleu(gemma_ans, gold_ans),
            "gemma_rouge_l": compute_rouge_l(gemma_ans, gold_ans),
            "gemma_latency_s": duration_gemma
        }
        results.append(res_item)
        
    res_df = pd.DataFrame(results)
    
    # Compute BERTScores in batch for accuracy and speed
    if progress_callback:
        progress_callback(total_q, total_q, "Computing real-time contextual BERTScores (roberta-base)...")
        
    res_df["bertscore_f1"] = batch_bertscore(rag_answers, gold_answers, model_type="roberta-base")
    res_df["llama_bertscore_f1"] = batch_bertscore(llama_answers, gold_answers, model_type="roberta-base")
    res_df["medgemma_bertscore_f1"] = batch_bertscore(medgemma_answers, gold_answers, model_type="roberta-base")
    res_df["gemma_bertscore_f1"] = batch_bertscore(gemma_answers, gold_answers, model_type="roberta-base")

    from rag.memory_utils import cleanup_after_inference
    cleanup_after_inference()

    summary = {
        "rag": {
            "model": f"Medical RAG System ({selected_model})",
            "token_f1_avg": float(res_df["token_f1"].mean()),
            "string_similarity_avg": float(res_df["string_similarity"].mean()),
            "bleu_avg": float(res_df["bleu"].mean()),
            "rouge_l_avg": float(res_df["rouge_l"].mean()),
            "bertscore_f1_avg": float(res_df["bertscore_f1"].mean()),
            "latency_s_avg": float(res_df["latency_s"].mean())
        },
        "llama": {
            "model": "Llama 3.1 8B (Plain Zero-Shot Live)",
            "token_f1_avg": float(res_df["llama_token_f1"].mean()),
            "string_similarity_avg": float(res_df["llama_string_similarity"].mean()),
            "bleu_avg": float(res_df["llama_bleu"].mean()),
            "rouge_l_avg": float(res_df["llama_rouge_l"].mean()),
            "bertscore_f1_avg": float(res_df["llama_bertscore_f1"].mean()),
            "latency_s_avg": float(res_df["llama_latency_s"].mean())
        },
        "medgemma": {
            "model": "MedGemma 1.5 4B (Plain Zero-Shot Live)",
            "token_f1_avg": float(res_df["medgemma_token_f1"].mean()),
            "string_similarity_avg": float(res_df["medgemma_string_similarity"].mean()),
            "bleu_avg": float(res_df["medgemma_bleu"].mean()),
            "rouge_l_avg": float(res_df["medgemma_rouge_l"].mean()),
            "bertscore_f1_avg": float(res_df["medgemma_bertscore_f1"].mean()),
            "latency_s_avg": float(res_df["medgemma_latency_s"].mean())
        },
        "gemma": {
            "model": "Gemma 3 12B (Plain Zero-Shot Live)",
            "token_f1_avg": float(res_df["gemma_token_f1"].mean()),
            "string_similarity_avg": float(res_df["gemma_string_similarity"].mean()),
            "bleu_avg": float(res_df["gemma_bleu"].mean()),
            "rouge_l_avg": float(res_df["gemma_rouge_l"].mean()),
            "bertscore_f1_avg": float(res_df["gemma_bertscore_f1"].mean()),
            "latency_s_avg": float(res_df["gemma_latency_s"].mean())
        }
    }
    
    # Auto-save results to benchmark_results directory
    try:
        save_benchmark_results(res_df, selected_model)
    except Exception as e:
        print(f"Warning: Could not auto-save benchmark results: {e}")

    return res_df, summary


def save_benchmark_results(res_df: pd.DataFrame, selected_model: str = "llama3.1_8b", results_dir: str = "benchmark_results") -> str:
    """
    Saves benchmark evaluation results to CSV in the specified benchmark_results directory.
    """
    os.makedirs(results_dir, exist_ok=True)
    safe_model = re.sub(r"[^a-zA-Z0-9_\-]", "_", selected_model)
    filename = f"medical_rag_benchmark_{len(res_df)}_results_{safe_model}.csv"
    filepath = os.path.join(results_dir, filename)
    res_df.to_csv(filepath, index=False)
    return filepath


def load_latest_benchmark_results(results_dir: str = "benchmark_results", selected_model: str = "llama3.1:8b") -> Tuple[Optional[pd.DataFrame], Optional[Dict[str, Any]], Optional[str]]:
    """
    Scans the benchmark_results directory for saved CSV evaluation files and loads the most recent run.
    Reconstructs the summary metrics dictionary for instant UI rendering.
    """
    import glob
    if not os.path.exists(results_dir):
        alt_dir = os.path.join(os.path.dirname(__file__), "..", "benchmark_results")
        if os.path.exists(alt_dir):
            results_dir = alt_dir
        else:
            return None, None, None

    csv_files = glob.glob(os.path.join(results_dir, "*.csv"))
    if not csv_files:
        return None, None, None

    latest_file = max(csv_files, key=os.path.getmtime)
    try:
        df = pd.read_csv(latest_file)
        summary = {}

        if "token_f1" in df.columns:
            summary["rag"] = {
                "model": f"Medical RAG System ({selected_model})",
                "token_f1_avg": float(df["token_f1"].mean()),
                "string_similarity_avg": float(df["string_similarity"].mean()),
                "bleu_avg": float(df["bleu"].mean()) if "bleu" in df.columns else 0.0,
                "rouge_l_avg": float(df["rouge_l"].mean()) if "rouge_l" in df.columns else 0.0,
                "bertscore_f1_avg": float(df["bertscore_f1"].mean()) if "bertscore_f1" in df.columns else 0.0,
                "latency_s_avg": float(df["latency_s"].mean()) if "latency_s" in df.columns else 0.0,
            }
        if "llama_token_f1" in df.columns:
            summary["llama"] = {
                "model": "Llama 3.1 8B (Plain Zero-Shot Live)",
                "token_f1_avg": float(df["llama_token_f1"].mean()),
                "string_similarity_avg": float(df["llama_string_similarity"].mean()),
                "bleu_avg": float(df["llama_bleu"].mean()) if "llama_bleu" in df.columns else 0.0,
                "rouge_l_avg": float(df["llama_rouge_l"].mean()) if "llama_rouge_l" in df.columns else 0.0,
                "bertscore_f1_avg": float(df["llama_bertscore_f1"].mean()) if "llama_bertscore_f1" in df.columns else 0.0,
                "latency_s_avg": float(df["llama_latency_s"].mean()) if "llama_latency_s" in df.columns else 0.0,
            }
        if "medgemma_token_f1" in df.columns:
            summary["medgemma"] = {
                "model": "MedGemma 1.5 4B (Plain Zero-Shot Live)",
                "token_f1_avg": float(df["medgemma_token_f1"].mean()),
                "string_similarity_avg": float(df["medgemma_string_similarity"].mean()),
                "bleu_avg": float(df["medgemma_bleu"].mean()) if "medgemma_bleu" in df.columns else 0.0,
                "rouge_l_avg": float(df["medgemma_rouge_l"].mean()) if "medgemma_rouge_l" in df.columns else 0.0,
                "bertscore_f1_avg": float(df["medgemma_bertscore_f1"].mean()) if "medgemma_bertscore_f1" in df.columns else 0.0,
                "latency_s_avg": float(df["medgemma_latency_s"].mean()) if "medgemma_latency_s" in df.columns else 0.0,
            }
        if "gemma_token_f1" in df.columns:
            summary["gemma"] = {
                "model": "Gemma 3 12B (Plain Zero-Shot Live)",
                "token_f1_avg": float(df["gemma_token_f1"].mean()),
                "string_similarity_avg": float(df["gemma_string_similarity"].mean()),
                "bleu_avg": float(df["bleu_avg"].mean()) if "bleu_avg" in df.columns else float(df["gemma_bleu"].mean()) if "gemma_bleu" in df.columns else 0.0,
                "rouge_l_avg": float(df["gemma_rouge_l"].mean()) if "gemma_rouge_l" in df.columns else 0.0,
                "bertscore_f1_avg": float(df["gemma_bertscore_f1"].mean()) if "gemma_bertscore_f1" in df.columns else 0.0,
                "latency_s_avg": float(df["gemma_latency_s"].mean()) if "gemma_latency_s" in df.columns else 0.0,
            }

        return df, summary, os.path.basename(latest_file)
    except Exception as e:
        print(f"Error loading latest benchmark CSV: {e}")
        return None, None, None

