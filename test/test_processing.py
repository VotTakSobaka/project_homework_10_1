import pytest
from src.processing import filter_by_state, sort_by_date


# Фикстура для корректных входных данных
@pytest.fixture
def input_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

# Параметризованные тесты для различных значений статуса
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]),
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]),
    ("PENDING", []),  # Нет словарей с таким статусом
    ("", []),  # Пустой статус
])
def test_filter_by_state(input_data, state, expected):
    assert filter_by_state(input_data, state) == expected


# Фикстура для корректных входных данных
@pytest.fixture
def input_data():
    return [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2022-12-31"},
        {"id": 3, "date": "2023-01-02"},
        {"id": 4, "date": "2023-01-01"},  # Дубликат даты
    ]

# Тестирование сортировки по убыванию
def test_sort_by_date_desc(input_data):
    expected = [
        {"id": 3, "date": "2023-01-02"},
        {"id": 1, "date": "2023-01-01"},
        {"id": 4, "date": "2023-01-01"},
        {"id": 2, "date": "2022-12-31"},
    ]
    assert sort_by_date(input_data) == expected

# Тестирование сортировки по возрастанию
def test_sort_by_date_asc(input_data):
    expected = [
        {"id": 2, "date": "2022-12-31"},
        {"id": 1, "date": "2023-01-01"},
        {"id": 4, "date": "2023-01-01"},
        {"id": 3, "date": "2023-01-02"},
    ]
    assert sort_by_date(input_data, reverse=False) == expected

# Тестирование некорректного формата даты
def test_sort_by_date_invalid_date():
    data = [
        {"id": 1, "date": "invalid-date"},
        {"id": 2, "date": "2022-12-31"},
    ]
    with pytest.raises(KeyError):  # Ожидаем ошибку, если 'date' отсутствует
        sort_by_date(data)

# Тестирование пустого списка
def test_sort_by_date_empty():
    assert sort_by_date([]) == []

# Тестирование списка с некорректными датами
def test_sort_by_date_mixed_dates():
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": None},  # None вместо даты
        {"id": 3, "date": "2022-12-31"},
    ]
    with pytest.raises(TypeError):  # Ожидаем ошибку при попытке сортировки
        sort_by_date(data)


if __name__ == "__processing__":
        pytest.main()