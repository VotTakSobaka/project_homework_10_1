import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234 5678 9012 3456") == "123456 ** **** 3456"
    assert get_mask_card_number("1234567890123456") == "123456 ** **** 3456"

def test_get_mask_card_number_invalid_non_digit():
    assert get_mask_card_number("1234 5678 90ab 3456") == "Ошибка: номер карты должен содержать только цифры."

def test_get_mask_card_number_invalid_length():
    assert get_mask_card_number("123456789012345") == "Ошибка: номер карты должен содержать 16 цифр."
    assert get_mask_card_number("12345678901234567") == "Ошибка: номер карты должен содержать 16 цифр."

def test_get_mask_card_number_empty_input():
    assert get_mask_card_number("") == "Ошибка: номер карты должен содержать только цифры."

def test_get_mask_account_valid():
    assert get_mask_account("1234567890") == "**7890"
    assert get_mask_account("123456789012") == "**9012"

def test_get_mask_account_invalid_non_digit():
    assert get_mask_account("1234ab7890") == "Ошибка: номер счета должен содержать только цифры."

def test_get_mask_account_invalid_length():
    assert get_mask_account("123") == "Ошибка: номер счета должен содержать хотя бы 4 цифры."

def test_get_mask_account_with_spaces():
    assert get_mask_account("1234 5678 90") == "**7890"
