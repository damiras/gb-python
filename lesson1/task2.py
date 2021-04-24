"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = int(input("Введите количество секунд: "))
minutes = int(seconds / 60)
seconds = seconds % 60
hours = int(minutes / 60)
minutes = minutes % 60
print(f"Время в формате 'чч:мм:сс': {hours:02d}:{minutes:02d}:{seconds:02d}")
