from sympy import sympify, lambdify
from latex2sympy2 import latex2sympy
import numpy as np
import sympy as sp


def polinomio_vandermonde(data):
    polinomio = ""
    n = len(data)

    for i in range(n):
        coeficiente = data[i]
        grado = n - i - 1
        polinomio += f"{coeficiente}*x^{grado} + "

    polinomio = polinomio.rstrip(" +")
    return polinomio


def polinomio_newton(coef, x_vals):
    terminos = []
    for i in range(len(coef)):
        term = f"{coef[i]}"
        for j in range(i):
            term += f"*(x - {x_vals[j]})"
        terminos.append(term)
    return " + ".join(terminos)


def vandermonde(x_str, y_str):
    X = np.array(x_str.split(','), dtype=float)
    Y = np.array(y_str.split(','), dtype=float)

    # Matriz de Vandermonde
    V = np.vander(X)

    # Resolver el sistema para encontrar los coeficientes
    b = Y
    V_inv = np.linalg.inv(V)

    # Formula
    coeficientes = V_inv @ b  # -> x^4 + x^3 + x^2 + x^1 + x^0
    polinomio = polinomio_vandermonde(coeficientes.tolist())
    return polinomio


def newton_interpolante(x_str, y_str):
    x_vals = np.array(x_str.split(','), dtype=float)
    y_vals = np.array(y_str.split(','), dtype=float)

    x = sp.Symbol('x')
    n = len(x_vals)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y_vals

    # Calcular la tabla de diferencias divididas
    for col in range(1, n):
        for fila in range(col, n):
            tabla[fila][col] = (tabla[fila][col - 1] - tabla[fila - 1][col - 1]) / (x_vals[fila] - x_vals[fila - col])

    coeficientes = tabla.diagonal()

    # Construir el polinomio de Newton simbólicamente
    polinomio = coeficientes[0]
    for i in range(1, n):
        terminos = 1
        for j in range(i):
            terminos *= (x - x_vals[j])
        polinomio += coeficientes[i] * terminos

    # Expandir el polinomio a forma estándar
    polinomio_expandido = sp.expand(polinomio)
    polinomio = polinomio_newton(coeficientes, x_vals)

    return str(polinomio), str(polinomio_expandido).replace("**", "^")


def lagrange(x_str, y_str):
    x_vals = np.array(x_str.split(','), dtype=float)
    y_vals = np.array(y_str.split(','), dtype=float)

    x = sp.Symbol('x')
    n = len(x_vals)
    polinomio = 0

    for i in range(n):
        # Construir el término de Lagrange L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])

        polinomio += y_vals[i] * L_i

    polinomio_expandido = sp.expand(polinomio)
    return str(polinomio), str(polinomio_expandido).replace("**", "^")


def spline_lineal(x_str, y_str):
    x_vals = np.array(x_str.split(','), dtype=float)
    y_vals = np.array(y_str.split(','), dtype=float)

    n = len(x_vals)
    tramos = []

    for i in range(n - 1):
        x0, x1 = x_vals[i], x_vals[i + 1]
        y0, y1 = y_vals[i], y_vals[i + 1]

        # Pendiente (m) y ordenada (b)
        m = (y1 - y0) / (x1 - x0)
        b = y0 - m * x0

        tramos.append((x0, x1, m, b))  # Guardamos el intervalo y la ecuación

    # Imprimir polinomios
    polinomios = []
    for i, (x0, x1, m, b) in enumerate(tramos):
        polinomios_str = f"Polinomio tramo {i + 1} para x en [{x0}, {x1}]:"
        polinomios_str += f"  S_{i}(x) = {m}x + {b}"
        polinomios.append(polinomios_str)

    return tramos, polinomios


def imprimir_spline_cubico(splines):
    polinomios = []
    for i, ((x0, x1), (a, b, c, d)) in enumerate(splines):
        polinomio_str = f"Tramo {i + 1}: x ∈ [{x0}, {x1}]"
        polinomio_str += f"S_{i}(x) = {a:.4f} + {b:.4f}(x - {x0}) + {c:.4f}(x - {x0})**2 + {d:.4f}(x - {x0})**3"
        polinomios.append(polinomio_str)
    return polinomios


def spline_cubico(x_str, y_str):
    x = np.array(x_str.split(','), dtype=float)
    y = np.array(y_str.split(','), dtype=float)

    n = len(x)
    h = np.diff(x)
    b = np.diff(y) / h

    # Construimos el sistema tridiagonal
    A = np.zeros((n, n))
    rhs = np.zeros(n)

    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        rhs[i] = 3 * (b[i] - b[i - 1])

    c = np.linalg.solve(A, rhs)

    a = y[:-1]
    d = (c[1:] - c[:-1]) / (3 * h)
    b = (y[1:] - y[:-1]) / h - h * (2 * c[:-1] + c[1:]) / 3

    tramos = []
    for i in range(n - 1):
        # Cada spline: S(x) = a + b*(x - x_i) + c*(x - x_i)^2 + d*(x - x_i)^3
        coef = (a[i], b[i], c[i], d[i])
        intervalo = (x[i], x[i + 1])
        tramos.append((intervalo, coef))

    polinomios = []
    for i, ((x0, x1), (a, b, c, d)) in enumerate(tramos):
        polinomio_str = f"Tramo {i + 1}: x ∈ [{x0}, {x1}]"
        polinomio_str += f"S_{i}(x) = {a:.4f} + {b:.4f}(x - {x0}) + {c:.4f}(x - {x0})**2 + {d:.4f}(x - {x0})**3"
        polinomios.append(polinomio_str)

    return tramos, polinomios
