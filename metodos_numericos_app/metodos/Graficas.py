import io
import numpy as np
from sympy import sympify, lambdify, Symbol, diff
from latex2sympy2 import latex2sympy
import matplotlib

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
