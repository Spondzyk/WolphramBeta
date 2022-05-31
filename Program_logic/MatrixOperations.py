from Program_logic.Matrix import *


class MatrixOperations:

    @staticmethod
    def matrix_subtraction(matrix1, matrix2):
        if matrix1.number_of_rows == matrix2.number_of_rows and matrix1.number_of_columns == matrix2.number_of_columns:
            r1 = np.subtract(matrix1.matrix_form, matrix2.matrix_form)
            result_matrix = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
            result_matrix.values = r1.flatten()
            result_matrix.matrix_form = result_matrix.reshape_to_matrix()
            return result_matrix
        else:
            return "Macierze nie mają jednakowych wymiarów, nie można ich odjąć"

    @staticmethod
    def matrix_add(matrix1, matrix2):
        if matrix1.number_of_rows == matrix2.number_of_rows and matrix1.number_of_columns == matrix2.number_of_columns:
            r1 = np.add(matrix1.matrix_form, matrix2.matrix_form)
            result_matrix = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
            result_matrix.values = r1.flatten()
            result_matrix.matrix_form = result_matrix.reshape_to_matrix()
            return result_matrix
        else:
            return "Macierze nie mają jednakowych wymiarów, nie można ich dodać"

    @staticmethod
    def matrix_multiply(matrix1, matrix2):
        if matrix1.number_of_columns == matrix2.number_of_rows:
            r1 = np.dot(matrix1.matrix_form, matrix2.matrix_form)
            result_matrix = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
            result_matrix.values = r1.flatten()
            result_matrix.matrix_form = result_matrix.reshape_to_matrix()
            return result_matrix
        else:
            return "Macierze mają nie prawidłowe wymiary, nie można ich pomnożyć"

    @staticmethod
    def check_if_matrix(matrix):
        if not isinstance(matrix, str):
            return True
        else:
            return False


# if __name__ == '__main__':
#     operation = MatrixOperations()
#     matrix1 = Matrix(2, 3, [3, 5, 1, 6, 2, 6])
#     matrix2 = Matrix(2, 3, [3, 1, 5, 0, 4, 0])
#
#     matrix_r1 = operation.matrix_add(matrix1, matrix2)
#     if operation.check_if_matrix(matrix_r1):
#         matrix_r1.print_matrix()
#     else:
#         print(matrix_r1)
#
#     matrix_r2 = operation.matrix_subtraction(matrix1, matrix2)
#     if operation.check_if_matrix(matrix_r2):
#         matrix_r2.print_matrix()
#     else:
#         print(matrix_r2)
#
#     matrix3 = Matrix(3, 2, [10, 6, 30, 5, 15, 5])
#     matrix_r3 = operation.matrix_multiply(matrix1, matrix3)
#     if operation.check_if_matrix(matrix_r3):
#         matrix_r3.print_matrix()
#     else:
#         print(matrix_r3)
#
#     matrix_r4 = operation.matrix_multiply(matrix1, matrix2)
#     if operation.check_if_matrix(matrix_r4):
#         matrix_r4.print_matrix()
#     else:
#         print(matrix_r4)
