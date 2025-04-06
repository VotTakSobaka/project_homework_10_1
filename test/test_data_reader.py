import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from src.data_reader import read_transactions_from_csv, read_transactions_from_excel

def test_read_transactions_from_csv():
    mock_csv_data = """id,state,date,amount,currency_name,currency_code,from,to,description
                        1,EXECUTED,2023-09-05T11:30:32Z,16210,Sol,PEN,account1,account2,Transaction 1"""

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = read_transactions_from_csv("dummy_path.csv")
        assert len(result) == 1
        assert result[0]['id'] == 1

def test_read_transactions_from_excel():
    mock_excel_data = pd.DataFrame({
        'id': [1],
        'state': ['EXECUTED'],
        'date': ['2023-09-05T11:30:32Z'],
        'amount': [16210],
        'currency_name': ['Sol'],
        'currency_code': ['PEN'],
        'from': ['account1'],
        'to': ['account2'],
        'description': ['Transaction 1']
    })

    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = mock_excel_data
        result = read_transactions_from_excel("dummy_path.xlsx")
        assert len(result) == 1
        assert result[0]['id'] == 1
