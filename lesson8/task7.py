"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, r: float, i: float = 0):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        r_part = self.r * other.r - self.i * other.i
        i_part = self.r * other.i + self.i * other.r
        return Complex(r_part, i_part)

    def __str__(self):
        return (str(self.r) if self.r else '') + \
               ('' if not self.i else (('-' if self.i < 0 else '+') + ('' if abs(self.i) == 1 else str(self.i)) + 'i'))


if __name__ == '__main__':
    c1 = Complex(1, 2)
    c2 = Complex(2, -3)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)

