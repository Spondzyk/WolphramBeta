import sympy as sym
from sympy import *


# klasa umozliwiajaca oblicznie wyrazen analizy matematycznej z pomoca biblioteki sympy
class CalculusAndAnalysis:
    # slownik pozwalajacy na refactoring stringa do postaci formuly przyjmowalnej przez sympy
    replacements = {
        'tg': 'tan',
        '^': '**',
        'e': 'E',
        'Exp': 'exp'
    }

    # tablica wyrazen uzywanych w przyapdku dzialan matematycznych
    math_operation = ['sin', 'cos', 'tg', 'log', 'log10', 'ln', '+', '-', '*', '/', 'sqrt', '^', 'abs', 'exp', 'e', '(',
                      ')', '[', ']']

    # metoda wykonujaca refactoring dostarczonej formuły z postaci napisu na postac akceptowalna przez
    # biblioteke sympy z uzyciem wczesniej zdefiniowanego slownika zamiennikow
    @staticmethod
    def refactor_formula(formula):
        new_formula = formula
        for old, new in CalculusAndAnalysis.replacements.items():
            new_formula = new_formula.replace(old, new)
        return new_formula

    # metoda zajmujaca sie wylonieniem symboli wystepujacych w formule - przydatne w przypadku obliczania pochodnej,
    # moze byc ona obliczona po kazdej zmiennej bedacej litera
    @staticmethod
    def get_symbols(formula):
        variables = formula
        for op in CalculusAndAnalysis.math_operation:
            variables = variables.replace(op, ' ')

        var_list = variables.split()
        result = []
        for vr in var_list:
            if vr.isalpha():
                result.append(vr)
            elif vr.isdigit():
                pass
            else:
                return 'symbol {} nie moze byc zmienna'.format(vr)
        return sorted(list(set(result)))

    # metoda sluzaca do obliczania pochodnej z wyrazenia funkcji po konkretnej zmiennej
    @staticmethod
    def differentiation(formula, symbol):
        # sprawdzenie ktore zmienne wystepuja w formule
        get_var = CalculusAndAnalysis.get_symbols(formula)
        # przypisanie warosci char do zmiennych globalnych o tej samej nazwie
        if not isinstance(get_var, str):
            for i in range(len(get_var)):
                val = str(get_var[i])
                globals()[val] = symbols(get_var[i])
            # refactoring formuly
            expression = CalculusAndAnalysis.refactor_formula(formula)
            try:
                # przetworzenie formuly na zapis matematyczny
                derivative = eval(expression)
                # wyliczenie wyniku dzialania funckji
                result = diff(derivative, symbol)
                replaced_result = str(result)
                # zamiana wyrazen matemtycznych na jezyk wolphramalpha
                for key, value in CalculusAndAnalysis.replacements.items():
                    if value in replaced_result:
                        replaced_result = replaced_result.replace(value, key)
                    else:
                        pass
                return replaced_result
            except SyntaxError:
                return "syntax error"
            except NameError:
                return "name error"
            except TypeError:
                return "type error"
            except ZeroDivisionError:
                return "zero division error"
        else:
            return "Nieprawidłowa formuła, zmienną musi być litera"

    # metoda sluzaca do obliczania calki pojedynczej z wyrazenia funkcji zmiennej x
    @staticmethod
    def integration(formula, symbol, s_limit=None, e_limit=None):
        # refactoring formuly
        expression = CalculusAndAnalysis.refactor_formula(formula)
        # przypisanie zmiennej do etykiety x
        x = sym.symbols('x')
        # jesli mamy jakis inny symbol niz x to blad
        if symbol != 'x':
            return "Błędny symbol, musi być x"
        else:
            try:
                # zamienienie granicy calkowania na te dopuszczalne przez biblioteke sympy
                if s_limit is not None and e_limit is not None:
                    if s_limit == 'inf' or s_limit == 'oo':
                        s_limit = sym.oo
                    elif e_limit == 'inf' or e_limit == 'oo':
                        e_limit = sym.oo
                    elif s_limit == '-inf' or s_limit == '-oo':
                        s_limit = -sym.oo
                    elif e_limit == '-inf' or e_limit == '-oo':
                        e_limit = -sym.oo

                    # wyliczenie wyniku calki oznaczonej
                    integral = integrate(eval(expression), (symbol, s_limit, e_limit))
                    return integral
                elif s_limit is None and e_limit is None:
                    # wyliczenie wyniku calki nieoznaczonej
                    integral = integrate(eval(expression), (symbol, s_limit, e_limit))
                    return integral
                else:
                    # blad granic calkowania
                    return "Nieprawidłowe granice całki"
            except SyntaxError:
                return "syntax error"
            except NameError:
                return "name error"
            except TypeError:
                return "type error"
            except ZeroDivisionError:
                return "zero division error"

    # metoda sluzaca do obliczania calki podwojnej z wyrazenia funkcji zmiennej x i/lub y
    @staticmethod
    def dual_integration(formula, symbol1, symbol2, s_limit1=None, e_limit1=None, s_limit2=None, e_limit2=None):
        expression = CalculusAndAnalysis.refactor_formula(formula)
        # przypisanie zmiennych do etykiety x oraz y
        x, y = sym.symbols('x y')
        # jesli mamy jakis inny symbol niz x lub y to blad
        if symbol1 != 'x' and symbol1 != 'y':
            return "Błędny symbol 1, musi być x lub y"
        elif symbol2 != 'x' and symbol2 != 'y':
            return "Błędny symbol 2, musi być x lub y"
        else:
            try:
                # zamienienie obu granicy calkowania na te dopuszczalne przez biblioteke sympy
                if s_limit1 is not None and e_limit1 is not None and s_limit2 is not None and e_limit2 is not None:
                    if s_limit1 == 'inf' or s_limit1 == 'oo':
                        s_limit1 = sym.oo
                    elif e_limit1 == 'inf' or e_limit1 == 'oo':
                        e_limit1 = sym.oo
                    elif s_limit1 == '-inf' or s_limit1 == '-oo':
                        s_limit1 = -sym.oo
                    elif e_limit1 == '-inf' or e_limit1 == '-oo':
                        e_limit1 = -sym.oo
                    elif s_limit2 == 'inf' or s_limit2 == 'oo':
                        s_limit2 = sym.oo
                    elif e_limit2 == 'inf' or e_limit2 == 'oo':
                        e_limit2 = sym.oo
                    elif s_limit2 == '-inf' or s_limit2 == '-oo':
                        s_limit1 = -sym.oo
                    elif e_limit2 == '-inf' or e_limit2 == '-oo':
                        e_limit2 = -sym.oo
                    # wyliczenie wyniku calki oznaczonej
                    integral = integrate(eval(expression), (symbol1, s_limit1, e_limit1), (symbol2, s_limit2, e_limit2))
                    return integral
                elif s_limit1 is None and e_limit1 is None and s_limit2 is None and e_limit2 is None:
                    # wyliczenie wyniku calki nieoznaczonej
                    integral = integrate(eval(expression), (symbol1, s_limit1, e_limit1), (symbol2, s_limit2, e_limit2))
                    return integral
                else:
                    # blad granic calkowania
                    return "Nieprawidłowe granice całki"
            except SyntaxError:
                return "syntax error"
            except NameError:
                return "name error"
            except TypeError:
                return "type error"
            except ZeroDivisionError:
                return "zero division error"

    # metoda sluzaca do obliczania granicyz wyrazenia funkcji zmiennej x
    @staticmethod
    def limits(formula, symbol, e_limit=None, side=None):
        # refactoring formuly
        expression = CalculusAndAnalysis.refactor_formula(formula)
        # przypisanie zmiennej do etykiety x
        x = sym.symbols('x')
        # jesli punkt graniczny jest pusty wtedy blad
        if e_limit is None:
            return "Nieprawidłowy punkt zbieżności"
        else:
            # zamienienie punktu granicznego na te dopuszczalne przez biblioteke sympy
            if e_limit == 'inf' or e_limit == 'oo':
                e_limit = sym.oo
            elif e_limit == '-inf' or e_limit == '-oo':
                e_limit = -sym.oo
            try:
                if symbol != 'x':
                    return "Błędny symbol, musi być x"
                else:
                    # jesli nie ma okreslonej strony z ktorej obliczamy granice
                    if side is None:
                        # obliczamy granice
                        limit_r = limit(eval(expression), symbol, e_limit)
                        return limit_r
                    # jesli jest okreslona storna z ktorej obliczamy granice
                    elif side == '+' or side == '-':
                        # obliczamy granice
                        limit_r = limit(eval(expression), symbol, e_limit, side)
                        return limit_r
                    # jesli wprowadzono nieprawidlowy symbol
                    else:
                        return "Błędny znak strony"
            except SyntaxError:
                return "syntax error"
            except NameError:
                return "name error"
            except TypeError:
                return "type error"
            except ZeroDivisionError:
                return "zero division error"
