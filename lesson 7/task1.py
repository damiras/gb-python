"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, list_of_lists: list):
        if not list_of_lists:
            raise ValueError("empty matrix")
        self.__columns_count = 0
        for row in list_of_lists:
            if not row:
                raise ValueError("empty matrix row")
            if not self.__columns_count:
                self.__columns_count = len(row)
                self.columns_widths = [0 for _ in range(self.__columns_count)]
            elif self.__columns_count != len(row):
                raise ValueError("matrix rows have different dimensions")
            for column, cell in enumerate(row):
                if self.columns_widths[column] < len(str(cell)):
                    self.columns_widths[column] = len(str(cell))
        self.__list_of_list = list_of_lists

    def __str__(self):
        matrix_string = ""
        for row in self.__list_of_list:
            formatted_row = ''
            for column, cell in enumerate(row):
                formatted_row += str(cell).rjust(self.columns_widths[column] + 1)
            matrix_string += formatted_row + '\n'
        return matrix_string

    def __getitem__(self, item):
        return self.__list_of_list[item]

    @property
    def columns(self):
        return self.__columns_count

    @property
    def rows(self):
        return len(self.__list_of_list)

    def __add__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            raise ValueError("matrices have different dimensions")
        sum_matrix_data = []
        for row_number in range(self.rows):
            sum_matrix_data.append([])
            for column_number in range(self.columns):
                sum_matrix_data[row_number].append(self[row_number][column_number] + other[row_number][column_number])
        return Matrix(sum_matrix_data)


m1 = Matrix([[1, 2, 3, 4], [500, 6, 7, 8], [9, 10, 1100, 12]])
m2 = Matrix([[11, 22, 33, 44], [55, 66, 77, 88], [99, 101, 111, 1212]])
print(m1 + m2)
