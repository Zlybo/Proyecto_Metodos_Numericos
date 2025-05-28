import numpy as np
from scipy.interpolate import CubicSpline


def cubic_spline_scipy(points, interval):
    # Extraer coordenadas
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    # Calcular el spline cúbico
    cs = CubicSpline(x, y, bc_type='natural')

    # Encontrar el índice del segmento que corresponde al intervalo
    for i in range(len(x) - 1):
        if x[i] <= interval[0] <= x[i + 1]:
            segment = i
            break

    # Los coeficientes en CubicSpline están almacenados como:
    # cs.c[3, i] + cs.c[2, i] * (x - x[i]) + cs.c[1, i] * (x - x[i])^2 + cs.c[0, i] * (x - x[i])^3
    # Necesitamos convertirlos a la forma estándar: a*x^3 + b*x^2 + c*x + d

    # Obtener los coeficientes para el segmento
    a, b, c, d = cs.c[:, segment]

    # Punto inicial del segmento
    xi = x[segment]

    # Convertir a la forma estándar (expandiendo (x - xi) términos)
    # Siempre es de grado 3, por eso se llama cubico
    coef_x3 = a
    coef_x2 = -3 * a * xi + b
    coef_x1 = 3 * a * xi ** 2 - 2 * b * xi + c
    coef_x0 = -a * xi ** 3 + b * xi ** 2 - c * xi + d

    return [coef_x3, coef_x2, coef_x1, coef_x0]


# Datos del problema
points = [(1, 3.21), (1.1, 3.64), (1.2, 4.11)]
interval = (1, 1.1)

# Obtener coeficientes
coefs = cubic_spline_scipy(points, interval)
polynomial = f"{coefs[0]:.2f}x^3 + {coefs[1]:.2f}x^2 + {coefs[2]:.2f}x + {coefs[3]:.2f}"
print(polynomial)
