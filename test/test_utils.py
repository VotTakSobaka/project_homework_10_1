import pytest
from unittest.mock import patch, mock_open, Mock
from src.utils import read_json, convert_currency

# Тесты для функции чтения JSON
def test_read_json_success():
    with patch('src.utils.open', new_callable=mock_open, read_data='[{"key": "value"}]'):
        result = read_json('dummy_path')
        assert result == [{"key": "value"}]

def test_read_json_empty_file():
    with patch('src.utils.open', new_callable=mock_open, read_data=''):
        result = read_json('dummy_path')
        assert result == []

def test_read_json_file_not_found():
    with patch('src.utils.open', side_effect=FileNotFoundError()):
        result = read_json('dummy_path')
        assert result == []

def test_read_json_invalid_json():
    with patch('src.utils.open', new_callable=mock_open, read_data='invalid_json'):
        result = read_json('dummy_path')
        assert result == []

# Тесты для функции конвертации валют
@patch('src.utils.requests.get')
def test_convert_currency_usd(mock_get):
    mock_response = Mock()  # Используем Mock из unittest.mock
    mock_response.json.return_value = {'rates': {'RUB': 75.0}}
    mock_get.return_value = mock_response

    transaction = {'amount': 100, 'currency': 'USD'}
    result = convert_currency(transaction)

    assert result == 7500.0

@patch('src.utils.requests.get')
def test_convert_currency_eur(mock_get):
    mock_response = Mock()  # Используем Mock из unittest.mock
    mock_response.json.return_value = {'rates': {'RUB': 90.0}}
    mock_get.return_value = mock_response

    transaction = {'amount': 100, 'currency': 'EUR'}
    result = convert_currency(transaction)

    assert result == 9000.0

def test_convert_currency_rub():
    transaction = {'amount': 100, 'currency': 'RUB'}
    result = convert_currency(transaction)

    assert result == 100
