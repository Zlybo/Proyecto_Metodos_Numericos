import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Datos
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 5, 0, 12, 9])

# Crear el spline cúbico natural
spline = CubicSpline(x, y, bc_type='natural')

# Evaluar el spline para graficar
x_fino = np.linspace(1, 5, 200)
y_fino = spline(x_fino)

# Imprimir los coeficientes por tramo
print("Coeficientes por tramo (forma: a(x - x_i)^3 + b(x - x_i)^2 + c(x - x_i) + d):")
for i in range(len(spline.c.T)):
    a, b, c, d = spline.c[:, i]
    print(f"Tramo {i}:")
    print(f"S_{i}(x) = {a:.4f}(x - {x[i]})^3 + {b:.4f}(x - {x[i]})^2 + {c:.4f}(x - {x[i]}) + {d:.4f}")
    print()

# Graficar
plt.plot(x, y, 'o', label='Puntos')
plt.plot(x_fino, y_fino, label='Spline cúbico')
plt.title('Spline Cúbico Natural')
plt.legend()
plt.grid(True)
plt.show()
