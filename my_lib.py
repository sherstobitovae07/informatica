def fibonacci(n):
    """
    Определяет первые n чисел Фибоначчи.
    :param n: Количество чисел Фибоначчи для вычисления.
    :return: Список первых n чисел Фибоначчи.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть положительным целым числом")

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def bubble_sort(arr):
    """
    Сортировка пузырьком для списка чисел.
    :param arr: Список чисел для сортировки.
    :return: Отсортированный список.
    """
    if not isinstance(arr, list) or not all(isinstance(i, (int, float)) for i in arr):
        raise ValueError("Входные данные должны быть списком чисел")

    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


def calculator(num1, num2, operation):
    """
    Калькулятор для выполнения простых арифметических операций.
    :param num1: Первое число.
    :param num2: Второе число.
    :param operation: Строка операции, одна из "+", "-", "*", "/".
    :return: Результат операции.
    """
    if operation not in ["+", "-", "*", "/"]:
        raise ValueError("Некорректный оператор. Используйте +, -, *, или /.")

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Операнды должны быть числами.")

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно.")
        return num1 / num2
