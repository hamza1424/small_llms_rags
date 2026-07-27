from dotenv import load_dotenv
load_dotenv()
from sentence_transformers import SentenceTransformer
from typing import List, Union

class MedicalEmbedder:
    """
    Handles text embedding generation using SentenceTransformer models.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", device: str = None):
        """
        Initialize the embedding model.
        """
        self.model_name = model_name
        self.device = device
        self.model = None

    def _load_model(self):
        """
        Load the model lazily if it is not already loaded.
        """
        if self.model is None:
            import torch
            device = self.device
            if device is None:
                if torch.cuda.is_available():
                    try:
                        free_gb = torch.cuda.mem_get_info()[0] / (1024 ** 3)
                        if free_gb < 1.5:
                            print(f"CUDA free memory ({free_gb:.2f} GB) is low. Using CPU for embedding model.")
                            device = "cpu"
                        else:
                            device = "cuda"
                    except Exception:
                        device = "cpu"
                else:
                    device = "cpu"

            print(f"Loading embedding model: {self.model_name} on device: {device}...")
            try:
                self.model = SentenceTransformer(self.model_name, device=device)
            except Exception as e:
                if device != "cpu":
                    print(f"Failed to load on {device} ({e}). Falling back to CPU...")
                    device = "cpu"
                    self.model = SentenceTransformer(self.model_name, device="cpu")
                else:
                    raise e
            print(f"Embedding model loaded successfully on {device}.")

    def encode(self, texts: Union[str, List[str]], batch_size: int = 128) -> List:
        """
        Generate embeddings for a single text or a list of texts.
        
        Args:
            texts: A single string or a list of strings to embed.
            batch_size: Batch size for sentence-transformers encoding.
            
        Returns:
            Embeddings as a list of floats (or list of lists for multiple texts).
        """
        self._load_model()
        
        # sentence-transformers encode returns numpy array, we convert to list
        embeddings = self.model.encode(texts, batch_size=batch_size)
        if isinstance(texts, str):
            return embeddings.tolist()
        return [emb.tolist() for emb in embeddings]
