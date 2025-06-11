"""Excel or CSV importer placeholder."""

from __future__ import annotations

from typing import Iterable

import pandas as pd


def import_file(path: str) -> Iterable[dict]:
    df = pd.read_excel(path) if path.endswith(".xlsx") else pd.read_csv(path)
    for _, row in df.iterrows():
        yield {
            "name": row.get("name"),
            "description": row.get("description"),
            "price": float(row.get("price", 0)),
            "image_url": row.get("image_url"),
        }
