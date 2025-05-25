datos = [
    {0: 0.00390625},
    {1: 0.002470422594234023},
    {2: 0.0039181960968665},
    {3: 2.7757526077643035e-05},
    {4: 0.003196136706007824},
    {5: 1.599046076217192e-05}
]

metodos = ["Biseccion", "Regla Falsa", "Punto Fijo", "Newton", "Secante", "Raices Multiples"]

# Encontrar el diccionario con el menor valor
mejor = min(datos, key=lambda d: list(d.values())[0])

# Obtener el índice (clave) del método con menor error
indice_mejor = list(mejor.keys())[0]

# Obtener el nombre del método
nombre_mejor = metodos[indice_mejor]

print(f"El mejor método es: {nombre_mejor} con error {mejor[indice_mejor]}")
