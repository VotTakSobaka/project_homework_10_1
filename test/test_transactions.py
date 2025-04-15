import pytest
from transactions import filter_transactions_by_description, count_transactions_by_category

def test_filter_transactions_by_description():
    transactions = [
        {"description": "Открытие вклада", "status": "EXECUTED", "date": "2019-12-08", "amount": 40542, "currency": "руб."},
        {"description": "Перевод с карты на карту", "status": "EXECUTED", "date": "2019-11-12", "amount": 130, "currency": "USD"},
        {"description": "Перевод организации", "status": "CANCELED", "date": "2018-07-18", "amount": 8390, "currency": "руб."},
        {"description": "Перевод со счета на счет", "status": "PENDING", "date": "2018-06-03", "amount": 8200, "currency": "EUR"}
    ]
    assert len(filter_transactions_by_description(transactions, "Перевод")) == 3
    assert len(filter_transactions_by_description(transactions, "вклад")) == 1
    assert len(filter_transactions_by_description(transactions, "несуществующий")) == 0

def test_count_transactions_by_category():
    transactions = [
        {"description": "Открытие вклада", "status": "EXECUTED", "date": "2019-12-08", "amount": 40542, "currency": "руб."},
        {"description": "Перевод с карты на карту", "status": "EXECUTED", "date": "2019-11-12", "amount": 130, "currency": "USD"},
        {"description": "Перевод организации", "status": "CANCELED", "date": "2018-07-18", "amount": 8390, "currency": "руб."},
        {"description": "Перевод со счета на счет", "status": "PENDING", "date": "2018-06-03", "amount": 8200, "currency": "EUR"}
    ]
    categories = ["Перевод", "вклад"]
    result = count_transactions_by_category(transactions, categories)
    assert result == {"Перевод": 3, "вклад": 1}

if __name__ == "__main__":
    pytest.main()
