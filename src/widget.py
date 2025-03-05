def mask_account_card(info: str) -> str:
    """
    Замаскировать номер карты или счета.

    Функция принимает строку, содержащую тип карты или счет и номер,
    и возвращает замаскированный номер в зависимости от типа.

    """
    # Разделяем строку на тип и номер
    parts = info.split()
    card_type = " ".join(parts[:-1])  # Все части, кроме последней, составляют тип
    number = parts[-1]  # Последняя часть - это номер

    # Проверяем, является ли номер картой или счетом
    if card_type.lower() in ["visa", "mastercard", "maestro", "visa platinum", "visa classic", "visa gold"]:
        # Маскировка номера карты
        if len(number) == 16:
            masked_number = number[:6] + " " + number[6:8] + "** **** " + number[-4:]
            return f"{card_type} {masked_number}"
        else:
            return "Ошибка: номер карты должен содержать 16 цифр."
    elif card_type.lower() == "счет":
        # Маскировка номера счета
        if len(number) >= 4:
            masked_number = "**" + number[-4:]
            return f"{card_type} {masked_number}"
        else:
            return "Ошибка: номер счета должен содержать хотя бы 4 цифры."
    else:
        return "Ошибка: неизвестный тип карты или счета."


input_info = input("Введите тип и номер карты или счета: ")
masked_result = mask_account_card(input_info)
print(masked_result)


def get_date(date_str: str) -> str:
    """
    Преобразовать строку с датой в формат "ДД.ММ.ГГГГ".

    Функция принимает строку, содержащую дату в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ".

    """
    # Разделяем строку на дату и время
    date_part = date_str.split("T")[0]
    # Разделяем дату на год, месяц и день
    year, month, day = date_part.split("-")
    # Формируем строку в нужном формате
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


input_date = input("Введите дату в формате 'YYYY-MM-DDTHH:MM:SS.ssssss': ")
formatted_result = get_date(input_date)
print("Дата в формате 'ДД.ММ.ГГГГ':", formatted_result)