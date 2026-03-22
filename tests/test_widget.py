import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize("input_str, expected", [
    ("Visa Gold 7000792289606361", "Visa Gold 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837493215786", "Maestro 1596 83** **** 5786"),
    ("", "Некорректные данные")  # Пример обработки ошибок
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-12-31T23:59:59.999999", "31.12.2018"),
    ("", "Некорректная дата")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
