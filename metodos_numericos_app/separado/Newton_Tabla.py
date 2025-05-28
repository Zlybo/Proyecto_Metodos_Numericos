import numpy as np


def newton_diferencias_divididas_completa(x, y):
    n = len(x)
    tabla = np.zeros((n, n))  # Matriz de zeros, que sera nuestra matriz diagonal inferior
    tabla[:, 0] = y  # Primera columna es y = f(x)

    # Llenamos la tabla de diferencias divididas
    for col in range(1, n):
        for fila in range(col, n):
            tabla[fila][col] = (tabla[fila][col - 1] - tabla[fila - 1][col - 1]) / (x[fila] - x[fila - col])

    return tabla


# Ejemplo
X = [3.0000, 3.6667, 4.3333, 5.0000]
Y = [6.7472, 10.7997, 15.8063, 21.7486]

tabla = newton_diferencias_divididas_completa(X, Y)
print(f"Tabla de diferencias divididas de Orden {len(X) - 1} (matriz triangular inferior):")
np.set_printoptions(precision=6, suppress=True)  # Ajusta el numero de decimales
print(" ---- X ---- Y ----\n", np.column_stack((X, tabla)))
