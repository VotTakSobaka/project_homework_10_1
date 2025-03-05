def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по указанному коду валюты.

    Args:
        transactions (list): Список словарей транзакций.
        currency_code (str): Код валюты для фильтрации (например, "USD").

    Yields:
        dict: Транзакции, соответствующие указанному коду валюты.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """
    Генерирует описания для каждой транзакции.

    Args:
        transactions (list): Список словарей транзакций.

    Yields:
        str: Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction['description']

def card_number_generator(start, end):
    """
    Генерирует номера карт в указанном диапазоне.

    Args:
        start (int): Начальное число для диапазона номеров карт.
        end (int): Конечное число для диапазона номеров карт.

    Yields:
        str: Номер карты в формате строки "XXXX XXXX XXXX XXXX".
    """
    for number in range(start, end + 1):
        yield f"{number:016}"
