"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


def multiply(el_prev, el):
    return el_prev * el


numbers = [n for n in range(100, 1001, 2)]
result = reduce(multiply, numbers)
print(result)
