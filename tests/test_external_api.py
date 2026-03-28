from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_to_rub_usd(mock_get):
    """Тест конвертации из USD в RUB через Mock."""
    # Настраиваем «фейковый» ответ сервера
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }

    assert convert_to_rub(transaction) == 7500.0
    # Проверяем, что запрос был вызван именно с этими параметрами
    mock_get.assert_called_once()


def test_convert_to_rub_already_rub():
    """Тест, что если валюта RUB, API не вызывается."""
    transaction = {
        "operationAmount": {"amount": "500", "currency": {"code": "RUB"}}
    }
    with patch("requests.get") as mock_get:
        assert convert_to_rub(transaction) == 500.0
        mock_get.assert_not_called()
