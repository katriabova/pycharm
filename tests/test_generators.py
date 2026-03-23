import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions_data():
    return [
        {
            "id": 938505981,
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
        },
        {
            "id": 441945886,
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
        },
        {
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
        },
    ]


def test_filter_by_currency(transactions_data):
    """Тест фильтрации по валюте USD."""
    usd_gen = filter_by_currency(transactions_data, "USD")
    result = list(usd_gen)
    assert len(result) == 2
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"
    assert result[1]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_empty():
    """Тест фильтрации пустого списка."""
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions_data):
    """Тест получения описаний транзакций."""
    descriptions = transaction_descriptions(transactions_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_missing_key():
    """Тест генератора описаний, если ключа 'description' нет."""
    data = [{"id": 1}]
    descriptions = transaction_descriptions(data)
    assert next(descriptions) == "Описание отсутствует"


def test_card_number_generator():
    """Тест генератора номеров карт."""
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"

    with pytest.raises(StopIteration):
        next(gen)


def test_card_number_generator_range():
    """Тест генератора на большом числе."""
    gen = card_number_generator(9999999999999998, 9999999999999999)
    assert next(gen) == "9999 9999 9999 9998"
    assert next(gen) == "9999 9999 9999 9999"
