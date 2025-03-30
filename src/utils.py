import os
import logging

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

# Настраиваем логирование для модуля utils
utils_logger = setup_logger('utils', os.path.join(logs_directory, 'utils.log'))

def get_mask_account(account_number: str) -> str:
    """Замаскировать номер счета."""
    utils_logger.info('Вызов функции get_mask_account.')

    account_number = account_number.replace(" ", "")

    if not account_number.isdigit():
        utils_logger.error('Ошибка: номер счета должен содержать только цифры.')
        return "Ошибка: номер счета должен содержать только цифры."

    if len(account_number) < 4:
        utils_logger.error('Ошибка: номер счета должен содержать хотя бы 4 цифры.')
        return "Ошибка: номер счета должен содержать хотя бы 4 цифры."

    masked_number = f"**{account_number[-4:]}"
    utils_logger.info('Успешное замаскирование номера счета.')
    return masked_number
