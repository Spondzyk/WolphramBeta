import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure


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

    def change_size_w(self, zoom):
        if zoom:
            self.start_w = self.start_w * 0.75
            self.stop_w = self.stop_w * 0.75
        else:
            self.start_w = self.start_w * 1.25
            self.stop_w = self.stop_w * 1.25

    def change_size_h(self, zoom):
        if zoom:
            self.start_h = self.start_h * 0.75
            self.stop_h = self.stop_h * 0.75
        else:
            self.start_h = self.start_h * 1.25
            self.stop_h = self.stop_h * 1.25

    def change_size_x(self, zoom):
        if zoom:
            self.start_x = self.start_x * 0.5
            self.stop_x = self.stop_x * 0.5
        else:
            self.start_x = self.start_x * 1.5
            self.stop_x = self.stop_x * 1.5

    def change_size_y(self, zoom):
        if zoom:
            self.start_y = self.start_y * 0.5
            self.stop_y = self.stop_y * 0.5
        else:
            self.start_y = self.start_y * 1.5
            self.stop_y = self.stop_y * 1.5

    @staticmethod
    def refactor_formula(formula):
        new_formula = formula
        for old, new in ChartCreator.replacements.items():
            new_formula = new_formula.replace(old, new)
        return new_formula

    def plot_a_function_of_one_variable(self, formula, start_w, stop_w, if_grid):
        fig = Figure(figsize=(5, 4.75), dpi=100)
        x = np.linspace(start=start_w, stop=stop_w, num=100)
        new_formula = ChartCreator.refactor_formula(formula)
        if '/0' in new_formula:
            self.info = "zero division error"
            print("zero division error")
        else:
            try:
                plot1 = fig.add_subplot(111)

                if new_formula.isdigit():
                    x = [start_w, stop_w]
                    y = [int(new_formula), int(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                elif new_formula.replace('.', '', 1).isdigit():
                    x = [start_w, stop_w]
                    y = [float(new_formula), float(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                elif new_formula.replace(',', '', 1).isdigit():
                    float_formula = new_formula.replace(',', '.', 1)
                    x = [start_w, stop_w]
                    y = [float(float_formula), float(float_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                elif new_formula == 'np.e':
                    x = [start_w, stop_w]
                    y = [np.e, np.e]
                    plot1.plot(x, y, 'y', label=formula)
                else:
                    plot1.plot(x, eval(new_formula), label=formula)

                if if_grid:
                    plot1.grid()
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

    def plot_a_several_function(self, start_w, stop_w, if_grid, list_):
        fig = Figure(figsize=(5, 4.75), dpi=100)
        x = np.linspace(start=start_w, stop=stop_w, num=100)

        flag = True
        for line in list_:
            new_formula = ChartCreator.refactor_formula(line)
            if '/0' in new_formula:
                self.info = "zero division error in {}".format(line)
                flag = False

        if flag:
            try:
                plot1 = fig.add_subplot(111)
                for line in list_:
                    new_formula = ChartCreator.refactor_formula(line)
                    self.formula = line
                    if new_formula.isdigit():
                        x = [start_w, stop_w]
                        y = [int(new_formula), int(new_formula)]
                        plot1.plot(x, y, 'y', label=line)
                    elif new_formula.replace('.', '', 1).isdigit():
                        x = [start_w, stop_w]
                        y = [float(new_formula), float(new_formula)]
                        plot1.plot(x, y, 'y', label=line)
                    elif new_formula.replace(',', '', 1).isdigit():
                        float_formula = new_formula.replace(',', '.', 1)
                        x = [start_w, stop_w]
                        y = [float(float_formula), float(float_formula)]
                        plot1.plot(x, y, 'y', label=line)
                    elif new_formula == 'np.e':
                        x = [start_w, stop_w]
                        y = [np.e, np.e]
                        plot1.plot(x, y, 'y', label=line)
                    else:
                        plot1.plot(x, eval(new_formula), label=line)
                if if_grid:
                    plot1.grid()
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

    def plot_a_function_on_a_logarithmic_scale(self, formula, start_w, stop_w, if_grid):
        fig = Figure(figsize=(5, 4.75), dpi=100)
        x = np.linspace(start=start_w, stop=stop_w, num=100)
        new_formula = ChartCreator.refactor_formula(formula)
        if '/0' in new_formula:
            self.info = "zero division error"
            print("zero division error")
        else:
            try:
                plot1 = fig.add_subplot(111)

                if new_formula.isdigit():
                    x = [start_w, stop_w]
                    y = [int(new_formula), int(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                elif new_formula.replace('.', '', 1).isdigit():
                    x = [start_w, stop_w]
                    y = [float(new_formula), float(new_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                elif new_formula.replace(',', '', 1).isdigit():
                    float_formula = new_formula.replace(',', '.', 1)
                    x = [start_w, stop_w]
                    y = [float(float_formula), float(float_formula)]
                    plot1.plot(x, y, 'y', label=formula)
                elif new_formula == 'np.e':
                    x = [start_w, stop_w]
                    y = [np.e, np.e]
                    plot1.plot(x, y, 'y', label=formula)
                else:
                    plot1.plot(x, eval(new_formula), label=formula)

                plot1.set_xscale('log')
                plot1.set_yscale('log')

                plot1.set_xlim(start_w, stop_w)
                if if_grid:
                    plot1.grid()
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

    def plot_function_with_two_variables(self, formula, start_x, stop_x, start_y, stop_y, if_grid):
        if formula.isdigit() or formula.replace('.', '', 1).isdigit() or formula.replace(',', '', 1).isdigit():
            self.info = 'Formula should be drawn using a single variable function, for this function at least one x and/or y variable is needed'
        else:
            def f(x, y):
                new_formula = ChartCreator.refactor_formula(formula)
                return eval(new_formula)

            fig = Figure(figsize=(5, 4.75), dpi=100)
            x = np.linspace(start_x, stop_x, 100)
            y = np.linspace(start_y, stop_y, 100)

            X, Y = np.meshgrid(x, y)

            try:
                Z = f(X, Y)
                ax = fig.add_subplot(111, projection='3d')
                ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis_r', edgecolor='none')

                ax.set_xlabel('x', fontsize=11)
                ax.set_ylabel('y', fontsize=11)
                ax.set_zlabel('z', fontsize=11)
                if if_grid:
                    plt.grid()
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

def show_figure(fig):

    # create a dummy figure and use its
    # manager to display "fig"
    dummy = plt.figure()
    new_manager = dummy.canvas.manager
    new_manager.canvas.figure = fig
    fig.set_canvas(new_manager.canvas)


if __name__ == '__main__':
    chart = ChartCreator()
    # chart.plot_a_function_of_one_variable("x^3-6*x^2+4*x+12", None, None, None, None, True)
    # chart.change_size_w(True)
    # chart.plot_a_function_of_one_variable("x^3-6*x^2+4*x+12", None, None, None, None, True)
    # chart.change_size_w(True)
    # chart.plot_a_function_of_one_variable("x^3-6*x^2+4*x+12", None, None, None, None, True)
    # chart.plot_a_function_of_one_variable("sin(x)+5+x^2", -20, 20, False)
    # chart.plot_a_several_function(-10, 10, -3, 3, False, 'sin(x)', 'cos(x)', 'tg(x)')
    # chart.change_size_w(True)
    # chart.plot_a_several_function(None, None, None, None, False, 'sin(x)', 'cos(x)', 'tg(x)')
    # chart.change_size_w(True)
    # chart.plot_a_several_function(None, None, None, None, False, 'sin(x)', 'cos(x)', 'tg(x)')
    # chart.plot_a_function_on_a_logarithmic_scale('e^x-x', -10, 10, True)
    # chart.change_size_w(True)
    # chart.plot_a_function_on_a_logarithmic_scale('e^x-x', None, None, True)
    # chart.change_size_w(True)
    # chart.plot_a_function_on_a_logarithmic_scale('e^x-x', None, None, True)
    # chart.change_size_w(True)
    # chart.plot_a_function_on_a_logarithmic_scale('e^x-x', None, None, True)
    # chart.change_size_w(True)
    # chart.plot_a_function_on_a_logarithmic_scale('e^x-x', None, None, True)
    # plot = chart.plot_function_with_two_variables("sin(x)*cos(y)", chart.start_x, chart.stop_x, chart.start_y, chart.stop_y, True)
    # show_figure(plot)
    # plot.show()
# chart.change_size_x(False)
# chart.plot_function_with_two_variables("2*sin(x)**2 - x*y**2 + 2*y**2", None, None, None, None, True)
# chart.change_size_x(False)
# chart.plot_function_with_two_variables("2*sin(x)**2 - x*y**2 + 2*y**2", None, None, None, None, True)
# chart.change_size_y(False)
# chart.plot_function_with_two_variables("2*sin(x)**2 - x*y**2 + 2*y**2", None, None, None, None, True)
# chart.change_size_y(False)
# chart.plot_function_with_two_variables("2*sin(x)**2 - x*y**2 + 2*y**2", None, None, None, None, True)
