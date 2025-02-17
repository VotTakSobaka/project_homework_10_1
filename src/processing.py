def filter_by_state(data, state="EXECUTED"):
    """
    Фильтрует список словарей по значению ключа 'state'.

    Функция принимает список словарей и возвращает новый список,
    содержащий только те словари у которых ключ 'state' соответствует
    указанному значению.

    """
    return [item for item in data if item.get("state") == state]


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filtered_result_executed = filter_by_state(input_data)
print(filtered_result_executed)

filtered_result_canceled = filter_by_state(input_data, "CANCELED")
print(filtered_result_canceled)


def sort_by_date(data, reverse: bool = True) -> list:
    """
    Сортирует список словарей по значению ключа 'date'.

    Функция принимает список словарей и возвращает новый список,
    отсортированный по дате. Порядок сортировки можно задать с помощью
    параметра reverse. Если reverse равно True, сортировка будет
    производиться в порядке убывания, если False — в порядке возрастания.

    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


input_data = [{"id": 1, "date": "2023-01-01"}, {"id": 2, "date": "2022-12-31"}, {"id": 3, "date": "2023-01-02"}]

# Сортировка по дате в порядке убывания
sorted_result_desc = sort_by_date(input_data)
print("Отсортированный список (убывание):", sorted_result_desc)


sorted_result_asc = sort_by_date(input_data, reverse=False)
print(sorted_result_asc)
