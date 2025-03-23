import json
import requests
from typing import List, Dict, Any, Union
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.apilayer.com/exchangerates_data/latest"

def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def convert_currency(transaction: Dict[str, Union[str, Dict]]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.
    """
    amount_data = transaction.get('operationAmount', {})
    amount = float(amount_data.get('amount', 0))
    currency_data = amount_data.get('currency', {})
    currency_code = currency_data.get('code', 'RUB')

    if currency_code not in ['USD', 'EUR']:
        return amount

    params = {
        'symbols': 'RUB',
        'base': currency_code
    }

    headers = {
        'apikey': API_KEY
    }

    response = requests.get(API_URL, headers=headers, params=params)
    data = response.json()

    if 'rates' in data and 'RUB' in data['rates']:
        rub_rate = data['rates']['RUB']
        return amount * rub_rate
    else:
        return amount
