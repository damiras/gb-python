"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subjects_total_hours = {}

subjects_filename = 'task6.dat'
with open(subjects_filename, 'r', encoding='utf-8') as lf:
    for row in lf:
        row_data = row.split(':')
        subject_name = row_data[0]
        subject_hours_data = row_data[1].split()
        subject_hours = 0
        for subject_hours_type in subject_hours_data:
            if subject_hours_type == '-':
                continue
            subject_hours_type_data = subject_hours_type.split('(')
            subject_hours += int(subject_hours_type_data[0])
        subjects_total_hours[subject_name] = subject_hours

print(subjects_total_hours)
