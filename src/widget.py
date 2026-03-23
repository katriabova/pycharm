from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа входных данных."""
    if not data:
        return "Некорректные данные"

    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формат DD.MM.YYYY."""
    if not date_str or len(date_str) < 10:
        return "Некорректная дата"

    # Пример входа: 2024-03-11T02:26:18.671407
    date_part = date_str.split("T")[0]  # 2024-03-11
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
