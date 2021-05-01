"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
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


def get_numbers_sum(numbers_list) -> tuple[float, bool]:
    """
    Возвращает кортеж из суммы чисел в списке (кортеже) number_list и логического значения - продолжать ли ввод.
    :param list|tuple numbers_list:
    :return: tuple[float, bool]
    """
    result = 0
    resume = True
    for n in numbers_list:
        if not isfloat(n):
            resume = False
            break
        result += float(n)
    return result, resume


total_sum = 0
numbers = input("Введите числа через пробел (стоп-символ: любая строка, не являющаяся числом): ").split()
numbers_sum, resume_input = get_numbers_sum(numbers)
total_sum += numbers_sum
while resume_input:
    numbers = input("Введите следующие числа через пробел: ").split()
    numbers_sum, resume_input = get_numbers_sum(numbers)
    total_sum += numbers_sum
print(f"Итоговая сумма: {total_sum}")
