"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input("Введите целое положительное число: "))
max_digit = last_digit = number % 10
step_result = int(number / 10)
while step_result > 0:
    last_digit = step_result % 10
    if last_digit > max_digit:
        max_digit = last_digit
    step_result = int(step_result / 10)
print(f"Самая большая цифра в числе: {max_digit}")
