import numpy as np


# klasa implementacyjna macierzy o dowolnym rozmiarze
class Matrix:
    def __init__(self, rows=None, columns=None):
        self.number_of_rows = rows
        self.number_of_columns = columns
        self.values = None
        self.matrix_form = None

    # metoda sprawdzajaca czy ilosc podanych danych jest odpowiednia, jesli nie odpowiednio modyfikuje liste ktora posluzy mi pozniej jako wartosci macierzy
    def check_data(self, values):
        number_of_data_required = self.number_of_rows * self.number_of_columns
        # jesli mamy za malo wartosci niz zadeklarowane ilosc rzedow * ilosc kolumn wtedy uzupelniam dane zerami
        if len(values) < number_of_data_required:
            for i in range(len(values), number_of_data_required):
                values.append(0)
            return values
        # jesli danych jest za duzo wtedy wybieram tylko okreslona ilosc
        elif len(values) > number_of_data_required:
            new_list = []
            for i in range(number_of_data_required):
                new_list.append(values[i])
            return new_list
        else:
            return values

    # zamiana listy wartosci na macierz z pomoca metody array z biblioteki numpy
    def reshape_to_matrix(self):
        return np.array(self.values).reshape(self.number_of_rows, self.number_of_columns)

    # metoda wykonujaca trasponowanie macierzy z pomoca funkcji transpose z biblioteki numpy
    def transpose_matrix(self):
        return np.transpose(self.matrix_form)

    # metoda obliczajaca rzad macierzy z pomoca funkcji linalg.matrix_rank z biblioteki numpy
    def rank_of_matrix(self):
        return np.linalg.matrix_rank(self.matrix_form)

    # metoda obliczajca slad macierzy z pomoca funkcji trace z biblioteki numpy
    def trace_of_matrix(self):
        return np.trace(self.matrix_form)

    # metoda wykonywana w przypadku testow sluzaca do printowania macierzy
    def print_matrix(self):
        print("Matrix {}x{}: \n".format(self.number_of_rows, self.number_of_columns), self.matrix_form)


# klasa implemetacyjna macierzy kwadratowej - specjalny rodzaj macierzy posiadajacej jednakowe wymiary
class SquareMatrix(Matrix):
    def __init__(self, dimension):
        super().__init__(dimension, dimension)

    # metoda obliczajaca wyznacznik macierzy z pomoca funkcji linalg.det z biblioteki numpy
    def calculate_determinant_of_the_matrix(self):
        return int(np.linalg.det(self.matrix_form))

    # metoda obliczajaca macierz odwrotna z pomoca funkcji linalg.inv z biblioteki numpy
    def matrix_inversion(self):
        # aby obliczyc macierz odwrotna jej wyznacznik musi byc rozny od 0
        if SquareMatrix.calculate_determinant_of_the_matrix(self) != 0:
            return np.linalg.inv(self.matrix_form)
        else:
            return "Wyznacznik jest równy 0, nie ma macierzy odwrotnej"
