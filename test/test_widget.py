import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card_valid_card():
    assert mask_account_card("Visa 1234567890123456") == "Visa 123456 ** **** 3456"
    assert mask_account_card("MasterCard 1234567890123456") == "MasterCard 123456 ** **** 3456"
    assert mask_account_card("Visa Platinum 1234567890123456") == "Visa Platinum 123456 ** **** 3456"

def test_mask_account_card_valid_account():
    assert mask_account_card("Счет 1234567890") == "Счет **7890"
    assert mask_account_card("Счет 123456789012") == "Счет **9012"

def test_mask_account_card_invalid_card():
    assert mask_account_card("Visa 123456789012345") == "Ошибка: номер карты должен содержать 16 цифр."
    assert mask_account_card("Unknown 1234567890123456") == "Ошибка: неизвестный тип карты или счета."

def test_mask_account_card_invalid_account():
    assert mask_account_card("Счет 123") == "Ошибка: номер счета должен содержать хотя бы 4 цифры."

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-31T23:59:59.999999") == "31.12.2023"

def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("invalid_date")
