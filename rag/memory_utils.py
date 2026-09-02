"""Lightweight cleanup helpers: __pycache__ removal + GPU VRAM release."""

from __future__ import annotations

import gc
import shutil
from pathlib import Path


def clear_pycache(root: str | Path | None = None) -> int:
    """
    Delete __pycache__ directories under project root.
    Returns number of directories removed.
    """
    base = Path(root) if root else Path(__file__).resolve().parent.parent
    removed = 0
    for cache_dir in base.rglob("__pycache__"):
        # Skip virtualenv caches
        if ".venv" in cache_dir.parts or "site-packages" in cache_dir.parts:
            continue
        try:
            shutil.rmtree(cache_dir, ignore_errors=True)
            removed += 1
        except Exception:
            pass
    return removed


def release_gpu_memory() -> None:
    """Force Python GC and free unused CUDA / MPS cache if available."""
    gc.collect()
    try:
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        if hasattr(torch, "mps") and hasattr(torch.mps, "empty_cache"):
            try:
                torch.mps.empty_cache()
            except Exception:
                pass
    except Exception:
        pass


def cleanup_after_inference(clear_cache_dirs: bool = True) -> None:
    """Run after heavy inference / BERTScore to free GPU memory (and optionally pycache)."""
    if clear_cache_dirs:
        clear_pycache()
    release_gpu_memory()
