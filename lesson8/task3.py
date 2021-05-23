"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NotNumberError(Exception):
    pass


def check_number(number, stop_phrase=None):
    if stop_phrase is not None and number == stop_phrase:
        return stop_phrase
    try:
        return float(number)
    except ValueError:
        raise NotNumberError(f"'{number}' не является числом! Введие корректное действительное число!")


def input_number(stop_phrase=None):
    while True:
        try:
            return check_number(input(), stop_phrase)
        except NotNumberError as err:
            print(err)


def input_next_number(stop_phrase='stop'):
    print(f'Введите список чисел. Каждое число вводится с новой строки. Для завершения введите "{stop_phrase}".')
    number = input_number(stop_phrase)
    while number != stop_phrase:
        yield number
        number = input_number(stop_phrase)


# list_of_numbers = []
# for numb in input_next_number('end'):
#     list_of_numbers.append(numb)
# print(f'Список чисел: {list_of_numbers}')


# другим спсобом

class InputNumbers:

    def __init__(self, stop_phrase: str = 'stop'):
        self.stop_phrase = stop_phrase

    def __iter__(self):
        print(f'Введите список чисел. Каждое число вводится с новой строки. '
              f'Для завершения введите "{self.stop_phrase}".')
        return self

    def __next__(self):
        while True:
            word = input()
            if word == self.stop_phrase:
                raise StopIteration()
            try:
                return InputNumbers._word_as_number(word)
            except NotNumberError:
                print("Введенное значение не является числом! Пожалуйста, введите действительное число!")

    @staticmethod
    def _word_as_number(word: str):
        try:
            return float(word)
        except ValueError:
            raise NotNumberError("Cannot convert to float!")


list_of_numbers = []
for numb in InputNumbers('end'):
    list_of_numbers.append(numb)
print(f'Список чисел: {list_of_numbers}')
