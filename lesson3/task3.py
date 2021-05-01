"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_of_max_two_numbers(n1, n2, n3):
    return sum([n1, n2, n3]) - min(n1, n2, n3)


print(sum_of_max_two_numbers(5, 1, 3))
