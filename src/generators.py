from typing import Iterable, List, Dict, Any, Generator


def filter_by_currency(transactions: Iterable[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """Фильтрует транзакции по коду валюты (например, 'USD')."""
    for transaction in transactions:
        # Проверяем вложенную структуру: operationAmount -> currency -> code
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """Выдает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирует номера карт XXXX XXXX XXXX XXXX в диапазоне от start до end."""
    for number in range(start, end + 1):
        # 1. Дополняем число нулями слева до 16 знаков
        card_str = f"{number:016d}"
        # 2. Форматируем: берем срезы по 4 цифры и соединяем пробелом
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted_card
