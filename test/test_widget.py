import pytest
from src.widget import mask_account_card,get_date

@pytest.mark.parametrize(
    "info, expected",
    [
        ("visa 1234567890123456", "visa 123456 78** **** 3456"),
        ("mastercard 1234567890123456", "mastercard 123456 78** **** 3456"),
        ("visa platinum 1234567890123456", "visa platinum 123456 78** **** 3456"),
        ("счет 1234567890", "счет **7890"),
        ("счет 1234", "счет **1234"),
        ("visa 123456789012345", "Ошибка: номер карты должен содержать 16 цифр."),
        ("счет 123", "Ошибка: номер счета должен содержать хотя бы 4 цифры."),
        ("unknown 1234567890123456", "Ошибка: неизвестный тип карты или счета."),
        ("visa 1234abcd56789012", "Ошибка: номер карты должен содержать 16 цифр."),
        ("счет 1234abcd", "Ошибка: номер счета должен содержать хотя бы 4 цифры."),
    ]
)
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected

def test_mask_account_card_empty_input():
    assert mask_account_card("") == "Ошибка: неизвестный тип карты или счета."

def test_mask_account_card_no_number():
    assert mask_account_card("visa") == "Ошибка: номер карты должен содержать 16 цифр."


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2024-02-29T12:34:56.789012", "29.02.2024"),
        ("2024-03-11", "11.03.2024"),  # Без времени
        ("2024-03-11T", "11.03.2024"),  # Только дата и T
    ]
)
def test_get_date_valid(date_str, expected):
    assert get_date(date_str) == expected

def test_get_date_invalid_format():
    assert get_date("11.03.2024 02:26:18") == "11.03.2024"

def test_get_date_empty_string():
    assert get_date("") == "01.01.0001"

def test_get_date_no_date():
    assert get_date("T02:26:18.671407") == "01.01.0001"


if __name__ == "__widget__":
    pytest.main()