import logging
import os
from typing import Any
from typing import Dict

# Настройка пути к логам
log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'utils.log')
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_amount(transaction: Dict[str, Any]) -> float:
    """Получает сумму транзакции."""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        logger.info(f"Сумма транзакции успешно получена: {amount}")
        return amount
    except (KeyError, ValueError, TypeError) as e:
        logger.error(f"Ошибка при получении суммы транзакции: {e}")
        return 0.0
