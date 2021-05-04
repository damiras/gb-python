"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

source_list = []
list_of_numbers = input('Введите элементы исходного списка через пробел: ').split()
for number in list_of_numbers:
    try:
        source_list.append(int(number))
    except ValueError:
        pass
print('Исходный список:', source_list)

result_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]]
print('Результат:', result_list)
