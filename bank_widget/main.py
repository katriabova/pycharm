from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    # Проверка маскировки карты
    card = 7000792289606361
    print(f"Карта: {get_mask_card_number(card)}")

    # Проверка маскировки счета
    account = 73654108430135874305
    print(f"Счет:  {get_mask_account(account)}")
