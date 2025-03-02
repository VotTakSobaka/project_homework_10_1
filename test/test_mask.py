import pytest
from src.masks import get_mask_account, get_mask_card_number


# Фикстура для корректных входных данных
@pytest.fixture
def valid_card_numbers():
    return [
        ("1234567812345678", "** ** ** ** 5678"),  # Стандартный номер карты
        ("9876543210123456", "** ** ** ** 3456"),  # Стандартный номер карты
        ("1234567890123456", "** ** ** ** 3456"),  # Стандартный номер карты
        ("1234", "1234"),  # Короткий номер карты
        ("", "Ошибка: некорректный номер карты")  # Пустой ввод
    ]


# тесты для корректных входных данных
@pytest.mark.parametrize("card_number, expected", valid_card_numbers())
def test_valid_card_numbers(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тестирование обработки некорректных входных данных
def test_invalid_card_numbers():
    invalid_numbers = [
        ("abcd1234abcd1234", "Ошибка: некорректный номер карты"),  # Неверный формат
        ("12345678901234567890", "Ошибка: некорректный номер карты"),  # Слишком длинный номер
        ("123456789012", "Ошибка: некорректный номер карты"),  # Слишком короткий номер
        ("123456789012345", "Ошибка: некорректный номер карты"),  # Неверная длина
        (" ", "Ошибка: некорректный номер карты")  # Пробелы
    ]

    for card_number, expected in invalid_numbers:
        assert get_mask_card_number(card_number) == expected

# тесты для корректных номеров карт
@pytest.mark.parametrize("card, expected", valid_card_numbers())
def test_valid_card_number(card, expected):
    assert get_mask_card_number(card) == expected

# тесты для номеров карт с недопустимыми символами
@pytest.mark.parametrize("card, expected", invalid_card_numbers())
def test_invalid_card_number(card, expected):
    assert get_mask_card_number(card) == expected

# Тесты для пустого ввода
def test_empty_input():
    assert get_mask_card_number("") == "Ошибка: некорректный номер карты"  # Пустой ввод


# тесты для корректных номеров счетов
@pytest.mark.parametrize("acc, expected", valid_accounts())
def test_valid_account(acc, expected):
    assert get_mask_account(acc) == expected


# тесты для номеров счетов с пробелами
@pytest.mark.parametrize("acc, expected", accounts_with_spaces())
def test_account_with_spaces(acc, expected):
    assert get_mask_account(acc) == expected


# тесты для номеров счетов с недопустимыми символами
@pytest.mark.parametrize("acc, expected", accounts_with_invalid_chars())
def test_account_with_invalid_chars(acc, expected):
    assert get_mask_account(acc) == expected


# Тесты для номеров счетов с неправильной длиной
@pytest.mark.parametrize("acc", ["123", "12345678901234567890"])
def test_account_with_wrong_length(acc):
    assert get_mask_account(acc) == "Ошибка: некорректный номер счета"


# Тест для пустого ввода
def test_empty_input() -> None:
    assert get_mask_account("") == "Ошибка: некорректный номер счета"  # Пустой ввод


if __name__ == "__masks__":
    pytest.main()