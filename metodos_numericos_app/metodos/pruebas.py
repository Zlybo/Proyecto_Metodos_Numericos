from sympy import sympify, lambdify, diff


def calcular_precision_RSBD(error, base):
    exponente = 0
    while error <= base * 10 ** -exponente:
        exponente += 1
    return max(exponente - 1, 0)  # Aseguramos que nunca sea negativo


def biseccion(f_str, a, b, tolerancia, max_iter):
    f_expr = sympify(f_str)
    f = lambdify('x', f_expr, 'math')  # convierte en función evaluable con floats

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_m = (a + b) / 2
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


def regla_falsa(funcion_str, a, b, tol=0.5e-6, max_iter=10):
    f_expr = sympify(funcion_str)
    f = lambdify('x', f_expr, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tol:
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


def punto_fijo(funcion_str, tolerancia, max_iter, funcion_g_str, x_0):
    f_expr = sympify(funcion_str)
    f = lambdify('x', f_expr, 'math')

    g_expr = sympify(funcion_g_str)
    g = lambdify('x', g_expr, 'math')

    tabla = []
    error = 100  # Error inicial alto
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
    f_expr = sympify(funcion_str)
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
    f_expr = sympify(funcion_str)
    f = lambdify('x', f_expr, 'math')

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        if f(x_1) - f(x_0) == 0:
            break  # Division por cero

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


tabla = secante('cos(x)-x', 1, 2, 0.5e-6, 100)
for _ in tabla:
    print(_)

"""tabla = newton('cos(x)-x', 1, 0.5e-6, 100)
for _ in tabla:
    print(_)"""

"""tabla = punto_fijo('cos(x) - x', 0.5e-6, 100, 'cos(x)', 0.5)
for _ in tabla:
    print(_)"""
"""tabla = regla_falsa('x**3 - x - 2', 1, 2, 0.005, 100)
for _ in tabla:
    print(_)"""
