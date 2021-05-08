"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

salary_filename = 'task3.dat'
salary_file = open(salary_filename, 'r', encoding='utf-8')

low_income_salary = 20000
low_income_employees = []
salaries = []

for row in salary_file:
    salary_data = row.strip().split()
    employee = salary_data[0]
    salary = float(salary_data[1])
    if salary < low_income_salary:
        low_income_employees.append(employee)
    salaries.append(salary)

salary_file.close()

if low_income_employees:
    print('Сотрудники с низким доходом:', ', '.join(low_income_employees))
else:
    print('Нет сотрудников с низким доходом!')

print('Средний доход сотрудников:', round(sum(salaries) / len(salaries), 1))
