import numpy as np


class Matrix:
    def __init__(self, rows=None, columns=None):
        self.number_of_rows = rows
        self.number_of_columns = columns
        self.values = None
        self.matrix_form = None

    def check_data(self, values):
        number_of_data_required = self.number_of_rows * self.number_of_columns
        if len(values) < number_of_data_required:
            for i in range(len(values), number_of_data_required):
                values.append(0)
            return values
        elif len(values) > number_of_data_required:
            new_list = []
            for i in range(number_of_data_required):
                new_list.append(values[i])
            return new_list
        else:
            return values

    def reshape_to_matrix(self):
        return np.array(self.values).reshape(self.number_of_rows, self.number_of_columns)

    def transpose_matrix(self):
        return np.transpose(self.matrix_form)

    def rank_of_matrix(self):
        return np.linalg.matrix_rank(self.matrix_form)

    def trace_of_matrix(self):
        return np.trace(self.matrix_form)

    def print_matrix(self):
        print("Matrix {}x{}: \n".format(self.number_of_rows, self.number_of_columns), self.matrix_form)


class SquareMatrix(Matrix):
    def __init__(self, dimension):
        super().__init__(dimension, dimension)

    def calculate_determinant_of_the_matrix(self):
        return int(np.linalg.det(self.matrix_form))

    def matrix_inversion(self):
        if SquareMatrix.calculate_determinant_of_the_matrix(self) != 0:
            return np.linalg.inv(self.matrix_form)
        else:
            return "Wyznacznik jest równy 0, nie ma macierzy odwrotnej"


# if __name__ == '__main__':
#     matrix = Matrix(2, 3, [3, 5, 1, 6, 2, 6])
    #     print(matrix.trace_of_matrix())
    # #     # print(matrix.rank_of_matrix())
    # #     # matrix.print_matrix()
    # #     # matrix2 = SquareMatrix(3, [3, 5, 1, 6, 2, 6, 3, 5, 2])
    # #     # print(matrix2.det)
    # #     # matrix2.print_matrix()
    # #     # print(matrix2.matrix_inversion())
    # print(matrix.transpose_matrix())
# #     # print(matrix2.rank_of_matrix())
