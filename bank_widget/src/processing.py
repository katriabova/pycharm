from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param data: Список словарей для фильтрации.
    :param state: Статус, по которому фильтруем (по умолчанию 'EXECUTED').
    :return: Новый список словарей с подходящим статусом.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате (ключ 'date').
        :param data: Список словарей с данными о транзакциях.
        :param reverse: Флаг для сортировки (True — по убыванию, False — по возрастанию).
        :return: Отсортированный список словарей.
        """
    return sorted(data, key=lambda x: x.get('date', ''), reverse=reverse)
