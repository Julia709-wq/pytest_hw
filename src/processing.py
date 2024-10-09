from datetime import datetime


def filter_by_state(my_list: list, state='EXECUTED') -> list:
    """Сортирует список по состоянию"""
    filtered_list = []
    for i in my_list:
        if i['state'] == state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(my_list: list, ascending=True) -> list:
    """Сортирует список по дате"""

    def parse_date(date):
        """Преобразует строку в объект datetime"""
        return datetime.fromisoformat(item['date'])


    for item in my_list:
        sorted_by_date_list = sorted(my_list, key=parse_date, reverse=ascending)

    return sorted_by_date_list