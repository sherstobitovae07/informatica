import pytest
import my_lib


# Тест функции Fibonacci
class TestFibonacci:

    # Фикстура для корректных значений
    @pytest.fixture
    def valid_values(self):
        return [
            (0, []),
            (1, [0]),
            (2, [0, 1]),
            (5, [0, 1, 1, 2, 3]),
        ]

    # Фикстура для некорректных значений
    @pytest.fixture
    def invalid_values(self):
        return [-1, "abc", 3.5]

    # Тест на корректные значения
    def test_valid_fibonacci(self, valid_values):
        for n, expected in valid_values:
            assert my_lib.fibonacci(n) == expected

    # Тест на некорректные значения
    def test_invalid_fibonacci(self, invalid_values):
        for n in invalid_values:
            with pytest.raises(ValueError):
                my_lib.fibonacci(n)
