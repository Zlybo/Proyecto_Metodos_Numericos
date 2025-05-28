import io
import numpy as np
from sympy import sympify, lambdify, Symbol, diff
from latex2sympy2 import latex2sympy
import matplotlib
import sympy as sp

matplotlib.use('Agg')  # AL ser un backend, no necesita GUI (Da erorres de buffer al quitarlo)
import matplotlib.pyplot as plt


def graficar_intervalos(funcion_str, a, b, x_m):
    x = Symbol('x')
    funcion = sympify(latex2sympy(funcion_str))
    f = lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.scatter(x_m, 0, label=f'Raíz: {x_m}')
    plt.axvline(x=a, color='red')
    plt.axvline(x=b, color='red')

    plt.title('Intervalos: Función y su raíz')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()  # bytes listos para enviar como imagen


def graficar_punto_fijo(funcion_str, funcion_g_str, x_n):
    x = Symbol('x')
    funcion = sympify(latex2sympy(funcion_str))
    f = lambdify(x, funcion, 'numpy')

    funcion_g = sympify(latex2sympy(funcion_g_str))
    g = lambdify(x, funcion_g, 'numpy')

    x_vals = np.linspace(x_n - 1, x_n + 1, 400)
    y_vals = f(x_vals)
    g_vals = g(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_vals, g_vals, label='g(x)', color='red')
    plt.plot(x_vals, x_vals, label='x', color='green')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.scatter(x_n, 0, label=f'Raíz: {x_n}')

    plt.title('Punto Fijo: Función y su raíz')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()  # bytes listos para enviar como imagen


def graficar_newton(funcion_str, x_n):
    x = Symbol('x')
    funcion = sympify(latex2sympy(funcion_str))
    f = lambdify(x, funcion, 'numpy')

    funcion_deriv_str = diff(funcion)
    f_deriv = lambdify(x, funcion_deriv_str, 'numpy')

    x_vals = np.linspace(x_n - 1, x_n + 1, 400)
    y_vals = f(x_vals)
    y_deriv_vals = f_deriv(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_vals, y_deriv_vals, label="f'(x)", color='red')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.scatter(x_n, 0, label=f'Raíz: {x_n}')

    plt.title('Newton: Función y su raíz')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()  # bytes listos para enviar como imagen


def graficar_secante(funcion_str, x_n):
    x = Symbol('x')
    funcion = sympify(latex2sympy(funcion_str))
    f = lambdify(x, funcion, 'numpy')

    funcion_deriv_str = diff(funcion)
    f_deriv = lambdify(x, funcion_deriv_str, 'numpy')

    x_vals = np.linspace(x_n - 1, x_n + 1, 400)
    y_vals = f(x_vals)
    y_deriv_vals = f_deriv(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_vals, y_deriv_vals, label="f'(x)", color='red')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.scatter(x_n, 0, label=f'Raíz: {x_n}')

    plt.title('Secante: Función y su raíz')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()  # bytes listos para enviar como imagen


def graficar_raices_multiples(funcion_str, x_n):
    x = Symbol('x')
    funcion = sympify(latex2sympy(funcion_str))
    f = lambdify(x, funcion, 'numpy')

    funcion_deriv_str = diff(funcion)
    f_deriv = lambdify(x, funcion_deriv_str, 'numpy')

    funcion_segunda_deriv_str = diff(funcion_deriv_str)
    f_segunda_deriv = lambdify(x, funcion_segunda_deriv_str, 'numpy')

    x_vals = np.linspace(x_n - 1, x_n + 1, 400)
    y_vals = f(x_vals)
    y_deriv_vals = f_deriv(x_vals)
    y_segunda_deriv_vals = f_segunda_deriv(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_vals, y_deriv_vals, label="f'(x)", color='red')
    plt.plot(x_vals, y_segunda_deriv_vals, label="f''(x)", color='green')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.scatter(x_n, 0, label=f'Raíz: {x_n}')

    plt.title('Raices Multiples: Función y su raíz')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()  # bytes listos para enviar como imagen


def graficar_polinomio(polinomio_str, x_vals, y_vals, titulo=""):
    x_vals = np.array(x_vals.split(','), dtype=float)
    y_vals = np.array(y_vals.split(','), dtype=float)

    x = sp.Symbol('x')
    # Convertir el string a expresión simbólica
    polinomio_expr = sympify(polinomio_str)

    # Crear una función evaluable con lambdify
    f = lambdify(x, polinomio_expr, modules=["numpy"])

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

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return buffer.getvalue()  # bytes listos para enviar como imagen


def evaluar_spline(x, tramos):
    y = np.zeros_like(x)
    for (x0, x1, m, b) in tramos:
        mask = (x >= x0) & (x <= x1)
        y[mask] = m * x[mask] + b
    return y


def graficar_tramos_lineal(tramos, x_vals, titulo=""):
    # Agrupar cada 4 elementos en una tupla, ya que se pierde el formato al llegar del html
    numeros = list(map(float, tramos.split(',')))
    tramos = [tuple(numeros[i:i + 4]) for i in range(0, len(numeros), 4)]

    x_vals = np.array(x_vals.split(','), dtype=float)
    y_vals = evaluar_spline(x_vals, tramos)

    # Crear rango de x para graficar
    x_plot = np.linspace(min(x_vals), max(x_vals), 500)
    y_plot = evaluar_spline(x_plot, tramos)

    # Graficar la curva
    plt.plot(x_plot, y_plot, label="Spline Lineal")
    plt.scatter(x_vals, y_vals, color='red', zorder=5, label="Puntos originales")
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return buffer.getvalue()  # bytes listos para enviar como imagen
