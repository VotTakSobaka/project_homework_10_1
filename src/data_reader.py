import pandas as pd

def read_transactions_from_csv(file_path):
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def read_transactions_from_excel(file_path):
    """
    Считывает финансовые операции из Excel-файла.

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
