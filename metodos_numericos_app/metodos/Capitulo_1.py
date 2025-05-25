from sympy import sympify, lambdify, diff
from latex2sympy2 import latex2sympy


def calcular_precision_RSBD(error, base):
    exponente = 0
    while error <= base * 10 ** -exponente:
        exponente += 1
    return max(exponente - 1, 0)  # Aseguramos que nunca sea negativo


def biseccion(funcion_str, a, b, tolerancia, max_iter):
    f_expr = sympify(latex2sympy(funcion_str))
    f = lambdify('x', f_expr, 'math')  # convierte en funcion evaluable con floats

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_m = (a + b) / 2  # Formula de la biseccion
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


def punto_fijo(funcion_str, funcion_g_str, x_0, tolerancia, max_iter):
    f_expr = sympify(latex2sympy(funcion_str))
    f = lambdify('x', f_expr, 'math')

    g_expr = sympify(latex2sympy(funcion_g_str))
    g = lambdify('x', g_expr, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = g(x_0)
        error = abs(x_next - x_0)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next,
            "f_x": f(x_next),
            "error": error
        })

        if f(x_next) == 0:
            break

        x_0 = x_next
        iteracion += 1

    return tabla


def newton(funcion_str, x_0, tolerancia, max_iter):
    f_expr = sympify(latex2sympy(funcion_str))
    f = lambdify('x', f_expr, 'math')

    f_derivada = diff(f_expr)
    f_d = lambdify('x', f_derivada, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = x_0 - f(x_0) / f_d(x_0)
        error = abs(x_next - x_0)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next,
            "f_x": f(x_next),
            "error": error
        })

        if f(x_next) == 0:
            break

        x_0 = x_next
        iteracion += 1
    return tabla


def secante(funcion_str, x_0, x_1, tolerancia, max_iter):
    f_expr = sympify(latex2sympy(funcion_str))
    f = lambdify('x', f_expr, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))
        error = abs(x_next - x_1)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next,
            "f_x": f(x_next),
            "error": error
        })

        if f(x_next) == 0:
            break

        x_0, x_1 = x_1, x_next
        iteracion += 1
    return tabla


def raices_multiples(funcion_str, x_0, tolerancia, max_iter):
    f_expr = sympify(latex2sympy(funcion_str))
    f = lambdify('x', f_expr, 'math')

    f_derivada = diff(f_expr)
    f_d = lambdify('x', f_derivada, 'math')

    f_segunda_derivada = diff(f_derivada)
    f_segunda_d = lambdify('x', f_segunda_derivada, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = x_0 - f(x_0) * f_d(x_0) / (f_d(x_0) ** 2 - f(x_0) * f_segunda_d(x_0))
        error = abs(x_next - x_0)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next,
            "f_x": f(x_next),
            "error": error
        })

        if f(x_next) == 0:
            break

        x_0 = x_next
        iteracion += 1
    return tabla
