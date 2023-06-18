'''
    O método Stac() faz o empilhamento de duas arrays
    O parametro axis= determina se a array resultante retornara na horizontal ou vertical
'''

import numpy as np

array_um = np.array([9, 8, 7])
array_dois = np.array([3, 2, 1])
# Podemos determinar uma hora array dentro da stack().
# exemplo stack_array = np.stack((array_um, array_dois, [11,22,33]), axis= 0)
stack_array = np.stack((array_um, array_dois), axis= 0)
stack_axis = np.stack((array_um, array_dois), axis= 1)
print('Axis= 0: \n', stack_array)
print('\nAxis= 1: \n', stack_axis)
print('*+'*20)

# Hstack() empilhamento horizontal, temos um retorno parecido com o concatenate
hstack = np.hstack((array_dois, array_um))
print('\nUsando o método Hstack:\n', hstack)

# Vstack() empilhamento vertical
vstack = np.vstack((array_dois, array_um))
print('\nUsando método Vstack:\n', vstack)

# Dstack()
dstack = np.dstack((array_dois, array_um))
print('Usando método Dstack:\n', dstack)
