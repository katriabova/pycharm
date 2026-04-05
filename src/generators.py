def filter_by_currency(transactions, currency):
    for transaction in transactions:
        # Безопасно достаем код валюты из вложенного словаря
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        # Если описания нет, можно выдать пустую строку или текст по умолчанию
        yield transaction.get("description", "")


def card_number_generator(start, end):
    for number in range(start, end + 1):
        # 1. Делаем строку из 16 цифр, заполняя пустоты нулями слева
        num_str = f"{number:016d}"

        # 2. Нарезаем строку по 4 символа и склеиваем через пробел
        formatted_card = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"

        yield formatted_card
