"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return (self.position + ' ' + self.name + ' ' + self.surname).title()

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


employee = Position('John', 'Smith', 'accountant', 2000, 1000)
print(employee.get_full_name(), 'has', employee.get_total_income(), 'total income.')

