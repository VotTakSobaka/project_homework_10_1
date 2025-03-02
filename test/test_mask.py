import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def valid_card_number():
    return "1234 5678 9012 3456"

@pytest.fixture
def invalid_card_number_non_digit():
    return "1234 5678 9012 abcd"

@pytest.fixture
def invalid_card_number_length():
    return "1234 5678 9012 345"

@pytest.fixture
def empty_card_number():
    return ""

def test_mask_valid_card_number(valid_card_number):
    assert get_mask_card_number(valid_card_number) == "123456 78** **** 3456"

def test_non_digit_card_number(invalid_card_number_non_digit):
    assert get_mask_card_number(invalid_card_number_non_digit) == (
        "Ошибка: номер карты должен содержать только цифры.")

def test_invalid_length_card_number(invalid_card_number_length):
    assert get_mask_card_number(invalid_card_number_length) == (
        "Ошибка: номер карты должен содержать 16 цифр.")

def test_empty_card_number(empty_card_number):
    assert get_mask_card_number(empty_card_number) == (
        "Ошибка: номер карты должен содержать только цифры.")

@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "123456 78** **** 3456"),
        ("1234 5678 9012 3456", "123456 78** **** 3456"),
        ("1234-5678-9012-3456", "Ошибка: номер карты должен содержать только цифры."),
        ("1234a567890123456", "Ошибка: номер карты должен содержать только цифры."),
        ("123456789012345", "Ошибка: номер карты должен содержать 16 цифр."),
        ("12345678901234567", "Ошибка: номер карты должен содержать 16 цифр."),
    ]
)
def test_various_formats(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.fixture
def valid_account_number():
    return "1234567890"

@pytest.fixture
def invalid_account_number_non_digit():
    return "1234abcd"

@pytest.fixture
def short_account_number():
    return "123"

@pytest.fixture
def empty_account_number():
    return ""

def test_mask_valid_account_number(valid_account_number):
    assert get_mask_account(valid_account_number) == "**7890"

def test_non_digit_account_number(invalid_account_number_non_digit):
    assert get_mask_account(invalid_account_number_non_digit) == (
        "Ошибка: номер счета должен содержать только цифры.")

def test_short_account_number(short_account_number):
    assert get_mask_account(short_account_number) == (
        "Ошибка: номер счета должен содержать хотя бы 4 цифры.")

def test_empty_account_number(empty_account_number):
    assert get_mask_account(empty_account_number) == (
        "Ошибка: номер счета должен содержать только цифры.")

@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890", "**7890"),
        ("1234 5678 90", "**7890"),
        ("1234-5678-90", "Ошибка: номер счета должен содержать только цифры."),
        ("1234abcd", "Ошибка: номер счета должен содержать только цифры."),
        ("123", "Ошибка: номер счета должен содержать хотя бы 4 цифры."),
        ("", "Ошибка: номер счета должен содержать только цифры."),
    ]
)
def test_various_formats(account_number, expected):
    assert get_mask_account(account_number) == expected


if __name__ == "__masks__":
    pytest.main()