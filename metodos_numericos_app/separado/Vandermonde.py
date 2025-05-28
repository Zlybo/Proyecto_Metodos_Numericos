import numpy as np

X = np.array([1, 2, 3, 4, 5])
Y = np.array([10, 5, 0, 12, 9])
# Nota: Ya que tenemos 5 datos, sabemos que el polinomio va a ser de grado/orden 4

V = np.vander(X)

b = Y
V_inv = np.linalg.inv(V)

an = V_inv @ b  # -> -2.04x^4 + 23.25x^3 -88.46x^2 + 128.25x^1 - 51
# Nota: El comerse decimales como en este caso, aumenta un poco el error

print(V)
print(an)

print(np.linalg.solve(V,Y))
