import sympy as sym
from sympy import *


class CalculusAndAnalysis:
    replacements = {
        'tg': 'tan',
        '^': '**',
        'e': 'E',
        'Exp': 'exp'
    }

    math_operation = ['sin', 'cos', 'tg', 'log', 'log10', 'ln', '+', '-', '*', '/', 'sqrt', '^', 'abs', 'exp', 'e', '(',
                      ')', '[', ']']

    @staticmethod
    def refactor_formula(formula):
        new_formula = formula
        for old, new in CalculusAndAnalysis.replacements.items():
            new_formula = new_formula.replace(old, new)
        return new_formula

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

    @staticmethod
    def differentiation(formula, symbol):
        get_var = CalculusAndAnalysis.get_symbols(formula)
        if not isinstance(get_var, str):
            for i in range(len(get_var)):
                val = str(get_var[i])
                globals()[val] = symbols(get_var[i])
            expression = CalculusAndAnalysis.refactor_formula(formula)
            try:
                derivative = eval(expression)
                result = diff(derivative, symbol)
                replaced_result = str(result)
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

    @staticmethod
    def integration(formula, symbol, s_limit=None, e_limit=None):
        expression = CalculusAndAnalysis.refactor_formula(formula)
        x = sym.symbols('x')
        if symbol != 'x':
            return "Błędny symbol, musi być x"
        else:
            try:
                if s_limit is not None and e_limit is not None:
                    if s_limit == 'inf' or s_limit == 'oo':
                        s_limit = sym.oo
                    elif e_limit == 'inf' or e_limit == 'oo':
                        e_limit = sym.oo
                    elif s_limit == '-inf' or s_limit == '-oo':
                        s_limit = -sym.oo
                    elif e_limit == '-inf' or e_limit == '-oo':
                        e_limit = -sym.oo
                    integral = integrate(eval(expression), (symbol, s_limit, e_limit))
                    return integral
                elif s_limit is None and e_limit is None:
                    integral = integrate(eval(expression), (symbol, s_limit, e_limit))
                    return integral
                else:
                    return "Nieprawidłowe granice całki"
            except SyntaxError:
                return "syntax error"
            except NameError:
                return "name error"
            except TypeError:
                return "type error"
            except ZeroDivisionError:
                return "zero division error"

    @staticmethod
    def dual_integration(formula, symbol1, symbol2, s_limit1=None, e_limit1=None, s_limit2=None, e_limit2=None):
        expression = CalculusAndAnalysis.refactor_formula(formula)
        x, y = sym.symbols('x y ')
        if symbol1 != 'x' and symbol1 != 'y' and symbol1 != 'z':
            return "Błędny symbol 1, musi być x lub y lub z"
        elif symbol2 != 'x' and symbol2 != 'y' and symbol2 != 'z':
            return "Błędny symbol 2, musi być x lub y lub z"
        else:
            try:
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
                    integral = integrate(eval(expression), (symbol1, s_limit1, e_limit1), (symbol2, s_limit2, e_limit2))
                    return integral
                elif s_limit1 is None and e_limit1 is None and s_limit2 is None and e_limit2 is None:
                    integral = integrate(eval(expression), (symbol1, s_limit1, e_limit1), (symbol2, s_limit2, e_limit2))
                    return integral
                else:
                    return "Nieprawidłowe granice całki"
            except SyntaxError:
                return "syntax error"
            except NameError:
                return "name error"
            except TypeError:
                return "type error"
            except ZeroDivisionError:
                return "zero division error"

    @staticmethod
    def limits(formula, symbol, e_limit=None, side=None):
        expression = CalculusAndAnalysis.refactor_formula(formula)
        x = sym.symbols('x')
        if e_limit is None:
            return "Nieprawidłowy punkt zbieżności"
        else:
            if e_limit == 'inf' or e_limit == 'oo':
                e_limit = sym.oo
            elif e_limit == '-inf' or e_limit == '-oo':
                e_limit = -sym.oo
            try:
                if symbol != 'x':
                    return "Błędny symbol, musi być x"
                else:
                    if side is None:
                        limit_r = limit(eval(expression), symbol, e_limit)
                        return limit_r
                    elif side == '+' or side == '-':
                        limit_r = limit(eval(expression), symbol, e_limit, side)
                        return limit_r
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


if __name__ == '__main__':
    math = CalculusAndAnalysis()
    print(math.differentiation("log(x) + 2", 'x'))
    # print(math.integration('x^2', 'x', 5, 10))
    # print(math.limits('sin(x)/(x)', 'x', 0))
    # print(math.limits('1/x', 'x', 0, '+'))
    # print(math.dual_integration('exp(-x**2 - y**2)', 'x', 'y', '-oo', 'oo', '-oo', 'oo'))
