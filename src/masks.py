def get_mask_card_number(card_number: str) -> str:
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(acc_number: str) -> str:
    return f"**{acc_number[-4:]}"

