import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


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

    print(polinomio)
    return sp.expand(polinomio)


def evaluar_polinomio(coeficientes, puntos_x, x_eval):
    """Evalúa el polinomio de Newton en un punto x_eval"""
    resultado = coeficientes[0]
    producto = 1

    for i in range(1, len(coeficientes)):
        producto *= (x_eval - puntos_x[i - 1])
        resultado += coeficientes[i] * producto

    return resultado


# Ejemplo
X = np.array([1.5, 8.5, 22, 35])
Y = np.array([0, 9, 28, 26])

# Calcular tabla y coeficientes
tabla = newton_diferencias_divididas_completa(X, Y)
print(f"Tabla de diferencias divididas de Orden {len(X) - 1} (matriz triangular inferior):")
np.set_printoptions(precision=6, suppress=True)  # Ajusta el numero de decimales
print(" ---- X ---- Y = F(X) ----\n", np.column_stack((X, tabla)))

coeficientes = tabla.diagonal()

# Mostrar forma de Newton
forma = f"{coeficientes[0]:.6f}"
for i in range(1, len(coeficientes)):
    termino = f"{coeficientes[i]:.6f}"
    for j in range(i):
        termino += f"(x-{X[j]})"
    forma += f" + {termino}"
print("\nForma de Newton:", forma)


# Expandir polinomio
polinomio_expandido = expandir_polinomio_newton(coeficientes, X)
print("\nPolinomio Expandido:")
print(polinomio_expandido)
"""
# Evaluar en punto específico
punto_eval = 33
valor = evaluar_polinomio(coeficientes, X, punto_eval)
print(f"\nP({punto_eval}) = {valor:.6f}")

# Graficar
plt.figure(figsize=(10, 6))

# Puntos originales
plt.scatter(X, Y, color='red', s=80, label='Puntos originales')

# Curva del polinomio
x_grafica = np.linspace(min(X) - 5, max(X) + 5, 1000)
y_grafica = [evaluar_polinomio(coeficientes, X, xi) for xi in x_grafica]
plt.plot(x_grafica, y_grafica, 'b-', label='Polinomio interpolante')

# Punto evaluado
plt.scatter([punto_eval], [valor], color='green', s=100,
            label=f'P({punto_eval}) = {valor:.6f}')
plt.axvline(x=punto_eval, color='green', linestyle=':', alpha=0.5)
plt.axhline(y=valor, color='green', linestyle=':', alpha=0.5)

# Configuración
plt.title('Polinomio interpolante de Newton')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Fórmula simplificada
formula = str(polinomio_expandido).replace('**', '^')
plt.figtext(0.5, 0.01, f"P(x) = {formula}", ha='center',
            bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.show()
"""
