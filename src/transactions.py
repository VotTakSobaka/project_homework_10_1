import re
from collections import Counter

def filter_transactions_by_description(transactions, search_string):
    """
    Фильтрует список транзакций по строке поиска в описании.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка для поиска в описании.
    :return: Список словарей с операциями, у которых в описании есть строка поиска.
    """
    filtered_transactions = []
    pattern = re.compile(search_string, re.IGNORECASE)

    for transaction in transactions:
        if pattern.search(transaction.get('description', '')):
            filtered_transactions.append(transaction)

    return filtered_transactions

def count_transactions_by_category(transactions, categories):
    """
    Подсчитывает количество банковских операций по категориям.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    category_counts = Counter()

    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                category_counts[category] += 1

    return dict(category_counts)
