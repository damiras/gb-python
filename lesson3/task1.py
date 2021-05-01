"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def isfloat(number: str) -> bool:
    """
    Проверяет переводится ли строка в число с плавающей точкой или нет.
    :param str number:
    :return: bool
    """
    try:
        float(number)
        return True
    except ValueError:
        return False


def divide(dividend: float, divider: float) -> float:
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        return float('NaN')


def input_dividend_and_divider() -> tuple[float, float]:
    """
    Просит ввести пользователя два действительных числа (делимое и делитель)
    и возвращает соотвественно два числа с плавающей точкой.
    :return: tuple[float, float]
    """
    a_b = tuple(input("Введите делимое и частное через пробел: ").split())
    a_b = a_b[:2] if len(a_b) > 1 else ('', '')
    a, b = a_b
    while not (isfloat(a) and isfloat(b)):
        print('Делимое и делитель должны быть действительными числами!')
        a_b = tuple(input("Введите делимое и частное через пробел: ").split())
        a_b = a_b[:2] if len(a_b) > 1 else ('', '')
        a, b = a_b
    return float(a), float(b)


n, m = input_dividend_and_divider()
print('Результат: ', divide(n, m))

