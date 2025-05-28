import numpy as np
import sympy as sp


def vandermonde(X, Y):
    # Matriz de Vandermonde
    V = np.vander(X)

    # Resolver el sistema para encontrar los coeficientes
    b = Y
    V_inv = np.linalg.inv(V)

    # Formula
    coeficientes = V_inv @ b  # -> x^4 + x^3 + x^2 + x^1 + x^0

    return coeficientes


def newton(x_vals, y_vals):
    x = sp.Symbol('x')
    n = len(x_vals)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y_vals

    # Calcular la tabla de diferencias divididas
    for col in range(1, n):
        for fila in range(col, n):
            tabla[fila][col] = (tabla[fila][col - 1] - tabla[fila - 1][col - 1]) / (x_vals[fila] - x_vals[fila - col])

    coef = tabla.diagonal()

    # Construir el polinomio de Newton simbólicamente (ordenado)
    polinomio = coef[0]
    for i in range(1, n):
        terminos = 1
        for j in range(i):
            terminos *= (x - x_vals[j])
        polinomio += coef[i] * terminos

    # Expandir el polinomio a forma estándar
    polinomio_expandido = sp.expand(polinomio)

    return coef, polinomio, polinomio_expandido


def lagrange(x_vals, y_vals):
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
    return polinomio, polinomio_expandido


def spline_lineal(x_vals, y_vals):
    n = len(x_vals)
    tramos = []

    for i in range(n - 1):
        x0, x1 = x_vals[i], x_vals[i + 1]
        y0, y1 = y_vals[i], y_vals[i + 1]

        # Pendiente (m) y ordenada (b)
        m = (y1 - y0) / (x1 - x0)
        b = y0 - m * x0

        tramos.append((x0, x1, m, b))  # Guardamos el intervalo y la ecuación

    return tramos


def spline_cubico(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

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

    splines = []
    for i in range(n - 1):
        # Cada spline: S(x) = a + b*(x - x_i) + c*(x - x_i)^2 + d*(x - x_i)^3
        coef = (a[i], b[i], c[i], d[i])
        intervalo = (x[i], x[i + 1])
        splines.append((intervalo, coef))

    return splines


# Datos (corregidos)
X = np.array([1, 1.2, 1.4, 1.6, 1.8, 2])
Y = np.array([0.6747, 0.8491, 1.1214, 1.4921, 1.9607, 2.5258])

# a3, a2, a1, a0
coeficientes = vandermonde(X, Y)
print("coeficientes Vandermonde:", coeficientes)

coeficientes, polinomio, polinomio_expandido = newton(X, Y)
print("\ncoeficientes Newton:", coeficientes)
print("Polinomio Newton:", polinomio)
print("Polinomio Newton Expandido:", polinomio_expandido)

polinomio, polinomio_expandido = lagrange(X, Y)
print("\nPolinomio Lagrange:", polinomio)
print("Polinomio Lagrange Expandido:", polinomio_expandido)

"""# Crear polinomio como función para evaluar
def evaluar_polinomio(coefs, x):
    resultado = 0
    for i, coef in enumerate(coefs):
        resultado += coef * (x ** (len(coefs) - i - 1))
    return resultado


# Evaluar en punto específico
punto_eval = 33
valor_punto = evaluar_polinomio(coeficientes, punto_eval)
print(f"\nP({punto_eval}) = {valor_punto:.6f}")
"""
