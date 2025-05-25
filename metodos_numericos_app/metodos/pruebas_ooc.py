# Parte 1
from latex2sympy2 import latex2sympy
import numpy as np

recibo = '\begin{pmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{pmatrix}'
latex = recibo.replace("\\", "\\\\")
resultado = '\\b' + latex[1:]
print('indice de barra:', resultado.index('\\', 1))
indice = resultado.index('end')
resultado = resultado[:indice - 1] + resultado[indice:]

m = latex2sympy(resultado)
print(m)
matriz = np.array(m, dtype=float)
print(np.tril(matriz))

# Parte 2
from latex2sympy2 import latex2sympy
import numpy as np

text = r"\begin{pmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{pmatrix}"
m = latex2sympy(text)
print(m)
matriz = np.array(m, dtype=float)
print(np.linalg.det(matriz))
