import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли через API."""
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com{currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return float(response.json().get("result", 0.0))
    return 0.0
