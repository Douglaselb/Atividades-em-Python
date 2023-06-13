# Método usado para modificar as dimensões de uma matriz

import numpy as np

matriz_um = np.array([1,2,3,4,5,6])

'''
    Primeiro valor indica que a array resultante tenha n elementos.
    Segundo valor indica que a array resultante tenha n elementos na segunda dimensão
    O total de elementos não pode ultrapassar o total da original
'''
primeira_modificada = matriz_um.reshape(2, 3)
segunda_modificada = matriz_um.reshape(3, 1, 2) # 1-D para 3-D

print('Matriz original:\n', primeira_modificada.base) # O .base mostra a matriz original usada na modificação
print('\nMatriz modificada:\n', primeira_modificada)
print('\nSegunda matriz modificada:\n', segunda_modificada)
