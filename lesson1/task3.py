"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number = input("Введите целое положительное число: ")
n = int(number)
nn = int(number + number)
nnn = int(number + number + number)
result = n + nn + nnn
print(f"Результат: {result}")
