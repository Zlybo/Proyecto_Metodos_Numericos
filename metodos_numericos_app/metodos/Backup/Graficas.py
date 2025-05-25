import io
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify, Symbol, diff
from latex2sympy2 import latex2sympy


def generar_grafico(funcion_str, a, b):
    x = Symbol('x')
    funcion = sympify(latex2sympy(funcion_str))
    derivada = diff(funcion, x)

    f = lambdify(x, funcion, 'numpy')
    f_der = lambdify(x, derivada, 'numpy')

    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)
    dy_vals = f_der(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_vals, dy_vals, label="f'(x)", color='red', linestyle='--')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.title('Función y su Derivada')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer.getvalue()  # bytes listos para enviar como imagen
