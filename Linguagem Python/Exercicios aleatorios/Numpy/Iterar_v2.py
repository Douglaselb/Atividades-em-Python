# Continuação da iteração de matrizes

import numpy as np

matriz = np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
segunda_matriz = np.array([1,2,3,4,5])
# Fazendo uso do ndtiter() não é preciso fazer tantos loops
for x in np.nditer(matriz):
    print(x, end='  ')
print('\nUsando flag e op_dtype')
for y in np.nditer(matriz, flags=['buffered'], op_dtypes= [float]): # O op_dtype não altera a matriz original
    print(y, end='  ')
