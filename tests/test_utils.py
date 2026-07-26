from unittest.mock import mock_open
from unittest.mock import patch

import pandas as pd
import pytest

from src.utils import read_transactions_csv
from src.utils import read_transactions_excel


@patch("builtins.open", new_callable=mock_open, read_data="id;amount\n1;100")
def test_read_transactions_csv(mock_file):
    result = read_transactions_csv("fake.csv")
    assert result == [{"id": "1", "amount": "100"}]
    mock_file.assert_called_once_with("fake.csv", mode='r', encoding='utf-8')

@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read):
    # Настраиваем мок так, чтобы он возвращал DataFrame
    mock_read.return_value = pd.DataFrame([{"id": 1, "amount": 100}])
    result = read_transactions_excel("fake.xlsx")
    assert result == [{"id": 1, "amount": 100}]
