import numpy as np


def lagrange(x, y):
    n = len(x)
    tabla = np.zeros((n, n))

    for i in range(n):
        Li = np.array([1.0])  # Polinomio 1
        den = 1.0

        for j in range(n):
            if j != i:
                # Multiplicar Li por (x - xj)
                paux = [1.0, -x[j]]
                Li = np.convolve(Li, paux)
                den *= (x[i] - x[j])

        tabla[i, :len(Li)] = y[i] * Li / den

    # Sumar todas las filas para obtener el polinomio final
    pol = np.sum(tabla, axis=0)
    return pol  # Coeficientes desde x^n a x^0


# Ejemplo de uso
x_vals = np.array([1, 2, 3, 4, 5])
y_vals = np.array([10, 5, 0, 12, 9])

coeficientes = lagrange(x_vals, y_vals)
print("Coeficientes del polinomio (de mayor a menor grado):")
print(coeficientes)
