import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


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


def graficar_polinomio(polinomio_str, x_vals, y_vals, titulo=""):
    x_vals = np.array(x_vals.split(','), dtype=float)
    y_vals = np.array(y_vals.split(','), dtype=float)

    x = sp.Symbol('x')
    # Convertir el string a expresión simbólica
    polinomio_expr = sp.sympify(polinomio_str)

    # Crear una función evaluable con lambdify
    f = sp.lambdify(x, polinomio_expr, modules=["numpy"])

    # Crear puntos para la curva del polinomio
    x_min, x_max = min(x_vals), max(x_vals)
    x_plot = np.linspace(x_min - 1, x_max + 1, 400)
    y_plot = f(x_plot)

    # Graficar la curva
    plt.plot(x_plot, y_plot, label="Polinomio interpolante")
    plt.scatter(x_vals, y_vals, color='red', zorder=5, label="Puntos originales")
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()


x_str = "1.5, 8.5, 22, 35"
y_str = "0, 9, 28, 26"

polinomio_vander = vandermonde(x_str, y_str)
print(polinomio_vander)
polinomio, expandido = newton_interpolante(x_str, y_str)
print('Newton:', polinomio)
print('Expandido', expandido)

graficar_polinomio(polinomio_vander, x_str, y_str)

graficar_polinomio(expandido, x_str, y_str)
