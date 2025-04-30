import pytest
from unittest.mock import patch
from main import main

def test_main(capsys):
    with patch('builtins.input', side_effect=['1', 'EXECUTED', 'да', 'по возрастанию', 'да', 'нет']):
        main()
        captured = capsys.readouterr()
        assert "Привет! Добро пожаловать в программу работы с банковскими транзакциями." in captured.out
        assert "Операции отфильтрованы по статусу \"EXECUTED\"" in captured.out
        assert "Распечатываю итоговый список транзакций..." in captured.out

if __name__ == "__main__":
    pytest.main()
