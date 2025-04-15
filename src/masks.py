import os
import logging

def get_mask_card_number(card_number: str) -> str:
    """Замаскировать номер кредитной карты."""
    card_number = card_number.replace(" ", "")


# Определяем путь к общей папке для логов
logs_directory = "logs"
os.makedirs(logs_directory, exist_ok=True)

def setup_logger(name, log_file, level=logging.DEBUG):
    """Настройка логера для записи в файл."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(level)

    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    return logger

# Настраиваем логирование для модуля masks
masks_logger = setup_logger('masks', os.path.join(logs_directory, 'masks.log'))

def get_mask_card_number(card_number: str) -> str:
    """Замаскировать номер кредитной карты."""
    masks_logger.info('Вызов функции get_mask_card_number.')

    masked_number = f"{card_number[:6]} ** **** {card_number[-4:]}"
    return masked_number

def get_mask_account(account_number: str) -> str:
    """Замаскировать номер счета."""
    account_number = account_number.replace(" ", "")


    card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        masks_logger.error('Ошибка: номер карты должен содержать только цифры.')
        return "Ошибка: номер карты должен содержать только цифры."


    if len(card_number) != 16:
        masks_logger.error('Ошибка: номер карты должен содержать 16 цифр.')
        return "Ошибка: номер карты должен содержать 16 цифр."

    masked_number = f"{card_number[:6]} ** **** {card_number[-4:]}"
    masks_logger.info('Успешное замаскирование номера карты.')
    return masked_number

    masked_number = f"**{account_number[-4:]}"
    return masked_number
