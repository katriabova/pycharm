def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты и возвращает маску XXXX XX** **** XXXX."""
    s = str(card_number)
    return f"{s[:4]} {s[4:6]}** **** {s[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает номер счета и возвращает маску **XXXX."""
    s = str(account_number)
    return f"**{s[-4:]}"