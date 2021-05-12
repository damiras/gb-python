"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    speed = 0

    def __init__(self, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self._stopped = True

    def go(self, speed):
        self.speed = speed
        print(self.color.title(), self.name, 'is going!')

    def stop(self):
        self.speed = 0
        print(self.color.title(), self.name, 'stopped!')

    def turn(self, direction):
        print(self.color.title(), self.name, 'turned', direction)

    def show_speed(self):
        print('Current speed of', self.color.title(), self.name, 'is', self.speed)


class TownCar(Car):

    def __init__(self, color):
        super().__init__(color, 'Town Car')

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('You are going too fast! Please, slow down!')


class WorkCar(Car):

    def __init__(self, color):
        super().__init__(color, 'Work Car')

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('You are going too fast! Please, slow down!')


class SportCar(Car):

    def __init__(self, color):
        super().__init__(color, 'Sport Car')


class PoliceCar(Car):

    def __init__(self, color):
        super().__init__(color, 'Police Car', True)


police_car = PoliceCar('white')
sport_car = SportCar('blue')
work_car = WorkCar('yellow')
town_car = TownCar('orange')

police_car.color = 'green'
police_car.go(80)
police_car.show_speed()

sport_car.speed = 120
sport_car.show_speed()

town_car.go(70)
town_car.turn('left')
town_car.show_speed()
town_car.stop()

work_car.go(50)
work_car.turn('right')
work_car.show_speed()
work_car.stop()
