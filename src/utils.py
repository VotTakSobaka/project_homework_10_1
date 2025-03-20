import json
import requests
from typing import Dict, Union
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

def read_json(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_currency(transaction: Dict[str, Union[str, float]]) -> float:
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency not in ['USD', 'EUR']:
        return amount

    params = {
        'symbols': 'RUB',
        'base': currency
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