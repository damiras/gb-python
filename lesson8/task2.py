"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroDivError(Exception):
    pass


def divide(dividend: float, divider: float):
    if not divider:
        raise ZeroDivError()
    return dividend / divider


def input_dividend_and_divider():
    a, b = input("Введите делимое и делитель через пробел: ").split()[:2]
    try:
        a = float(a)
        b = float(b)
        return a, b
    except ValueError:
        print("Данные, которые вы ввели, не являются числами!")
        return input_dividend_and_divider()


n1, n2 = input_dividend_and_divider()
try:
    result = divide(n1, n2)
    print(f"Результат деления {n1}/{n2}: {result}")
except ZeroDivError:
    print("Деление на ноль запрещено!")

