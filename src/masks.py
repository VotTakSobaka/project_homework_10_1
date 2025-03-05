def get_mask_card_number(card_number: str) -> str:
    """
    Замаскировать номер кредитной карты.

    """
    card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        return "Ошибка: номер карты должен содержать только цифры."

    if len(card_number) != 16:
        return "Ошибка: номер карты должен содержать 16 цифр."

    masked_number = card_number[:6] + " " + card_number[6:8] + "** **** " + card_number[-4:]

    return masked_number


input_card_number = input("Введите номер карты: ")
masked_card_number = get_mask_card_number(input_card_number)
print("Замаскированный номер карты:", masked_card_number)


def get_mask_account(account_number: str) -> str:
    """
    Замаскировать номер счета.

    """
    account_number = account_number.replace(" ", "")

    if not account_number.isdigit():
        return "Ошибка: номер счета должен содержать только цифры."

    if len(account_number) < 4:
        return "Ошибка: номер счета должен содержать хотя бы 4 цифры."

    masked_number = "**" + account_number[-4:]

    return masked_number


input_account_number = input("Введите номер счета: ")
masked_account_number = get_mask_account(input_account_number)
print(masked_account_number)
