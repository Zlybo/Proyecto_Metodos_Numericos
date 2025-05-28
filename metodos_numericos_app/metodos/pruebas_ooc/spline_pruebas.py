import numpy as np
import matplotlib.pyplot as plt


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


def evaluar_spline(x, tramos):
    y = np.zeros_like(x)
    for (x0, x1, m, b) in tramos:
        mask = (x >= x0) & (x <= x1)
        y[mask] = m * x[mask] + b
    return y


def graficar_tramos_lineal(tramos, x_vals, titulo=""):
    print("tramos", tramos)
    print('x_vals', x_vals)
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
    plt.show()


x_str = "1.5, 8.5, 22, 35"
y_str = "0, 9, 28, 26"
tramos, polinomios = spline_lineal(x_str, y_str)

print(tramos)
print(polinomios)
graficar_tramos_lineal(tramos, x_str)
