# Usamos o loop for para passarmos por cada elemento da matriz

import numpy as np
matriz_zero = np.array([1,2,3,4,5])
matriz_um = np.array([[1,2,3,4,5,],[10,9,8,7,6]])
matriz_dois = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_tres = np.array([[[11,12,13],[21,22,23]],[[31,32,33],[41,42,43]]])
print('Matriz 1-D original:\n', matriz_zero, '\nApós o loop: ', end='')
for l in matriz_zero:
    print(l, end='  ')

# Para matrizes 2-D acima precisa de um for para cada dimensão
print('\nMatriz 2-D original:\n', matriz_um, '\nApós o loop: ', end='')
for i in matriz_um:
    for z in i:
        print(z, end='  ')

# Matriz 3-D
print('\nMatriz 3-D original:\n', matriz_tres, '\nApós o loop: ', end='')
for x in matriz_tres:
    for y in x:
        for k in y:
            print(k, end='  ')