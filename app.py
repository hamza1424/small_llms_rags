import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import time
import pandas as pd
from typing import List, Dict, Any
from rag.rag_pipeline import MedicalRAGPipeline
from rag.gold_loader import load_gold_dataset, filter_by_focus_area
from rag.bert_scorer import compute_bertscore
from rag.benchmark import run_rag_benchmark_50, get_baseline_scores, load_benchmark_questions, load_latest_benchmark_results
from rag.memory_utils import cleanup_after_inference

# Set page configuration with medical theme emojis
st.set_page_config(
    page_title="Med-RAG: Clinical QA & Reproducibility Lab",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for high-quality, premium aesthetic (glassmorphism details, custom card containers, color alerts)
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }
    .stApp [data-testid="stSidebar"] {
        background-color: #0e1e38;
        color: #ffffff;
    }
    .stApp [data-testid="stSidebar"] svg {
        fill: #ffffff;
    }
    .stApp [data-testid="stSidebar"] .stMarkdown p {
        color: #e2e8f0;
    }
    .medical-header {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .medical-header h1 {
        margin: 0;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
    }
    .medical-header p {
        margin: 8px 0 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        border-left: 5px solid #10b981;
        margin-bottom: 16px;
    }
    .chunk-card {
        background-color: #f8fafc;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 12px;
    }
    .plain-response {
        background-color: #fffbeb;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #fef3c7;
        border-left: 5px solid #f59e0b;
        height: 100%;
    }
    .rag-response {
        background-color: #ecfdf5;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #d1fae5;
        border-left: 5px solid #10b981;
        height: 100%;
    }
    .gold-response {
        background-color: #eff6ff;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #bfdbfe;
        border-left: 5px solid #3b82f6;
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Cache RAG Pipeline initialization to speed up reloads
@st.cache_resource
def get_pipeline():
    try:
        return MedicalRAGPipeline(config_path="configs/rag_config.yaml")
    except Exception as e:
        st.error(f"Error initializing pipeline: {e}")
        return None

pipeline = get_pipeline()

if pipeline is None:
    st.stop()


@st.cache_data
def get_gold_dataset(config: dict) -> pd.DataFrame:
    gold_cfg = config.get("gold_data", {})
    return load_gold_dataset(
        folder=gold_cfg.get("folder", "data"),
        csv_file=gold_cfg.get("csv_file", "gold_data.csv"),
    )


@st.cache_resource
def get_bertscore_config(config: dict) -> dict:
    return config.get("bertscore", {"model": "roberta-base", "batch_size": 8})

# --- SIDEBAR: Settings & Operations ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/stethoscope.png", width=64)
    st.title("Control Center")
    st.write("Configure models, retrieval, and databases.")
    
    st.markdown("---")
    
    # 1. Model Configuration
    st.subheader("🤖 LLM Settings")
    available_models = pipeline.config['ollama']['models']
    selected_model = st.selectbox(
        "Select Ollama Model",
        options=available_models,
        index=0
    )
    
    temperature = st.slider(
        "Temperature (Creativity)",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.05,
        help="Lower values make outputs more deterministic and factual."
    )
    
    # 2. Retrieval Configuration
    st.subheader("🔍 Retrieval Settings")
    top_k = st.slider(
        "Top K chunks to retrieve",
        min_value=1,
        max_value=8,
        value=pipeline.config['retrieval']['top_k'],
        step=1
    )
    
    st.markdown("---")
    
    # 3. Vector Database Management
    st.subheader("📁 Knowledge Base DB")
    
    chunk_count = pipeline.vector_store.get_chunk_count()
    st.metric(label="Documents in Index", value=f"{chunk_count} Chunks")

    ingest_source = st.selectbox(
        "Ingestion Data Source",
        options=[
            "🌐 External Scraped KB (PubMed & Wikipedia)",
            "📊 Gold CSV Answers (data/gold_data.csv)"
        ],
        index=0,
        key="sb_ingest_source"
    )

    if "External Scraped KB" in ingest_source:
        kb_filter = st.selectbox(
            "Filter KB by Focus Area",
            options=[
                "All",
                "Breast Cancer",
                "Prostate Cancer",
                "Stroke",
                "Skin Cancer",
                "Alzheimer's Disease",
                "Colorectal Cancer",
                "Lung Cancer",
                "High Blood Cholesterol",
                "Heart Attack",
                "Heart Failure"
            ],
            index=0,
            key="sb_ext_kb_filter"
        )
        kb_source_type = st.selectbox(
            "Filter Source Type",
            options=["All Sources", "Wikipedia Only", "PubMed Only"],
            index=0,
            key="sb_ext_kb_source"
        )
        if st.button("📥 Index External Knowledge Base", use_container_width=True, key="btn_ingest_ext_kb"):
            with st.spinner(f"Loading external KB ({kb_filter} / {kb_source_type}), embedding chunks & storing in ChromaDB..."):
                try:
                    start_time = time.time()
                    st_code = "all"
                    if "Wikipedia" in kb_source_type:
                        st_code = "wikipedia"
                    elif "PubMed" in kb_source_type:
                        st_code = "pubmed"

                    added = pipeline.ingest_scraped_kb(
                        kb_folder="data/scraped_kb",
                        focus_area=None if kb_filter == "All" else kb_filter,
                        source_type=st_code,
                        clear_existing=True
                    )
                    duration = time.time() - start_time
                    st.success(f"Indexed {added} external KB chunks in {duration:.2f} seconds!")
                    st.rerun()
                except Exception as e:
                    st.error(f"External KB Ingestion failed: {e}")

    elif "Gold CSV Answers" in ingest_source:
        csv_filter = st.selectbox(
            "Filter CSV by Focus Area",
            options=["All", "Diabetes", "Glaucoma", "Breast Cancer", "Heart Attack", "Stroke"],
            index=0,
            key="sb_csv_filter"
        )
        if st.button("📥 Index Gold CSV Answers", use_container_width=True, key="btn_ingest_csv"):
            with st.spinner(f"Loading CSV answers ({csv_filter}), embedding chunks & storing in ChromaDB..."):
                try:
                    start_time = time.time()
                    added = pipeline.ingest_csv_documents(
                        csv_file="data/gold_data.csv",
                        text_column="answer",
                        focus_area=None if csv_filter == "All" else csv_filter,
                        clear_existing=True
                    )
                    duration = time.time() - start_time
                    st.success(f"Indexed {added} CSV chunks in {duration:.2f} seconds!")
                    st.rerun()
                except Exception as e:
                    st.error(f"CSV Ingestion failed: {e}")

    if st.button("🗑️ Clear Vector Index", use_container_width=True, key="btn_clear_db"):
        pipeline.vector_store.clear_collection()
        st.success("Vector store index cleared!")
        st.rerun()

# --- MAIN APP LAYOUT ---
# Header Banner
st.markdown("""
<div class="medical-header">
    <h1>🩺 Med-RAG</h1>
    <p>Clinical Question-Answering & Large Language Model Reproducibility Laboratory</p>
</div>
""", unsafe_allow_html=True)

# Setup tabs
tab_query, tab_gold_eval, tab_benchmark, tab_consistency, tab_explorer = st.tabs([
    "💬 Side-by-Side Playground",
    "📊 Gold Dataset Evaluation",
    "🏆 Benchmark Evaluation (50 Qs)",
    "📈 Consistency & Reproducibility Evaluator",
    "🔍 Knowledge Base Explorer"
])

# --- TAB 1: Single Query Playground ---
with tab_query:
    st.subheader("Compare Plain LLM vs. RAG Pipeline")
    st.write("Input a clinical question below to observe the effect of external medical knowledge grounding.")
    
    # Pre-populated suggestions
    suggestions = [
        "What is diabetes?",
        "What causes a diabetes hyper (hyperglycaemia)?",
        "What are the long-term complications of diabetes?",
        "How can someone prevent diabetes?"
    ]
    
    col_sug1, col_sug2, col_sug3, col_sug4 = st.columns(4)
    with col_sug1:
        if st.button(suggestions[0], use_container_width=True):
            st.session_state.query_text = suggestions[0]
    with col_sug2:
        if st.button(suggestions[1], use_container_width=True):
            st.session_state.query_text = suggestions[1]
    with col_sug3:
        if st.button(suggestions[2], use_container_width=True):
            st.session_state.query_text = suggestions[2]
    with col_sug4:
        if st.button(suggestions[3], use_container_width=True):
            st.session_state.query_text = suggestions[3]
            
    # Text input for query
    query_input = st.text_input(
        "Enter your medical query:",
        value=st.session_state.get('query_text', "What is diabetes?"),
        key="main_query_input"
    )
    
    if st.button("🚀 Run Comparison Query", type="primary"):
        if not query_input.strip():
            st.warning("Please enter a question.")
        else:
            col_plain, col_rag = st.columns(2)
            
            # Run Plain LLM Query
            with col_plain:
                st.markdown("### ⚠️ Plain LLM Response (No Context)")
                with st.spinner("Generating plain answer..."):
                    start = time.time()
                    plain_ans = pipeline.run_plain_query(query_input, selected_model, temperature)
                    plain_dur = time.time() - start
                st.markdown(f'<div class="plain-response">{plain_ans}</div>', unsafe_allow_html=True)
                st.caption(f"Generated in {plain_dur:.2f}s")
                
            # Run RAG Query
            with col_rag:
                st.markdown("### ✅ RAG-Augmented Response")
                with st.spinner("Retrieving context & generating answer..."):
                    start = time.time()
                    rag_ans, retrieved_chunks = pipeline.run_rag_query(
                        query_input, 
                        selected_model, 
                        temperature, 
                        top_k
                    )
                    rag_dur = time.time() - start
                st.markdown(f'<div class="rag-response">{rag_ans}</div>', unsafe_allow_html=True)
                st.caption(f"Generated in {rag_dur:.2f}s")

            cleanup_after_inference()
                
            # Display Retrieved Chunks
            st.markdown("---")
            st.markdown("### 📚 Grounding Source Documents")
            if not retrieved_chunks:
                st.warning("No grounding contexts were retrieved from the database.")
            else:
                for idx, chunk in enumerate(retrieved_chunks):
                    with st.expander(
                        f"Chunk {idx+1} — Source: {chunk['metadata'].get('source')} — Distance Score: {chunk['distance']:.4f}",
                        expanded=(idx == 0)
                    ):
                        st.markdown(f"**Retrieved Content:**")
                        st.write(chunk['text'])
                        st.caption(f"Metadata: {chunk['metadata']}")

# --- TAB 2: Gold Dataset Evaluation ---
with tab_gold_eval:
    st.subheader("📊 Dual BERTScore Evaluation: Plain LLM & RAG vs. Ground Truth")
    st.write(
        "Compare how accurately both **Plain LLM** and **RAG-Augmented** responses "
        "align with Ground Truth clinical reference answers using **BERTScore** (RoBERTa contextual semantic similarity)."
    )

    data_source = st.radio(
        "Select Evaluation Data Source:",
        options=["📋 Gold Dataset CSV", "✍️ Custom Question & Reference Answer"],
        horizontal=True,
        key="eval_data_source"
    )

    question_text = ""
    gold_answer = ""
    can_proceed = False

    if data_source == "📋 Gold Dataset CSV":
        try:
            gold_df = get_gold_dataset(pipeline.config)
        except Exception as e:
            st.error(f"Failed to load gold dataset: {e}")
            gold_df = None

        if gold_df is not None:
            gold_cfg = pipeline.config.get("gold_data", {})
            focus_areas = sorted(gold_df["category"].dropna().unique().tolist())
            default_focus = gold_cfg.get("default_focus_area", "Diabetes")

            if default_focus in focus_areas:
                default_index = focus_areas.index(default_focus)
            else:
                default_index = 0

            selected_focus = st.selectbox(
                "Filter by focus area",
                options=focus_areas,
                index=default_index,
            )

            filtered_df = filter_by_focus_area(gold_df, selected_focus)
            st.caption(f"{len(filtered_df)} questions available for **{selected_focus}**")

            if default_focus != selected_focus:
                st.warning(
                    f"The active knowledge base index may not contain context for **{selected_focus}**. "
                    f"Ensure you index the corresponding focus area in the sidebar."
                )

            if filtered_df.empty:
                st.warning("No questions found for the selected focus area.")
            else:
                question_labels = [
                    f"{row['id']}: {row['question'][:80]}{'...' if len(row['question']) > 80 else ''}"
                    for _, row in filtered_df.iterrows()
                ]
                selected_idx = st.selectbox(
                    "Select question from gold dataset",
                    options=range(len(filtered_df)),
                    format_func=lambda i: question_labels[i],
                )

                selected_row = filtered_df.iloc[selected_idx]
                question_text = selected_row["question"]
                gold_answer = selected_row["gold_answer"]
                can_proceed = True
    else:
        question_text = st.text_input("Enter Question:", value="What is diabetes?", key="custom_eval_q")
        gold_answer = st.text_area(
            "Enter Ground Truth / Reference Answer:",
            value="Diabetes is a chronic disease that occurs when blood glucose (sugar) levels are too high. "
                  "Insulin helps glucose get into cells to be used for energy.",
            key="custom_eval_gold"
        )
        if question_text.strip() and gold_answer.strip():
            can_proceed = True
        else:
            st.warning("Please provide both a question and a reference ground truth answer.")

    if can_proceed and question_text and gold_answer:
        st.markdown("#### 📋 Ground Truth Reference Answer")
        st.markdown(f'<div class="gold-response">{gold_answer}</div>', unsafe_allow_html=True)
        st.markdown(" ")

        if st.button("🚀 Run Dual BERTScore Evaluation", type="primary", key="dual_bert_eval_run"):
            with st.spinner("Generating Plain LLM answer (no context)..."):
                start_p = time.time()
                plain_ans = pipeline.run_plain_query(question_text, selected_model, temperature)
                dur_p = time.time() - start_p

            with st.spinner("Generating RAG-Augmented answer..."):
                start_r = time.time()
                rag_ans, retrieved_chunks = pipeline.run_rag_query(
                    question_text,
                    selected_model,
                    temperature,
                    top_k,
                )
                dur_r = time.time() - start_r

            with st.spinner("Computing BERTScores for Plain LLM & RAG vs. Ground Truth..."):
                bert_cfg = get_bertscore_config(pipeline.config)
                model_type = bert_cfg.get("model", "roberta-base")
                batch_size = bert_cfg.get("batch_size", 8)

                scores_plain = compute_bertscore(
                    prediction=plain_ans,
                    reference=gold_answer,
                    model_type=model_type,
                    batch_size=batch_size,
                )
                scores_rag = compute_bertscore(
                    prediction=rag_ans,
                    reference=gold_answer,
                    model_type=model_type,
                    batch_size=batch_size,
                )
            cleanup_after_inference()

            # --- Display Responses Side-by-Side ---
            col_p, col_r = st.columns(2)
            with col_p:
                st.markdown("### ⚠️ Plain LLM Answer")
                st.markdown(f'<div class="plain-response">{plain_ans}</div>', unsafe_allow_html=True)
                st.caption(f"Generated in {dur_p:.2f}s")
            with col_r:
                st.markdown("### ✅ RAG Pipeline Answer")
                st.markdown(f'<div class="rag-response">{rag_ans}</div>', unsafe_allow_html=True)
                st.caption(f"Generated in {dur_r:.2f}s")

            # --- Display Metric Comparison & Gains ---
            st.markdown("---")
            st.markdown("### 📊 BERTScore Metric Comparison (vs. Ground Truth)")

            delta_f1 = scores_rag["f1"] - scores_plain["f1"]
            delta_p = scores_rag["precision"] - scores_plain["precision"]
            delta_r = scores_rag["recall"] - scores_plain["recall"]

            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(
                    label="RAG BERTScore F1",
                    value=f"{scores_rag['f1']:.4f}",
                    delta=f"{delta_f1:+.4f} vs Plain"
                )
                st.caption(f"Plain LLM F1: **{scores_plain['f1']:.4f}**")
            with m2:
                st.metric(
                    label="RAG Precision",
                    value=f"{scores_rag['precision']:.4f}",
                    delta=f"{delta_p:+.4f} vs Plain"
                )
                st.caption(f"Plain LLM Precision: **{scores_plain['precision']:.4f}**")
            with m3:
                st.metric(
                    label="RAG Recall",
                    value=f"{scores_rag['recall']:.4f}",
                    delta=f"{delta_r:+.4f} vs Plain"
                )
                st.caption(f"Plain LLM Recall: **{scores_plain['recall']:.4f}**")

            # Comparison Table
            st.markdown("#### 📈 Detailed Metrics Comparison Table")
            metrics_df = pd.DataFrame({
                "Metric": ["BERTScore F1", "Precision", "Recall"],
                "Plain LLM": [
                    f"{scores_plain['f1']:.4f}",
                    f"{scores_plain['precision']:.4f}",
                    f"{scores_plain['recall']:.4f}",
                ],
                "RAG Pipeline": [
                    f"{scores_rag['f1']:.4f}",
                    f"{scores_rag['precision']:.4f}",
                    f"{scores_rag['recall']:.4f}",
                ],
                "Δ Improvement (RAG Gain)": [
                    f"{delta_f1:+.4f}",
                    f"{delta_p:+.4f}",
                    f"{delta_r:+.4f}",
                ],
            })
            st.dataframe(metrics_df, use_container_width=True, hide_index=True)

            st.caption(
                "BERTScore measures contextual semantic similarity using RoBERTa embeddings. "
                "The Δ Improvement highlights the performance gain achieved by retrieval grounding over plain generation."
            )

            if retrieved_chunks:
                st.markdown("#### 📚 Grounding Source Chunks")
                for idx, chunk in enumerate(retrieved_chunks):
                    with st.expander(
                        f"Chunk {idx + 1} — Distance: {chunk['distance']:.4f}",
                        expanded=(idx == 0),
                    ):
                        st.write(chunk["text"])

# --- TAB 3: 🏆 Benchmark Evaluation (50 Qs) ---
with tab_benchmark:
    st.subheader("🏆 Medical RAG 50-Question Benchmark Evaluation")
    st.write(
        "Evaluate our **Medical RAG System** against the 50 reference clinical questions from the "
        "`llm_medical_reproducibility-1.0.0` benchmark. Compare our similarity scores directly against "
        "the reference zero-shot LLM baselines (`llama3.1:8b`, `gemma3:12b`, `medaibase/medgemma1.5:4b`)."
    )

    # Auto-load latest benchmark results from disk if available and session_state is empty
    if "benchmark_results_df" not in st.session_state or st.session_state.benchmark_results_df is None:
        c_df, c_summary, c_file = load_latest_benchmark_results(selected_model=selected_model)
        if c_df is not None and c_summary is not None:
            st.session_state.benchmark_results_df = c_df
            st.session_state.benchmark_summary = c_summary
            st.session_state.benchmark_source_file = c_file

    st.markdown("### 🎯 Benchmark Evaluation Mode & Configuration")
    
    bench_mode = st.radio(
        "Choose Benchmark Dataset Mode:",
        options=[
            "🎯 Fixed 50 Benchmark Questions (Top 10 Focus Areas - Deterministic & Reproducible)",
            "🎲 Custom Dynamic Sample (User-Selected Focus Areas & Question Count)"
        ],
        index=0,
        help="Fixed mode runs the exact 50 reference questions across the Top 10 focus areas. Dynamic mode samples randomly based on your custom criteria."
    )

    use_fixed_50 = "Fixed 50" in bench_mode

    if not use_fixed_50:
        try:
            gold_df_bench = get_gold_dataset(pipeline.config)
            avail_categories = sorted([c for c in gold_df_bench["category"].dropna().unique().tolist() if c and str(c).strip() and str(c).lower() != "nan"])
        except Exception:
            avail_categories = ["Breast Cancer", "Prostate Cancer", "Stroke", "Diabetes", "Glaucoma", "High Blood Pressure"]

        top_10_focus_areas = [
            "Breast Cancer",
            "Prostate Cancer",
            "Stroke",
            "Skin Cancer",
            "Alzheimer's Disease",
            "Colorectal Cancer",
            "Lung Cancer",
            "High Blood Cholesterol",
            "Heart Attack",
            "Heart Failure"
        ]
        default_selected = [fa for fa in top_10_focus_areas if fa in avail_categories] if 'avail_categories' in locals() else top_10_focus_areas
        focus_options = ["All Focus Areas"] + avail_categories

        col_fa, col_num = st.columns([2, 1])
        with col_fa:
            selected_focus_areas = st.multiselect(
                "Select Clinical Focus Area(s):",
                options=focus_options,
                default=default_selected,
                help="Select one or more medical categories from gold_data.csv to sample benchmark questions from."
            )
        with col_num:
            num_benchmark_questions = st.number_input(
                "Number of Questions to Sample:",
                min_value=1,
                max_value=500,
                value=50,
                step=5,
                help="Set how many questions to randomly sample from the selected focus areas."
            )

        if "All Focus Areas" in selected_focus_areas or not selected_focus_areas:
            chosen_fa = None
            matching_count = len(gold_df_bench) if 'gold_df_bench' in locals() and gold_df_bench is not None else 50
        else:
            chosen_fa = selected_focus_areas
            if 'gold_df_bench' in locals() and gold_df_bench is not None:
                clean_sel = [fa.strip().lower() for fa in selected_focus_areas]
                matching_count = len(gold_df_bench[gold_df_bench["category"].astype(str).str.strip().str.lower().isin(clean_sel)])
            else:
                matching_count = 50

        q_eval_count = min(int(num_benchmark_questions), matching_count)
        st.info(f"📋 **Selection Summary:** Found **{matching_count}** matching questions. **{q_eval_count}** questions will be evaluated randomly.")
    else:
        chosen_fa = None
        q_eval_count = 50
        st.info("📋 **Fixed Mode Summary:** Evaluating the exact **50 fixed benchmark questions** across all Top 10 clinical focus areas.")

    st.markdown("### 🚀 Execute Live RAG Benchmark Run")
    st.caption("Runs evaluation across the benchmark questions using the active Ollama model and vector database.")

    col_btn, col_info = st.columns([1, 2])
    with col_btn:
        btn_label = "🚀 Run Fixed 50-Question Benchmark" if use_fixed_50 else f"🚀 Run Dynamic {q_eval_count}-Question Benchmark"
        run_bench = st.button(btn_label, type="primary", key="btn_run_benchmark_action")

    if run_bench:
        progress_bar = st.progress(0.0)
        status_box = st.empty()

        def update_progress(current: int, total: int, msg: str):
            progress_bar.progress(current / total)
            status_box.markdown(
                f'<div style="background-color: #e0f2fe; padding: 14px; border-radius: 8px; border-left: 5px solid #0284c7; color: #0369a1; font-size: 1.05rem;">'
                f'⏳ <b>Active Question Processing:</b><br/>{msg}'
                f'</div>',
                unsafe_allow_html=True
            )

        with st.spinner(f"Running {q_eval_count}-question benchmark evaluation..."):
            res_df, summary = run_rag_benchmark_50(
                pipeline=pipeline,
                selected_model=selected_model,
                focus_areas=chosen_fa,
                num_questions=q_eval_count,
                temperature=temperature,
                top_k=top_k,
                progress_callback=update_progress,
                use_fixed_50=use_fixed_50
            )
            st.session_state.benchmark_results_df = res_df
            st.session_state.benchmark_summary = summary
            st.session_state.benchmark_source_file = f"medical_rag_benchmark_{len(res_df)}_results_{re.sub(r'[^a-zA-Z0-9_\\-]', '_', selected_model)}.csv"
            cleanup_after_inference()
            status_box.success(f"✅ {len(res_df)}-Question Benchmark Evaluation Complete!")

    if "benchmark_summary" in st.session_state and "benchmark_results_df" in st.session_state:
        summary = st.session_state.benchmark_summary
        res_df = st.session_state.benchmark_results_df
        rag_sum = summary.get("rag", summary)
        llama_sum = summary.get("llama", {})
        medgemma_sum = summary.get("medgemma", {})
        gemma_sum = summary.get("gemma", {})

        st.markdown("### 🎯 Real-Time Benchmark Evaluation Results")

        # Metrics cards comparing Medical RAG against live Llama 3.1 8B
        m1, m2, m3, m4 = st.columns(4)
        delta_bert = (rag_sum["bertscore_f1_avg"] - llama_sum["bertscore_f1_avg"]) if llama_sum else 0.0
        delta_tf1 = (rag_sum["token_f1_avg"] - llama_sum["token_f1_avg"]) if llama_sum else 0.0
        delta_ssim = (rag_sum["string_similarity_avg"] - llama_sum["string_similarity_avg"]) if llama_sum else 0.0
        delta_rl = (rag_sum["rouge_l_avg"] - llama_sum["rouge_l_avg"]) if llama_sum else 0.0

        with m1:
            st.metric(
                label="RAG BERTScore F1",
                value=f"{rag_sum['bertscore_f1_avg']:.4f}",
                delta=f"{delta_bert:+.4f} vs Live Llama 3.1" if llama_sum else None
            )
        with m2:
            st.metric(
                label="RAG Token F1",
                value=f"{rag_sum['token_f1_avg']:.4f}",
                delta=f"{delta_tf1:+.4f} vs Live Llama 3.1" if llama_sum else None
            )
        with m3:
            st.metric(
                label="RAG String Similarity",
                value=f"{rag_sum['string_similarity_avg']:.4f}",
                delta=f"{delta_ssim:+.4f} vs Live Llama 3.1" if llama_sum else None
            )
        with m4:
            st.metric(
                label="RAG ROUGE-L F1",
                value=f"{rag_sum['rouge_l_avg']:.4f}",
                delta=f"{delta_rl:+.4f} vs Live Llama 3.1" if llama_sum else None
            )

        # 100% Real-Time Comparison Table
        st.markdown("#### 📈 Real-Time Live Model Comparison Table")

        rows = [rag_sum]
        if llama_sum:
            rows.append(llama_sum)
        if medgemma_sum:
            rows.append(medgemma_sum)
        if gemma_sum:
            rows.append(gemma_sum)

        comp_df = pd.DataFrame({
            "Model / System": [r.get("model", "Model") for r in rows],
            "BERTScore F1": [f"{r['bertscore_f1_avg']:.4f}" for r in rows],
            "Token F1": [f"{r['token_f1_avg']:.4f}" for r in rows],
            "String Similarity": [f"{r['string_similarity_avg']:.4f}" for r in rows],
            "ROUGE-L F1": [f"{r['rouge_l_avg']:.4f}" for r in rows],
            "BLEU": [f"{r['bleu_avg']:.4f}" for r in rows],
            "Avg Latency (s)": [f"{r.get('latency_s_avg', 0.0):.2f}s" for r in rows]
        })

        st.dataframe(comp_df, use_container_width=True, hide_index=True)
        st.caption(
            "⚡ **100% Real-Time Live Evaluation:** All metrics above are dynamically evaluated live for the exact questions sampled during this run. No hardcoded paper baselines are used."
        )

        st.markdown("#### 🔍 Detailed Per-Question Results Explorer")
        st.dataframe(
            res_df[["question_id", "category", "question", "bertscore_f1", "token_f1", "string_similarity", "latency_s"]],
            use_container_width=True
        )

        # Allow detailed question inspection
        selected_q_id = st.selectbox("Select Question ID to inspect outputs:", options=res_df["question_id"].tolist())
        if selected_q_id:
            q_row = res_df[res_df["question_id"] == selected_q_id].iloc[0]
            st.markdown(f"**Question ({q_row['question_id']}):** {q_row['question']}")
            
            c_g, c_r = st.columns(2)
            with c_g:
                st.markdown("##### 📋 Gold Reference Answer")
                st.markdown(f'<div class="gold-response">{q_row["gold_answer"]}</div>', unsafe_allow_html=True)
            with c_r:
                st.markdown("##### ✅ RAG Generated Answer")
                st.markdown(f'<div class="rag-response">{q_row["rag_answer"]}</div>', unsafe_allow_html=True)

        # Download CSV option
        csv_bytes = res_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Benchmark Results (CSV)",
            data=csv_bytes,
            file_name=f"medical_rag_benchmark_50_results_{selected_model.replace(':', '_')}.csv",
            mime="text/csv"
        )

# --- TAB 3: Consistency & Reproducibility Evaluator ---
with tab_consistency:
    st.subheader("MSc Lab: Output Reproducibility Evaluation")
    st.write("""
    One of the key safety concerns of deploying LLMs in clinical contexts is output **reproducibility**. 
    Run the same prompt multiple times to analyze output consistency (variance in word counts, response text similarity, etc.) 
    with and without RAG.
    """)
    
    eval_query = st.text_input(
        "Enter query for consistency evaluation:",
        value="What is diabetes?",
        key="eval_query_input"
    )
    
    runs = st.slider("Number of evaluation iterations", min_value=2, max_value=5, value=3)
    
    eval_mode = st.radio(
        "Pipeline Mode to Evaluate",
        options=["Compare both side-by-side", "Plain LLM Only", "RAG Pipeline Only"],
        horizontal=True
    )
    
    if st.button("🔥 Run Reproducibility Test", type="primary"):
        st.write("Executing runs... This may take a few moments.")
        
        plain_runs = []
        rag_runs = []
        
        progress_bar = st.progress(0.0)
        
        for r in range(runs):
            progress_bar.progress((r) / runs)
            
            # Plain Run
            if eval_mode in ["Compare both side-by-side", "Plain LLM Only"]:
                p_ans = pipeline.run_plain_query(eval_query, selected_model, temperature)
                plain_runs.append(p_ans)
                
            # RAG Run
            if eval_mode in ["Compare both side-by-side", "RAG Pipeline Only"]:
                r_ans, _ = pipeline.run_rag_query(eval_query, selected_model, temperature, top_k)
                rag_runs.append(r_ans)
                
        progress_bar.progress(1.0)
        cleanup_after_inference()
        
        # Display side-by-side comparison tables
        if eval_mode in ["Compare both side-by-side", "Plain LLM Only"] and plain_runs:
            st.markdown("### ⚠️ Plain LLM Consistency (No Context)")
            
            # Compute stats
            lengths = [len(ans.split()) for ans in plain_runs]
            len_df = pd.Series(lengths)
            
            col_metric1, col_metric2 = st.columns(2)
            with col_metric1:
                st.metric("Plain Mean Word Count", f"{len_df.mean():.1f} words")
            with col_metric2:
                st.metric("Plain Word Count Std Dev (Variance)", f"{len_df.std():.2f} words")
                
            for idx, ans in enumerate(plain_runs):
                with st.expander(f"Run {idx+1} ({len(ans.split())} words)"):
                    st.write(ans)
                    
        st.markdown(" ")
        
        if eval_mode in ["Compare both side-by-side", "RAG Pipeline Only"] and rag_runs:
            st.markdown("### ✅ RAG Pipeline Consistency")
            
            # Compute stats
            lengths = [len(ans.split()) for ans in rag_runs]
            len_df = pd.Series(lengths)
            
            col_metric1, col_metric2 = st.columns(2)
            with col_metric1:
                st.metric("RAG Mean Word Count", f"{len_df.mean():.1f} words")
            with col_metric2:
                st.metric("RAG Word Count Std Dev (Variance)", f"{len_df.std():.2f} words")
                
            for idx, ans in enumerate(rag_runs):
                with st.expander(f"Run {idx+1} ({len(ans.split())} words)"):
                    st.write(ans)

# --- TAB 4: Knowledge Base Explorer ---
with tab_explorer:
    st.subheader("Browse ChromaDB Embeddings Index")
    st.write("Search the vector store or inspect all text segments loaded into the database.")
    
    if chunk_count == 0:
        st.warning("The database is currently empty. Please index the External KB or Gold CSV in the sidebar.")
    else:
        # Get all records from the collection
        try:
            records = pipeline.vector_store.collection.get()
            
            # Build DataFrame
            ids = records.get('ids', [])
            documents = records.get('documents', [])
            metadatas = records.get('metadatas', [])
            
            df_data = []
            for idx in range(len(ids)):
                meta = metadatas[idx] if idx < len(metadatas) else {}
                source = meta.get('source', 'Unknown')
                page = meta.get('page', 'Unknown')
                text_preview = documents[idx][:150] + "..." if len(documents[idx]) > 150 else documents[idx]
                
                df_data.append({
                    "ID": ids[idx],
                    "Source": source,
                    "Page": page,
                    "Snippet Preview": text_preview,
                    "Full Content": documents[idx]
                })
                
            df = pd.DataFrame(df_data)
            
            search_term = st.text_input("🔍 Search chunks in index:", "")
            if search_term:
                df_filtered = df[df['Full Content'].str.contains(search_term, case=False)]
            else:
                df_filtered = df
                
            st.dataframe(
                df_filtered[["ID", "Source", "Page", "Snippet Preview"]],
                use_container_width=True
            )
            
            # Allow expanding individual rows
            st.markdown("#### Detail Chunk Inspector")
            selected_id = st.selectbox("Select Chunk ID to inspect", options=df_filtered["ID"].tolist())
            if selected_id:
                row = df[df["ID"] == selected_id].iloc[0]
                st.markdown(f"**Source Document:** `{row['Source']}` (Page {row['Page']})")
                st.info(row["Full Content"])
                
        except Exception as e:
            st.error(f"Error loading index explorer: {e}")
