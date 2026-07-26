import csv
from typing import Dict
from typing import List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    Возвращает список словарей.
    """
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        return []
    return transactions

def read_transactions_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    Возвращает список словарей.
    """
    try:
        df = pd.read_excel(file_path)
        # Превращаем DataFrame в список словарей
        return df.to_dict(orient='records')
    except Exception:
        return []
