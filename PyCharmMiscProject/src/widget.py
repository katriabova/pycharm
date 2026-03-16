from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    parts = data.split()
    name = " ".join(parts[:-1])
    number = parts[-1]

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


