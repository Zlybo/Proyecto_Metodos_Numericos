import sympy
import numpy as np
import matplotlib.pyplot as plt

# Definir símbolo y función
x = sympy.Symbol('x')
funcion = sympy.sympify('x**3 - x - 2')

# Derivar la función
derivada = sympy.diff(funcion, x)

# Convertir las expresiones simbólicas a funciones de numpy
funcion_lambda = sympy.lambdify(x, funcion, 'numpy')
funcion_lambda_derivada = sympy.lambdify(x, derivada, 'numpy')

# Crear valores de x para graficar
x_valores = np.linspace(-5, 5, 400)
y_valores = funcion_lambda(x_valores)
dy_valores = funcion_lambda_derivada(x_valores)

# Graficar
plt.figure(figsize=(10, 6))  # 1000x600

plt.plot(x_valores, y_valores, label=f"f(x): {funcion}", color='blue')
plt.plot(x_valores, dy_valores, label=f"f'(x): {derivada}", color='red', linestyle='--')

# Punto evaluado
plt.scatter(2, funcion_lambda(2), color='green', label=f'P(2) = {funcion_lambda(2):.6f}')
plt.axvline(x=2, color='green', linestyle=':', alpha=0.5)
plt.axhline(y=funcion_lambda(2), color='green', linestyle=':', alpha=0.5)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title('Función y su Derivada')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.show()
