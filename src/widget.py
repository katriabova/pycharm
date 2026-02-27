def mask_account_card(data: str) -> str:
    parts = data.split()
    name = " ".join(parts[:-1])
    number = parts[-1]
    if name.lower().startswith("счет"):
        masked_number = f"**{number[-4:]}"
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    return f"{name} {masked_number}"

def get_date(date_string: str) -> str:
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))
