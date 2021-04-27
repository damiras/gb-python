"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
seasons_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}

month = input('Введите номер месяца года (от 1 до 12): ')
while not month.isdigit() or not 1 <= int(month) <= 12:
    print("Вы ввели неверный номер месяца!")
    month = input('Введите номер месяца года (от 1 до 12): ')
month = int(month)

season = seasons_list[month - 1]
print(f"Месяц {month} - {season}")

for season, months in seasons_dict.items():
    if month in months:
        print(f"Подтверждаю! Месяц {month} - это {season}.")
        break
