from typing import Any
from typing import Dict
from typing import List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    try:
        df = pd.read_csv(file_path, delimiter=';')
        return df.to_dict(orient='records')
    except Exception:
        return []


def read_transactions_excel(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из Excel-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except Exception:
        return []
