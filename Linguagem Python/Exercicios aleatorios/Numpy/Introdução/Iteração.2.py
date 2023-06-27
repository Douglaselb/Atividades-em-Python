# Continuação da iteração de array

import numpy as np

array = np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
segunda_array = np.array([1,2,3,4,5])
# Fazendo uso do nditer() não é preciso fazer tantos loops
for x in np.nditer(array):
    print(x, end='  ')
print('\nUsando flag e op_dtype')
for y in np.nditer(array, flags=['buffered'], op_dtypes= [float]): # O op_dtype não altera a array original
    print(y, end='  ')
