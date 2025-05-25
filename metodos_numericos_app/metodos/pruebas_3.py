import numpy as np


def vandermonde(X, Y):
    # Matriz de Vandermonde
    V = np.vander(X)

    # Resolver el sistema para encontrar los coeficientes
    b = Y
    V_inv = np.linalg.inv(V)

    # Formula
    coeficientes = V_inv @ b  # -> x^4 + x^3 + x^2 + x^1 + x^0

    return coeficientes


# Datos (corregidos)
X = np.array([1.5, 8.5, 22, 35])
Y = np.array([0, 9, 28, 26])

# a3, a2, a1, a0
print(vandermonde(X, Y))
coeficientes = vandermonde(X, Y)


# Crear polinomio como función para evaluar
def evaluar_polinomio(coefs, x):
    resultado = 0
    for i, coef in enumerate(coefs):
        resultado += coef * (x ** (len(coefs) - i - 1))
    return resultado


# Evaluar en punto específico
punto_eval = 33
valor_punto = evaluar_polinomio(coeficientes, punto_eval)
print(f"\nP({punto_eval}) = {valor_punto:.6f}")
