"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

numbers = set()
repetitions = set()
source_list = list()
list_of_numbers = input('Введите элементы исходного списка через пробел: ').split()
for element in list_of_numbers:
    try:
        number = int(element)
        source_list.append(number)
        if number in numbers:
            repetitions.add(number)
        numbers.add(number)
    except ValueError:
        pass

print('Исходный список:', source_list)

result_list = [n for n in source_list if n not in repetitions]
print('Результат:', result_list)
