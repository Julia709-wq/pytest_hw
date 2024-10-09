from datetime import datetime


def filter_by_state(my_list: list, state='EXECUTED') -> list:
    """Сортирует список по состоянию"""
    filtered_list = []
    for i in my_list:
        if i['state'] == state:
            filtered_list.append(i)
    return filtered_list


def parse_date(date: str) -> datetime:
    """Преобразует строку в объект datetime"""
    return datetime.fromisoformat(date)


def sort_by_date(my_list: list, ascending=True) -> list:
    """Сортирует список по дате"""
    sorted_by_date_list = sorted(
        my_list,
        key=lambda item: parse_date(item['date']),
        reverse=not ascending
        )
    return sorted_by_date_list
