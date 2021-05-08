"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

input_filename = 'task2.dat'
input_file = open(input_filename, 'r', encoding='utf-8')

lines_count = 0
words_in_lines_count = []

for line in input_file:
    lines_count += 1
    words_in_line = line.split()
    words_in_lines_count.append(len(words_in_line))

input_file.close()

print(f'Всего строк: {lines_count}')
for n in range(lines_count):
    print(f'Слов в строке {n + 1}: {words_in_lines_count[n]}')
