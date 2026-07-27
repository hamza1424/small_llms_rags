from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["question", "answer"]


def load_gold_csv(path: str | Path) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Gold data CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(
            f"Gold data CSV missing required columns: {missing}. "
            f"Required: {REQUIRED_COLUMNS}"
        )

    out = pd.DataFrame(
        {
            "id": [f"q{i + 1}" for i in range(len(df))],
            "question": df["question"].astype(str),
            "gold_answer": df["answer"].astype(str),
            "category": df["focus_area"].astype(str) if "focus_area" in df.columns else "",
            "source": df["source"].astype(str) if "source" in df.columns else "",
        }
    )
    return out


def load_gold_dataset(folder: str, csv_file: str) -> pd.DataFrame:
    return load_gold_csv(Path(folder) / csv_file)


def filter_by_focus_area(df: pd.DataFrame, focus_area: str) -> pd.DataFrame:
    if not focus_area or focus_area == "All":
        return df
    return df[df["category"].str.lower() == focus_area.lower()].reset_index(drop=True)
