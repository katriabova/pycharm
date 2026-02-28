from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    parts = data.split()
    name = " ".join(parts[:-1])
    number = parts[-1]

    if name.lower().startswith("счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"

def get_date(date_string: str) -> str:
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"

# тест
if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))