from latex2sympy2 import latex2sympy
import numpy as np


def jacobi(matriz_str, vector_str, x_0_str, tolerancia, max_iter):
    A = np.array(latex2sympy(matriz_str), dtype=float)
    b = np.array(latex2sympy(vector_str), dtype=float)
    x_0 = np.array(latex2sympy(x_0_str), dtype=float)

    # Diagonal, Diagonal Estrica Inferior y Diagonal Estricta Superior
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    # Inversa de D
    D_inv = np.linalg.inv(D)

    # Matriz T y vector c
    T = -D_inv @ (L + U)
    c = D_inv @ b

    eigvals = np.linalg.eigvals(T)
    radio_espectral = max(abs(eigvals))

    print("Radio espectral ρ(T):", radio_espectral)
    if radio_espectral < 1:
        print("El método Jacobi CONVERGERÁ.")
    else:
        print("El método Jacobi NO CONVERGERÁ.")
        return [], radio_espectral

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = T @ x_0 + c
        error = np.linalg.norm(x_next - x_0, ord=np.inf)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next.tolist(),
            "error": error
        })
        x_0 = x_next
        iteracion += 1

    return tabla, radio_espectral


def gauss_seidel(matriz_str, vector_str, x_0_str, tolerancia, max_iter):
    A = np.array(latex2sympy(matriz_str), dtype=float)
    b = np.array(latex2sympy(vector_str), dtype=float)
    x_0 = np.array(latex2sympy(x_0_str), dtype=float)

    # Diagonal, Diagonal Estrica Inferior y Diagonal Estricta Superior
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    # Paso 2: Matriz T y vector c, Matriz de Transicion y Vector Constante
    DL_inv = np.linalg.inv(D + L)
    T = -DL_inv @ U
    c = DL_inv @ b

    # Radio espectral: Se necesita que p(T_SOR) < 1, para que converga, de lo contrario no llegará al resultado
    eigvals = np.linalg.eigvals(T)
    radio_espectral = max(abs(eigvals))

    print("Radio espectral ρ(T):", radio_espectral)
    if radio_espectral < 1:
        print("El método Gauss-Seidel CONVERGERÁ.")
    else:
        print("El método Gauss-Seidel NO CONVERGERÁ.")
        return [], radio_espectral

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = T @ x_0 + c
        error = np.linalg.norm(x_next - x_0, ord=np.inf)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next.tolist(),
            "error": error
        })
        x_0 = x_next
        iteracion += 1

    return tabla, radio_espectral


def sor(matriz_str, vector_str, x_0_str, omega, tolerancia, max_iter):
    A = np.array(latex2sympy(matriz_str), dtype=float)
    b = np.array(latex2sympy(vector_str), dtype=float)
    x_0 = np.array(latex2sympy(x_0_str), dtype=float)

    # Diagonal, Diagonal Estrica Inferior y Diagonal Estricta Superior
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    # Matriz de Transicion y Vector Constante
    DL_inv = np.linalg.inv(D + omega * L)
    T = DL_inv @ ((1 - omega) * D - omega * U)
    c = omega * DL_inv @ b

    # Radio espectral: Se necesita que p(T_SOR) < 1, para que converga, de lo contrario no llegará al resultado
    eigvals = np.linalg.eigvals(T)
    radio_espectral = max(abs(eigvals))

    print("Radio espectral ρ(T):", radio_espectral)
    if radio_espectral < 1:
        print("El método SOR CONVERGERÁ.")
    else:
        print("El método SOR NO CONVERGERÁ.")
        return [], radio_espectral

    tabla = []
    error = 100
    iteracion = 0

    while iteracion < max_iter and error > tolerancia:
        x_next = T @ x_0 + c
        error = np.linalg.norm(x_next - x_0, ord=np.inf)

        tabla.append({
            "iter": iteracion + 1,
            "x_n": x_next.tolist(),
            "error": error
        })
        x_0 = x_next
        iteracion += 1

    return tabla, radio_espectral
