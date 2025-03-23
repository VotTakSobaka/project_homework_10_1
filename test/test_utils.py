import pytest
import json
from unittest.mock import patch, mock_open, Mock
from src.utils import read_json, convert_currency

# Тесты для функции чтения JSON
def test_read_json_success():
    json_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    with patch('builtins.open', new_callable=mock_open, read_data=json.dumps(json_data)):
        result = read_json('dummy_path')
        assert result == json_data

def test_read_json_empty_file():
    with patch('builtins.open', new_callable=mock_open, read_data=''):
        result = read_json('dummy_path')
        assert result == []

def test_read_json_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError()):
        result = read_json('dummy_path')
        assert result == []

def test_read_json_invalid_json():
    with patch('builtins.open', new_callable=mock_open, read_data='invalid_json'):
        result = read_json('dummy_path')
        assert result == []

# Тесты для функции конвертации валют
@patch('src.utils.requests.get')
def test_convert_currency_usd(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.0}}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "USD"
            }
        }
    }
    result = convert_currency(transaction)
    assert result == 7500.0

@patch('src.utils.requests.get')
def test_convert_currency_eur(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 90.0}}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "EUR"
            }
        }
    }
    result = convert_currency(transaction)
    assert result == 9000.0

def test_convert_currency_rub():
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = convert_currency(transaction)
    assert result == 100.0
