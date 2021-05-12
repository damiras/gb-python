"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from itertools import cycle
from time import sleep


class TrafficLight:
    __color_times = (('red', 7), ('yellow', 2), ('green', 5))
    __color = 'green'

    def running(self, init_color='red', switching_count=9):
        if self.__chek_color(init_color):
            n = 1
            for color, seconds in cycle(TrafficLight.__color_times):
                if init_color is not None and color != init_color:
                    continue
                if n > switching_count:
                    break
                init_color = None
                self.__color = color
                print(f'{self.__color.title()} color! Waiting {seconds} seconds!')
                sleep(seconds)
                n += 1
            return self.__color
        else:
            return False

    def __chek_color(self, color_to_check):
        if color_to_check not in dict(TrafficLight.__color_times).keys():
            print("Invalid traffic light initial color. Traffic light supports red, yellow and green colors only!")
            return False
        previous_color = self.__color
        for color, seconds in TrafficLight.__color_times:
            if color == color_to_check:
                if previous_color == self.__color:
                    self.__color = color_to_check
                    return True
                else:
                    print("Incorrect traffic light color order. Correct order is: red, yellow, green")
                    return False
            previous_color = color


traffic_light = TrafficLight()
traffic_light.running('red', 3)
traffic_light.running('yellow')
