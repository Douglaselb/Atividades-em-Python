# Copiando array

import numpy as np

array_raiz = np.array([1,2,3,4,5])
copia = array_raiz.copy()

# Alterando um valor da array raiz. A mudança do índice não altera o valor da copy()
array_raiz = array_raiz[::-1]

print(array_raiz)
print(copia)
