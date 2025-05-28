import numpy as np
import sympy as sp


def newton_diferencias_divididas_completa(x, y):
    n = len(x)
    tabla = np.zeros((n, n))  # Matriz de zeros, que sera nuestra matriz diagonal inferior
    tabla[:, 0] = y  # Primera columna es y = f(x)

    # Llenamos la tabla de diferencias divididas
    for col in range(1, n):
        for fila in range(col, n):
            tabla[fila][col] = (tabla[fila][col - 1] - tabla[fila - 1][col - 1]) / (x[fila] - x[fila - col])

    return tabla


def expandir_polinomio_newton(coeficientes, x):
    x_simbolo = sp.Symbol('x')
    n = len(x)

    # Construir el polinomio de Newton
    polinomio = 0
    producto = 1
    for i in range(n):
        if i > 0:
            producto *= (x_simbolo - x[i - 1])
        polinomio += coeficientes[i] * producto

    return sp.expand(polinomio)


# Ejemplo
X = np.array([1, 2, 3, 4, 5])
Y = np.array([10, 5, 0, 12, 9])

tabla = newton_diferencias_divididas_completa(X, Y)
print(f"Tabla de diferencias divididas de Orden {len(X) - 1} (matriz triangular inferior):")
# np.set_printoptions(precision=6, suppress=True)  # Ajusta el numero de decimales
print(" ---- X ---- Y = F(X) ----\n", np.column_stack((X, tabla)))

coeficientes = tabla.diagonal()
forma = (f"{coeficientes[0]} + {coeficientes[1]}(x-1) + {coeficientes[2]}(x-1)(x-2)"
         f" + {coeficientes[3]}(x-1)(x-2)(x-3) + {coeficientes[4]}(x-1)(x-2)(x-3)(x-4)")

print("\nForma:", forma)

print("\nPolinomio Expandido:")
print(expandir_polinomio_newton(coeficientes, X))
