import json
import os
from typing import Any


def get_financial_data(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список транзакций."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []
