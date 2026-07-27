from dotenv import load_dotenv
load_dotenv()
import os
import sys
from rag.rag_pipeline import MedicalRAGPipeline

def run_tests():
    print("=== STARTING RAG PIPELINE UNIT TESTS ===")
    
    # 1. Initialize Pipeline
    print("\n--- Step 1: Initializing RAG Pipeline ---")
    try:
        pipeline = MedicalRAGPipeline(config_path="configs/rag_config.yaml")
        print("Success: Pipeline initialized.")
    except Exception as e:
        print(f"FAIL: Pipeline initialization failed: {e}")
        sys.exit(1)

    # 2. Test Document Loading and Ingestion
    print("\n--- Step 2: Testing Document Ingestion ---")
    try:
        # Check if dataset exists
        dataset_folder = pipeline.config['knowledge_base']['folder']
        if not os.path.exists(dataset_folder):
            print(f"FAIL: Dataset folder '{dataset_folder}' does not exist.")
            sys.exit(1)
            
        print("Ingesting files...")
        added_count = pipeline.ingest_documents()
        print(f"Success: Ingested {added_count} chunks.")
        assert added_count > 0, "Ingested chunk count must be greater than 0."
    except Exception as e:
        print(f"FAIL: Document ingestion failed: {e}")
        sys.exit(1)

    # 3. Test Retrieval
    print("\n--- Step 3: Testing Retrieval ---")
    try:
        query = "What is diabetes?"
        print(f"Retrieving context for query: '{query}'")
        retrieved = pipeline.retriever.retrieve_context(query, top_k=2)
        print(f"Success: Retrieved {len(retrieved)} chunks.")
        assert len(retrieved) > 0, "Should retrieve at least one chunk."
        
        for i, chunk in enumerate(retrieved):
            print(f"  Chunk {i+1} (source: {chunk['metadata'].get('source')}, distance: {chunk['distance']:.4f}):")
            print(f"    Text snippet: {chunk['text'][:150]}...")
    except Exception as e:
        print(f"FAIL: Context retrieval failed: {e}")
        sys.exit(1)

    # 4. Test Ollama connection & Generation
    print("\n--- Step 4: Testing Ollama connection ---")
    # Let's see what model we can use to test
    available_models = pipeline.config['ollama']['models']
    test_model = available_models[0] # Try the first model
    
    print(f"Testing generation using model '{test_model}'...")
    try:
        # Test plain query
        plain_response = pipeline.run_plain_query("What is diabetes?", model=test_model)
        print("Plain Response:")
        print(f"  {plain_response}")
        assert len(plain_response) > 0, "Response should not be empty."
        
        # Test RAG query
        rag_response, chunks = pipeline.run_rag_query("What is diabetes?", model=test_model, top_k=2)
        print("\nRAG Response:")
        print(f"  {rag_response}")
        assert len(rag_response) > 0, "Response should not be empty."
        assert len(chunks) > 0, "Chunks list should not be empty."
        
        print("\nSuccess: Ollama query and response parsing completed successfully.")
    except Exception as e:
        print(f"FAIL: Ollama integration test failed: {e}")
        sys.exit(1)

    print("\n=== ALL TESTS PASSED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_tests()
