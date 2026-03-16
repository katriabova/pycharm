import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("NON_EXISTENT", 0)
])
def test_filter_by_state(transactions_data, state, expected_count):
    """Параметризованный тест фильтрации по статусу."""
    result = filter_by_state(transactions_data, state)
    assert len(result) == expected_count

def test_sort_by_date(transactions_data):
    """Тест сортировки по дате (по убыванию)."""
    result = sort_by_date(transactions_data)
    assert result[0]["id"] == 3  # Самая поздняя дата должна быть первой