import numpy as np


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

    splines = []
    for i in range(n - 1):
        # Cada spline: S(x) = a + b*(x - x_i) + c*(x - x_i)^2 + d*(x - x_i)^3
        coef = (a[i], b[i], c[i], d[i])
        intervalo = (x[i], x[i + 1])
        splines.append((intervalo, coef))

    polinomios = []
    for i, ((x0, x1), (a, b, c, d)) in enumerate(splines):
        polinomio_str = f"Tramo {i + 1}: x ∈ [{x0}, {x1}]"
        polinomio_str += f"S_{i}(x) = {a:.4f} + {b:.4f}(x - {x0}) + {c:.4f}(x - {x0})**2 + {d:.4f}(x - {x0})**3"
        polinomios.append(polinomio_str)

    return splines, polinomios


import matplotlib.pyplot as plt


def graficar_spline_cubico(tramos, puntos_x, puntos_y, titulo="Spline Cúbico"):
    puntos_x = np.array(puntos_x.split(','), dtype=float)
    puntos_y = np.array(puntos_y.split(','), dtype=float)

    x_plot = []
    y_plot = []

    for (x0, x1), (a, b, c, d) in tramos:
        x_vals = np.linspace(x0, x1, 100)
        x_shift = x_vals - x0
        y_vals = a + b * x_shift + c * x_shift ** 2 + d * x_shift ** 3

        x_plot.extend(x_vals)
        y_plot.extend(y_vals)

    # Graficar
    plt.plot(x_plot, y_plot, label="Spline cúbico", color="blue")
    plt.scatter(puntos_x, puntos_y, color='red', zorder=5, label="Puntos originales")

    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()


x_str = "1.5, 8.5, 22, 35"
y_str = "0, 9, 28, 26"

tramos, polinomios = spline_cubico(x_str, y_str)
print(tramos)
print(polinomios)

graficar_spline_cubico(tramos, x_str, y_str)
