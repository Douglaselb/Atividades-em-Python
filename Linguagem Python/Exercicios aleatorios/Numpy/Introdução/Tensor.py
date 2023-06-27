# O termo 'tensor' é usado para identificar as dimensões da array

import numpy as np

# array 0-D
array_zero = np.array(555)

# array 1-D
array_um = np.array([1,2,3,4,5])

# Array 2-D
array_dois = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Array 3-D ela contem n Arrays
array_n = np.array([[10,9,8],[8,10,9],[9,8,10],[10,9,8]])

print(f'''Arrays e seus exemplos
array 0-D:
{array_zero}

array 1-D:
{array_um}

array 2-D:
{array_dois}

array 3-D:
{array_n}
''')
