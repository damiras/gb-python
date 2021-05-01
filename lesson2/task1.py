"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

type_test_list = [1, 2, 3, [1, 2, 3], (1,), 1.23, "123", set('123'), {1, 2, 3}, frozenset([1, 2, 3]), {1: 2, 1.2: '3'}]
for index, element in enumerate(type_test_list):
    print("element", index, "is", str(type(element))[8:-2])