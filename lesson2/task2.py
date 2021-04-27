"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

replace_list = input('Введите элементы списка через пробел: ').split()
print("Исходный список:", replace_list)
if len(replace_list) > 1:
    for i in range(1, len(replace_list), 2):
        replace_list[i - 1], replace_list[i] = replace_list[i], replace_list[i - 1]
print("Конечный список:", replace_list)
