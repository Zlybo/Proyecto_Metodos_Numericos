import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def newton_interpolante(x_str, y_str):
    x_vals = x_str
    y_vals = y_str

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


def polinomio_newton(coef, x_vals):
    terminos = []
    for i in range(len(coef)):
        term = f"{coef[i]}"
        for j in range(i):
            term += f"*(x - {x_vals[j]})"
        terminos.append(term)
    return " + ".join(terminos)


def graficar_polinomio(polinomio_str, x_vals, y_vals, titulo=""):
    x = sp.Symbol('x')
    # Convertir el string a expresión simbólica
    polinomio_expr = sp.sympify(polinomio_str.replace("^", "**"))

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


x_str = "1,2,3,4"
y_str = "1,4,9,16"

# Polinomio de Newton
polinomio, polinomio_expandido = newton_interpolante(x_str, y_str)
x_vals = np.array(x_str.split(','), dtype=float)
y_vals = np.array(y_str.split(','), dtype=float)

graficar_polinomio(polinomio_expandido, x_vals, y_vals, titulo="Interpolación de Newton")
