"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

from datetime import date


class NotIntegerError(Exception):
    pass


class Date:

    def __init__(self, initial_date: str):
        date_components = initial_date.split('-')
        if not len(date_components) == 3:
            raise ValueError("Initial date param should match '(D)D-(M)M-YYYY' format!")
        try:
            self.day = self.to_int(date_components[0])
            self.month = self.to_int(date_components[1])
            self.year = self.to_int(date_components[2])
        except NotIntegerError as error:
            raise ValueError(str(error))
        if not Date.is_valid(self.year, self.month, self.day):
            raise ValueError("Invalid initial date!")

    @classmethod
    def to_int(cls, value: str):
        try:
            return int(value)
        except ValueError:
            raise NotIntegerError("Day, month and year must be integer values!")

    @staticmethod
    def is_valid(year: int, month: int, day: int) -> bool:
        today = date.today()
        if today.year - 100 < year < today.year + 100:
            if 1 <= month <= 12:
                days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if not year % 4:  # високосный год
                    days_in_months[1] = 29  # в феврале 29 дней
                if 1 <= day <= days_in_months[month - 1]:
                    return True
        return False

    def __str__(self):
        return str(self.day).zfill(2) + '.' + str(self.month).zfill(2) + '.' + str(self.year)


if __name__ == '__main__':
    try:
        my_date = Date('29-2-2020')
        print(my_date)
    except ValueError as err:
        print(err)

    try:
        my_date = Date('abc')
    except ValueError as err:
        print(err)

    try:
        my_date = Date('a-b-c')
    except ValueError as err:
        print(err)

    try:
        my_date = Date('29-02-2001')
    except ValueError as err:
        print(err)
