"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

number_count = 10
number_from_to = (-100, 100)

numbers_filename = 'task5.dat'
with open(numbers_filename, 'w+', encoding='utf-8') as nf:
    # записываем числа в файл
    for n in range(number_count):
        number = randint(*number_from_to)
        nf.write((' ' if n else '') + str(number))

    # читаем числа из файла и вычисляем их сумму
    nf.seek(0)
    numbers_line = nf.readline()
    numbers = map(int, numbers_line.split())
    numbers_sum = sum(numbers)
    print('Сумма чисел в файле:', numbers_sum)
