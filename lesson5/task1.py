"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

output_filename = 'task1.dat'
output_file = open(output_filename, 'w', encoding='utf-8')

print("Введите текст для записи в файл. Пустая строка - конец ввода.")

line = input()
while line:
    output_file.write(line + '\n')
    line = input()

output_file.close()
