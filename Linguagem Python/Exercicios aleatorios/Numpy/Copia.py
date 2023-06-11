# Copiando matriz

import numpy as np

matriz_raiz = np.array([1,2,3,4,5])
copia = matriz_raiz.copy()

# Alterando um valor da matriz raiz. A mudança do índice não altera o valor da copy()
matriz_raiz = matriz_raiz[::-1]

print(matriz_raiz)
print(copia)

