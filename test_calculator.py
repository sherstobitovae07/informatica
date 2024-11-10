import pytest
import my_lib


# Тест функции Calculator
class TestCalculator:

    # Фикстура для корректных значений
    @pytest.fixture
    def valid_operations(self):
        return [
            (3, 2, "+", 5),
            (3, 2, "-", 1),
            (3, 2, "*", 6),
            (6, 2, "/", 3),
        ]

    # Фикстура для некорректных значений (операнды и операции)
    @pytest.fixture
    def invalid_operations(self):
        return [
            (3, 0, "/", ValueError),  # Деление на ноль
            ("three", 2, "+", ValueError),  # Неверный операнд
            (3, "two", "*", ValueError),  # Неверный операнд
            (3, 2, "%", ValueError),  # Неверный оператор
        ]

    # Тест на корректные операции
    def test_valid_calculator_operations(self, valid_operations):
        for num1, num2, operation, expected_result in valid_operations:
            assert my_lib.calculator(num1, num2, operation) == expected_result

    # Тест на некорректные операции
    def test_invalid_calculator_operations(self, invalid_operations):
        for num1, num2, operation, expected_exception in invalid_operations:
            with pytest.raises(expected_exception):
                my_lib.calculator(num1, num2, operation)
