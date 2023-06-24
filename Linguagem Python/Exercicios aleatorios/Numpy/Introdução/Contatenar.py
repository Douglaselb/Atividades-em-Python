# Método para concatenar array

import numpy as np
matriz_um = np.array([1,2,3])
matriz_dois = np.array([10,11,12])
uniao = np.concatenate((matriz_um, matriz_dois)) # Concatenando matriz 1-D

matriz_tres = np.array([[20,21,22],[30,31,32]])
matriz_quatro = np.array([[90,91,92],[80,81,82]])
uniao_dois = np.concatenate((matriz_tres, matriz_quatro), axis= 1) # Concatenando 2-D

print('Concatenando matrizes.\nArray 1-D: ', uniao)
print('Matrizes 2-D:\n', uniao_dois)
