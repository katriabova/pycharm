from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """Фильтрует транзакции по коду валюты (например, USD)."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, stop + 1):
        # Форматируем число в 16 цифр с ведущими нулями
        s = f"{number:016d}"
        # Разбиваем на блоки по 4 цифры
        yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:]}"
