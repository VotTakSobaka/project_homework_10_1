import pytest
from src.decorators import log

# Очистка файла логов перед запуском тестов
open('test_log.txt', 'w').close()

def test_log_to_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out

def test_log_to_file():
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    my_function(3, 4)  # Используем другие значения
    with open("test_log.txt", "r") as f:
        content = f.read()
        assert "my_function ok" in content

def test_log_error_to_console(capsys):
    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    captured = capsys.readouterr()
    assert "my_function error: ZeroDivisionError" in captured.out

def test_log_error_to_file():
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    with open("test_log.txt", "r") as f:
        content = f.read()
        assert "my_function error: ZeroDivisionError" in content

def test_log_with_different_inputs():
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x / y

    # Различные входные данные
    my_function(10, 2)
    my_function(5, 2)
    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    with open("test_log.txt", "r") as f:
        content = f.read()
        assert "my_function ok" in content
        assert "my_function error: ZeroDivisionError" in content
