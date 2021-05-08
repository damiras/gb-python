"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calculate_salary(hours_count: int, rate: float, prize: float) -> float:
    return hours_count * rate + prize


try:
    hours = int(argv[1])
    rate_per_hour = float(argv[2])
    premium = 0
    try:
        premium = float(argv[3])
    except IndexError:
        pass
    except ValueError:
        print("Премия должна быть действительным числом!")
        exit()
    print(calculate_salary(hours, rate_per_hour, premium))
except IndexError:
    print("Первым и вторым параметрами должны быть выработка в часах и ставка в час соответственно!")
    exit()
except ValueError:
    print("Выработка в часах должна быть целым числом, а ставка в час действительным!")
    exit()
