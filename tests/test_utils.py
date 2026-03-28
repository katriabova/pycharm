from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from src.utils import get_financial_data


def test_get_financial_data_success():
    """Тест успешного чтения корректного JSON-списка."""
    mock_data = '[{"id": 1, "state": "EXECUTED"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_financial_data("data/operations.json")
        assert result == [{"id": 1, "state": "EXECUTED"}]


def test_get_financial_data_not_found():
    """Тест возврата пустого списка, если файл не найден."""
    with patch("os.path.exists", return_value=False):
        assert get_financial_data("invalid.json") == []


def test_get_financial_data_invalid_json():
    """Тест возврата пустого списка при битом JSON."""
    with patch("builtins.open", mock_open(read_data='{ "not_a_list": 1 }')):
        # Если функция проверяет isinstance(data, list)
        assert get_financial_data("data/operations.json") == []

