"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name=''):
        self.name = name

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size, name=''):
        super().__init__(name)
        self.size = size

    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 1)

    def __str__(self):
        return 'Пальто' + (' ' + self.name if self.name else '')


class Suit(Clothes):

    def __init__(self, height, name=''):
        super().__init__(name)
        self.height = height

    def tissue_consumption(self):
        return round(self.height * 2 + 0.3, 1)

    def __str__(self):
        return 'Костюм' + (' ' + self.name if self.name else '')


coat = Coat(56, 'Finn Flare')
suit = Suit(1.89)
print(f"У {coat} расход ткани составляет: {coat.tissue_consumption()} метров.")
print(f"{suit} расходует {suit.tissue_consumption()} метров ткани")

