import numpy as np
from matplotlib.figure import Figure


# klasa umozliwiajaca rysowanie wykresow funkcji z pomoca biblioteki matplotlib
class ChartCreator:

    def __init__(self):
        self.info = ''

        self.start_w = -20
        self.stop_w = 20
        self.start_h = -20
        self.stop_h = 20

        self.start_x = -30
        self.stop_x = 30
        self.start_y = -30
        self.stop_y = 30

        self.formula = None

    # slownik pozwalajacy na refactoring stringa do postaci formuly przyjmowalnej przez matplotlib
    replacements = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'sqrt': 'np.sqrt',
        'tg': 'np.tan',
        'log': 'np.log',
        'log10': 'log10',
        'log2': 'log2',
        '^': '**',
        'abs': 'np.abs',
        'e': 'np.e'
    }

    # metoda zmieniajaca szerokosc zakresu dla danego wykresu, przydatne dla funkcji jedenj zmiennej
    def change_size_w(self, zoom):
        if zoom:
            self.start_w = self.start_w * 0.75
            self.stop_w = self.stop_w * 0.75
        else:
            self.start_w = self.start_w * 1.25
            self.stop_w = self.stop_w * 1.25

    # metoda zmieniajaca wysokosc zakresu dla danego wykresu, przydatne dla funkcji jedenj zmiennej
    def change_size_h(self, zoom):
        if zoom:
            self.start_h = self.start_h * 0.75
            self.stop_h = self.stop_h * 0.75
        else:
            self.start_h = self.start_h * 1.25
            self.stop_h = self.stop_h * 1.25

    # metoda zmieniajaca szerokosc zakresu na osi x dla danego wykresu,
    # przydatne dla funkcji dwoch zmeinnych - zaleznych od x i y
    def change_size_x(self, zoom):
        if zoom:
            self.start_x = self.start_x * 0.5
            self.stop_x = self.stop_x * 0.5
        else:
            self.start_x = self.start_x * 1.5
            self.stop_x = self.stop_x * 1.5

    # metoda zmieniajaca wysokosc zakresu na osi y dla danego wykresu,
    # przydatne dla funkcji dwoch zmeinnych - zaleznych od x i y
    def change_size_y(self, zoom):
        if zoom:
            self.start_y = self.start_y * 0.5
            self.stop_y = self.stop_y * 0.5
        else:
            self.start_y = self.start_y * 1.5
            self.stop_y = self.stop_y * 1.5

    # metoda wykonujaca refactoring dostarczonej formuły z postaci napisu na postac akceptowalna przez
    # biblioteke matplotlib z uzyciem wczesniej zdefiniowanego slownika zamiennikow
    @staticmethod
    def refactor_formula(formula):
        new_formula = formula
        for old, new in ChartCreator.replacements.items():
            new_formula = new_formula.replace(old, new)
        return new_formula

    # funkcja umozliwajaca rysowanie funkcji jednej zmiennej na normalnej skali liczbowej
    def plot_a_function_of_one_variable(self, formula, start_w, stop_w, if_grid):
        # okreslenie rozmiaru obrazka z wykresem wybranej funkcji
        fig = Figure(figsize=(5, 4.75), dpi=100)
        # okreslenie punktow pomiaru przydatnych do rysowania wykresu
        x = np.linspace(start=start_w, stop=stop_w, num=100)
        # refactoring formuly
        new_formula = ChartCreator.refactor_formula(formula)
        # jesli w formule wystepuje dzielenie przez 0 - blad
        if '/0' in new_formula:
            self.info = "zero division error"
            print("zero division error")
        else:
            try:
                # dodawanie wykresu do obrazka
                plot1 = fig.add_subplot(111)

                # jesli formula to liczba calkowita
                if new_formula.isdigit():
                    x = [start_w, stop_w]
                    y = [int(new_formula), int(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                # jesli formula to liczba rzeczywista
                elif new_formula.replace('.', '', 1).isdigit():
                    x = [start_w, stop_w]
                    y = [float(new_formula), float(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                # rozpatrzenie polskiego oznaczenia liczb rzeczywistych
                elif new_formula.replace(',', '', 1).isdigit():
                    float_formula = new_formula.replace(',', '.', 1)
                    x = [start_w, stop_w]
                    y = [float(float_formula), float(float_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                # jesli rozpatrujemy stala matematyczna e
                elif new_formula == 'np.e':
                    x = [start_w, stop_w]
                    y = [np.e, np.e]
                    plot1.plot(x, y, 'y', label=formula)
                else:
                    # przetworzenie formuly na zapis matematyczny i wykreslenie wykresu
                    plot1.plot(x, eval(new_formula), label=formula)

                # okreslenie czy na wykresie powinna wystapic siatka
                if if_grid:
                    plot1.grid()
                # dodanie legendy z oznaczeniem
                plot1.legend(loc="upper right")
                self.info = 'done'
                return fig
            except SyntaxError:
                self.info = "syntax error"
                print("syntax error")
            except NameError:
                self.info = "name error"
                print("name error")
            except TypeError:
                self.info = "type error"
                print("type error")
            except ZeroDivisionError:
                self.info = "zero division error"
                print("zero division error")

    # funkcja umozliwajaca rysowanie kilku funkcji jednej zmiennej na normalnej skali liczbowej
    def plot_a_several_function(self, start_w, stop_w, if_grid, list_):
        # okreslenie rozmiaru obrazka z wykresem wybranej funkcji
        fig = Figure(figsize=(5, 4.75), dpi=100)

        flag = True
        # sprawdzenie wszystkich formul czy nie wystepuje w nich dzielenie przez 0
        for line in list_:
            # refactoring formuly
            new_formula = ChartCreator.refactor_formula(line)
            if '/0' in new_formula:
                self.info = "zero division error in {}".format(line)
                flag = False

        # jesli nie ma dzielenia przez 0 w zadnej z formul przechodze dalej do dalszego przetwarzania
        if flag:
            try:
                # dodawanie wykresu do obrazka
                plot1 = fig.add_subplot(111)
                for line in list_:
                    # refactoring formuly
                    new_formula = ChartCreator.refactor_formula(line)
                    self.formula = line
                    # jesli formula to liczba calkowita
                    if new_formula.isdigit():
                        x = [start_w, stop_w]
                        y = [int(new_formula), int(new_formula)]
                        plot1.plot(x, y, 'y', label=line)
                    # jesli formula to liczba rzeczywista
                    elif new_formula.replace('.', '', 1).isdigit():
                        x = [start_w, stop_w]
                        y = [float(new_formula), float(new_formula)]
                        plot1.plot(x, y, 'y', label=line)
                    # rozpatrzenie polskiego oznaczenia liczb rzeczywistych
                    elif new_formula.replace(',', '', 1).isdigit():
                        float_formula = new_formula.replace(',', '.', 1)
                        x = [start_w, stop_w]
                        y = [float(float_formula), float(float_formula)]
                        plot1.plot(x, y, 'y', label=line)
                    # jesli rozpatrujemy stala matematyczna e
                    elif new_formula == 'np.e':
                        x = [start_w, stop_w]
                        y = [np.e, np.e]
                        plot1.plot(x, y, 'y', label=line)
                    else:
                        # okreslenie punktow pomiaru przydatnych do rysowania wykresu
                        x = np.linspace(start=start_w, stop=stop_w, num=100)
                        # przetworzenie formuly na zapis matematyczny i wykreslenie wykresu
                        plot1.plot(x, eval(new_formula), label=line)
                # okreslenie czy na wykresie powinna wystapic siatka
                if if_grid:
                    plot1.grid()
                # dodanie legendy z oznaczeniem
                plot1.legend(loc="upper right")
                self.info = 'done'
                return fig
            except SyntaxError:
                self.info = "syntax error in {}".format(self.formula)
            except NameError:
                self.info = "name error in {}".format(self.formula)
            except TypeError:
                self.info = "type error in {}".format(self.formula)
            except ZeroDivisionError:
                self.info = "zero division error in {}".format(self.formula)

    # funkcja umozliwajaca rysowanie funkcji jednej zmiennej na logarytmicznej skali liczbowej
    def plot_a_function_on_a_logarithmic_scale(self, formula, start_w, stop_w, if_grid):
        # okreslenie rozmiaru obrazka z wykresem wybranej funkcji
        fig = Figure(figsize=(5, 4.75), dpi=100)
        # okreslenie punktow pomiaru przydatnych do rysowania wykresu
        x = np.linspace(start=start_w, stop=stop_w, num=100)
        # refactoring formuly
        new_formula = ChartCreator.refactor_formula(formula)
        # jesli w formule wystepuje dzielenie przez 0 - blad
        if '/0' in new_formula:
            self.info = "zero division error"
            print("zero division error")
        else:
            try:
                # dodawanie wykresu do obrazka
                plot1 = fig.add_subplot(111)

                # jesli formula to liczba calkowita
                if new_formula.isdigit():
                    x = [start_w, stop_w]
                    y = [int(new_formula), int(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                # jesli formula to liczba rzeczywista
                elif new_formula.replace('.', '', 1).isdigit():
                    x = [start_w, stop_w]
                    y = [float(new_formula), float(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                # rozpatrzenie polskiego oznaczenia liczb rzeczywistych
                elif new_formula.replace(',', '', 1).isdigit():
                    float_formula = new_formula.replace(',', '.', 1)
                    x = [start_w, stop_w]
                    y = [float(float_formula), float(float_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                # jesli rozpatrujemy stala matematyczna e
                elif new_formula == 'np.e':
                    x = [start_w, stop_w]
                    y = [np.e, np.e]
                    plot1.plot(x, y, 'y', label=formula)
                else:
                    # przetworzenie formuly na zapis matematyczny i wykreslenie wykresu
                    plot1.plot(x, eval(new_formula), label=formula)

                # ustawienie skali x i y wykresu na logarytmiczna
                plot1.set_xscale('log')
                plot1.set_yscale('log')

                # ustawienie granicy skali x wykresu
                plot1.set_xlim(start_w, stop_w)
                # okreslenie czy na wykresie powinna wystapic siatka
                if if_grid:
                    plot1.grid()
                # dodanie legendy z oznaczeniem
                plot1.legend(loc="upper right")
                self.info = 'done'
                return fig
            except SyntaxError:
                self.info = "syntax error"
                print("syntax error")
            except NameError:
                self.info = "name error"
                print("name error")
            except TypeError:
                self.info = "type error"
                print("type error")
            except ZeroDivisionError:
                self.info = "zero division error"
                print("zero division error")

    # funkcja umozliwajaca rysowanie funkcji dwóch zmiennych
    def plot_function_with_two_variables(self, formula, start_x, stop_x, start_y, stop_y):
        # jezeli formula nie zawiera choc jednej zmiennej x lub y wtedy komunikat
        if formula.isdigit() or formula.replace('.', '', 1).isdigit() or formula.replace(',', '', 1).isdigit():
            self.info = 'Formula should be drawn using a single variable function, for this function at least one x and/or y variable is needed'
        else:
            # funkcja umozliwiajaca stworzenie funkcji dwoch zmiennych x i y
            def f(x, y):
                # refactoring formuly
                new_formula = ChartCreator.refactor_formula(formula)
                # zwrocenie fromuly przedstawionej jako zpais matemtyczny
                return eval(new_formula)

            # okreslenie rozmiaru obrazka z wykresem wybranej funkcji
            fig = Figure(figsize=(5, 4.75), dpi=100)
            # ustawienie zakresu zmiennych x i y na wykresie
            x = np.linspace(start_x, stop_x, 100)
            y = np.linspace(start_y, stop_y, 100)

            # zwrocenie macierzy punktow przydatnych do rysowania wykresu
            X, Y = np.meshgrid(x, y)

            try:
                Z = f(X, Y)
                # dodawanie wykresu w 3D do obrazka
                ax = fig.add_subplot(111, projection='3d')
                # kreslenie przestrzeni bedacej odzwierciedleniem wskazanej formuly
                ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis_r', edgecolor='none')

                # ustawienie nazw poszczegolnyvh osi
                ax.set_xlabel('x', fontsize=11)
                ax.set_ylabel('y', fontsize=11)
                ax.set_zlabel('z', fontsize=11)
                self.info = 'done'
                return fig
            except SyntaxError:
                self.info = "syntax error"
                print("syntax error")
            except NameError:
                self.info = "name error"
                print("name error")
            except TypeError:
                self.info = "type error"
                print("type error")
            except ZeroDivisionError:
                self.info = "zero division error"
                print("zero division error")
