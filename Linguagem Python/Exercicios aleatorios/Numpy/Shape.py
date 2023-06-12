# O shape informa o tamanho de cada dimensão da matriz
import numpy as np

matriz_um = np.array([1,2,3,4,5])
matriz_dois = np.array([[1,2,3,4,5],[9,8,7,6,5]])
matriz_tres = np.array([1,2,3,4], ndmin= 5)

print('Matriz: ', matriz_um, '\nShape: ', matriz_um.shape)
print('*-'*30)
print('Matriz: ', matriz_dois, '\nShape: ', matriz_dois.shape)
print('*-'*30)
print('Matriz: ', matriz_tres, '\nShape: ', matriz_dois.shape)
