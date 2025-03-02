import pytest
from src.widget import mask_account_card,get_date

# Фикстура для корректных входных данных
@pytest.fixture
def valid_inputs():
    return [
        ("Visa 1234567812345678", "Visa 123456** **** 5678"),  # Стандартный номер карты Visa
        ("MasterCard 9876543210123456", "MasterCard 987654** **** 3456"),  # Стандартный номер карты MasterCard
        ("Maestro 1234567890123456", "Maestro 123456** **** 3456"),  # Стандартный номер карты Maestro
        ("Счет 123456789012", "Счет **9012"),  # Номер счета
        ("Счет 1234", "Счет **34"),  # Короткий номер счета
    ]

# Фикстура для некорректных входных данных
@pytest.fixture
def invalid_inputs():
    return [
        ("Visa 1234abcd", "Ошибка: номер карты должен содержать 16 цифр."),  # Неверный номер карты
        ("Счет 123", "Ошибка: номер счета должен содержать хотя бы 4 цифры."),  # Короткий номер счета
        ("UnknownType 1234567890123456", "Ошибка: неизвестный тип карты или счета."),  # Неизвестный тип
        ("Visa 12345678901234567890", "Ошибка: номер карты должен содержать 16 цифр."),  # Слишком длинный номер карты
        ("", "Ошибка: неизвестный тип карты или счета."),  # Пустой ввод
    ]

# тесты для корректных входных данных
@pytest.mark.parametrize("info, expected", valid_inputs())
def test_valid_inputs(info, expected):
    assert mask_account_card(info) == expected

# тесты для некорректных входных данных
@pytest.mark.parametrize("info, expected", invalid_inputs())
def test_invalid_inputs(info, expected):
    assert mask_account_card(info) == expected


# Фикстура для корректных входных данных
@pytest.fixture
def valid_dates():
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Стандартный формат
        ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Конец года
        ("2000-01-01T00:00:00.000000", "01.01.2000"),  # Начало века
        ("1999-07-04T12:00:00.000000", "04.07.1999"),  # Дата в прошлом
    ]


# тесты для корректных входных данных
@pytest.mark.parametrize("date_str, expected", valid_dates())
def test_valid_dates(date_str, expected):
    assert get_date(date_str) == expected


# Тестирование обработки некорректных входных данных
def test_invalid_dates():
    invalid_dates = [
        ("abcd-ef-ghTHH:MM:SS", "Ошибка: некорректный формат даты"),  # Неверный формат
        ("2024-02-30T00:00:00.000000", "Ошибка: некорректная дата"),  # Неверная дата
        ("2024-03-11", "Ошибка: некорректный формат даты"),  # Отсутствует время
        ("", "Ошибка: некорректный формат даты"),  # Пустая строка
    ]

    for date_str, expected in invalid_dates:
        with pytest.raises(ValueError) as excinfo:
            get_date(date_str)
        assert str(excinfo.value) == expected


if __name__ == "__widget__":
    pytest.main()