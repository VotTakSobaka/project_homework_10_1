def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    Функция принимает список словарей и возвращает новый список,
    содержащий только те словари у которых ключ 'state' соответствует
    указанному значению.

    """
    return [item for item in data if item.get('state') == state]

input_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_result_executed = filter_by_state(input_data)
print(filtered_result_executed)

filtered_result_canceled = filter_by_state(input_data, 'CANCELED')
print(filtered_result_canceled)