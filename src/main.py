from transactions import filter_transactions_by_description

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта меню: ")

    if choice == '1':
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт меню 1, 2 или 3.")
        return

    # Пример данных о транзакциях
    transactions = [
        {"description": "Открытие вклада", "status": "EXECUTED", "date": "2019-12-08", "amount": 40542, "currency": "руб."},
        {"description": "Перевод с карты на карту", "status": "EXECUTED", "date": "2019-11-12", "amount": 130, "currency": "USD"},
        {"description": "Перевод организации", "status": "CANCELED", "date": "2018-07-18", "amount": 8390, "currency": "руб."},
        {"description": "Перевод со счета на счет", "status": "PENDING", "date": "2018-06-03", "amount": 8200, "currency": "EUR"}
    ]

    status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции \"{status}\" недоступен.")
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()

    filtered_transactions = [t for t in transactions if t["status"] == status]
    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions = sorted(filtered_transactions, key=lambda x: x["date"], reverse=(sort_order == "по убыванию"))

    ruble_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if ruble_choice == "да":
        filtered_transactions = [t for t in filtered_transactions if t["currency"].lower() == "руб."]

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == "да":
        search_string = input("Введите слово для поиска в описании: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        print(f"{transaction['date']} {transaction['description']}")
        print(f"Сумма: {transaction['amount']} {transaction['currency']}")
        print()

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == "__main__":
    main()
