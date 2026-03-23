import pytest


@pytest.fixture
def transactions_data():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00.000",
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-02-01T12:00:00.000",
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-03-01T12:00:00.000",
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Оплата услуг",
        },
    ]
