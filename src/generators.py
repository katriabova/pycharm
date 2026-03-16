from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Генерирует описания каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "No description")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        str_num = f"{number:016d}"
        yield f"{str_num[:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:]}"
