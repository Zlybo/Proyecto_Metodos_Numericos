import numpy as np

def imprimir_spline_cubico(splines):
    for i, ((x0, x1), (a, b, c, d)) in enumerate(splines):
        print(f"Tramo {i+1}: x ∈ [{x0}, {x1}]")
        print(f"S_{i}(x) = {a:.4f} + {b:.4f}(x - {x0}) + {c:.4f}(x - {x0})² + {d:.4f}(x - {x0})³\n")


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

    return splines


x_str = "1.5, 8.5, 22, 35"
y_str = "0, 9, 28, 26"

tramos = spline_cubico(x_str, y_str)

imprimir_spline_cubico(tramos)