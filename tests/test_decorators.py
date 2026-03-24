import pytest
from src.decorators import log


@log()
def success_func(x: int, y: int) -> int:
    return x + y


@log()
def error_func() -> None:
    raise ValueError("Test error")


def test_log_to_console_success(capsys):
    """Проверка успешного логирования в консоль."""
    success_func(5, 10)
    captured = capsys.readouterr()
    assert "success_func ok" in captured.out


def test_log_to_console_error(capsys):
    """Проверка логирования ошибки в консоль."""
    with pytest.raises(ValueError):
        error_func()
    captured = capsys.readouterr()
    assert "error_func error: ValueError. Inputs: (), {}" in captured.out


def test_log_to_file(tmp_path):
    """Проверка записи лога в файл."""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def file_func():
        return "hello"

    file_func()

    with open(log_file, "r") as f:
        content = f.read()
    assert "file_func ok" in content
