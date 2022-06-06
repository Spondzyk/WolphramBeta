from Program_logic.Matrix import *


# klasa umozliwiajaca wykonywanie dzialan algebraicznych na dwoch macierzach
class MatrixOperations:

    # metoda umożliwiajaca odejmowanie macierzy
    @staticmethod
    def matrix_subtraction(matrix1, matrix2):
        # sprawdzam czy rozmiary macierzy sa odpowiednie
        if matrix1.number_of_rows == matrix2.number_of_rows and matrix1.number_of_columns == matrix2.number_of_columns:
            # korzystam z metody substract zawartej w bibliotece numpy by otrzymac macierz wynikowa
            r1 = np.subtract(matrix1.matrix_form, matrix2.matrix_form)
            result_matrix = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
            result_matrix.values = r1.flatten()
            result_matrix.matrix_form = result_matrix.reshape_to_matrix()
            return result_matrix
        else:
            return "Macierze nie mają jednakowych wymiarów, nie można ich odjąć"

    # metoda umozliwiajaca dodawanie macierzy
    @staticmethod
    def matrix_add(matrix1, matrix2):
        # sprawdzam czy rozmiary macierzy sa odpowiednie
        if matrix1.number_of_rows == matrix2.number_of_rows and matrix1.number_of_columns == matrix2.number_of_columns:
            # korzystam z metody add zawartej w bibliotece numpy by otrzymac macierz wynikowa
            r1 = np.add(matrix1.matrix_form, matrix2.matrix_form)
            result_matrix = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
            result_matrix.values = r1.flatten()
            result_matrix.matrix_form = result_matrix.reshape_to_matrix()
            return result_matrix
        else:
            return "Macierze nie mają jednakowych wymiarów, nie można ich dodać"

    # metoda umożliwiajaca mnozenie macierzy
    @staticmethod
    def matrix_multiply(matrix1, matrix2):
        # sprawdzam czy rozmiary macierzy sa odpowiednie
        if matrix1.number_of_columns == matrix2.number_of_rows:
            # korzystam z metody dot zawartej w bibliotece numpy by otrzymac macierz wynikowa
            r1 = np.dot(matrix1.matrix_form, matrix2.matrix_form)
            result_matrix = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
            result_matrix.values = r1.flatten()
            result_matrix.matrix_form = result_matrix.reshape_to_matrix()
            return result_matrix
        else:
            return "Macierze mają nie prawidłowe wymiary, nie można ich pomnożyć"

    # metoda sprawdzajaca czy wynikiem dzialania jest macierz czy komunikat o bledzie
    @staticmethod
    def check_if_matrix(matrix):
        if not isinstance(matrix, str):
            return True
        else:
            return False
