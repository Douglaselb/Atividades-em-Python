# O shape informa o tamanho de cada dimensão da array

import numpy as np

array_um = np.array([1,2,3,4,5])
array_dois = np.array([[1,2,3,4,5],[9,8,7,6,5]])
array_tres = np.array([1,2,3,4], ndmin= 5)

print('array: ', array_um, '\nShape: ', array_um.shape)
print('*-'*30)
print('array: ', array_dois, '\nShape: ', array_dois.shape)
print('*-'*30)
print('array: ', array_tres, '\nShape: ', array_dois.shape)
