# Para percorrermos os elementos da array um método é usar o loop for

import numpy as np
array_zero = np.array([1,2,3,4,5])
array_um = np.array([[1,2,3,4,5,],[10,9,8,7,6]])
array_dois = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_tres = np.array([[[11,12,13],[21,22,23]],[[31,32,33],[41,42,43]]])
print('array 1-D original:\n', array_zero, '\nApós o loop: ', end='')
for l in array_zero:
    print(l, end='  ')

# Para array 2-D acima precisa de um for para cada dimensão
print('\narray 2-D original:\n', array_um, '\nApós o loop: ', end='')
for i in array_um:
    for z in i:
        print(z, end='  ')

# Array 3-D
print('\nArray 3-D original:\n', array_tres, '\nApós o loop: ', end='')
for x in array_tres:
    for y in x:
        for k in y:
            print(k, end='  ')
