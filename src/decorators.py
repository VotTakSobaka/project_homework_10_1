import functools
import logging
from typing import Callable, Optional, Any


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функций.

    Аргументы:
    - filename (Optional[str]): Имя файла для записи логов. Если не указано, логи выводятся в консоль.

    Возвращает:
    - Callable: Декоратор, который оборачивает функцию для логирования.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка для логирования выполнения функции.

            Аргументы:
            - *args: Позиционные аргументы функции.
            - **kwargs: Именованные аргументы функции.

            Возвращает:
            - Any: Результат выполнения функции.
            """
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, 'a') as f:
                        f.write(message + '\n')
                else:
                    print(message)
            return result
        return wrapper
    return decorator
