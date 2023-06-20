# O método where() mostra a posição do elemento na array e seu tipo

import numpy as np

# Where a partir de uma array 1-D
array_um = np.array([1,2,3,9,8,7])
local_um = np.where(array_um == 9)
print('Posição do valor 9 na array 1-D:\n', local_um)

# Where a partir de uma array 2-D
array_dois = np.array([[1,2,3],[9,8,7]])
local_dois = np.where(array_dois == 9)
print('\nPosição do valor 9 na array 2-D:\n', local_dois)
