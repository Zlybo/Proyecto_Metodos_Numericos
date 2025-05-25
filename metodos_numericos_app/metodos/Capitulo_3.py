from sympy import sympify, lambdify
from latex2sympy2 import latex2sympy
import numpy as np


def regla_falsa(funcion_str, a, b, tolerancia, max_iter):
    f_expr = sympify(latex2sympy(funcion_str))
    f = lambdify('x', f_expr, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_m = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Formula de la Regla Falsa

        error = abs(x_m - a)

        tabla.append({
            "iter": iteracion + 1,
            "a": a,
            "b": b,
            "x_m": x_m,
            "error": error
        })

        if f(a) * f(x_m) < 0:
            b = x_m
        else:
            a = x_m

        iteracion += 1

    return tabla
