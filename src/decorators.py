import functools
from datetime import datetime
from typing import Any
from typing import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который логирует вызов функции, её результат или ошибку.
    Логирует в файл (если задан filename) или в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_message = f"{now} {func.__name__} ok"
                write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = f"{now} {func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}"
                write_log(log_message, filename)
                raise e

        return wrapper

    return decorator


def write_log(message: str, filename: Optional[str]) -> None:
    """Вспомогательная функция для записи лога в файл или вывода в консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
