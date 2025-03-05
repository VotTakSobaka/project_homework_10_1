def mask_account_card(info: str) -> str:
    """Замаскировать номер карты или счета."""
    parts = info.split()
    card_type = " ".join(parts[:-1])
    number = parts[-1]

    if card_type.lower() in ["visa", "mastercard", "maestro", "visa platinum", "visa classic", "visa gold"]:
        if len(number) == 16:
            masked_number = f"{number[:6]} ** **** {number[-4:]}"
            return f"{card_type} {masked_number}"
        else:
            return "Ошибка: номер карты должен содержать 16 цифр."
    elif card_type.lower() == "счет":
        if len(number) >= 4:
            masked_number = f"**{number[-4:]}"
            return f"{card_type} {masked_number}"
        else:
            return "Ошибка: номер счета должен содержать хотя бы 4 цифры."
    else:
        return "Ошибка: неизвестный тип карты или счета."

def get_date(date_str: str) -> str:
    """Преобразовать строку с датой в формат "ДД.ММ.ГГГГ"."""
    try:
        date_part = date_str.split("T")[0]
        year, month, day = date_part.split("-")
        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    except ValueError:
        raise ValueError("Неверный формат даты")
