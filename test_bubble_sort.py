import pytest
import my_lib


# Тест функции Bubble Sort
class TestBubbleSort:

    # Фикстура для корректных значений (списков)
    @pytest.fixture
    def valid_lists(self):
        return [
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([1, 1, 1], [1, 1, 1]),
            ([10, 2, 3, 5], [2, 3, 5, 10]),
            ([], []),  # Пустой список
        ]

    # Фикстура для некорректных значений
    @pytest.fixture
    def invalid_lists(self):
        return [
            "not a list",
            [1, "two", 3],
            {"a": 1, "b": 2},
        ]

    # Тест на корректные значения
    def test_valid_bubble_sort(self, valid_lists):
        for input_list, expected in valid_lists:
            assert my_lib.bubble_sort(input_list) == expected

    # Тест на некорректные значения
    def test_invalid_bubble_sort(self, invalid_lists):
        for invalid_input in invalid_lists:
            with pytest.raises(ValueError):
                my_lib.bubble_sort(invalid_input)
