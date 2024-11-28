import pytest
from src.decorators import log


# тесты логирования в консоль
def test_log_to_console(capsys):
    @log()
    def test_func(x, y):
        return x + y

    test_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "test_func started\ntest_func ok"

def test_log_to_console_error(capsys):
    @log()
    def test_func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "test_func started\ntest_func error: ZeroDivisionError. Inputs: (1, 0), {}"





