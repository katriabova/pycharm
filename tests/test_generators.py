import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


def test_filter_by_currency(transactions_data):
    """Проверка фильтрации по валюте."""
    usd_transactions = list(filter_by_currency(transactions_data, "USD"))
    assert len(usd_transactions) == 2
    # Проверяем код валюты в первом найденном элементе
    assert usd_transactions[0]["operationAmount"]["currency"]["code"] == "USD"


def test_transaction_descriptions(transactions_data):
    """Проверка генератора описаний."""
    descriptions = transaction_descriptions(transactions_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "start, stop, expected",
    [(1, 1, "0000 0000 0000 0001"), (9999999999999999, 9999999999999999, "9999 9999 9999 9999")],
)
def test_card_number_generator(start, stop, expected):
    """Проверка формата номера карты."""
    gen = card_number_generator(start, stop)
    assert next(gen) == expected
