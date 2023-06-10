# O termo 'tensor' é usado para identificar as dimensões da array

import numpy as np

# Matriz 0-D
matriz_zero = np.array(555)

# Matriz 1-D
matriz_um = np.array([1,2,3,4,5])

# Array 2-D
matriz_dois = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Array 3-D ela contem n matrizes
matriz_n = np.array([[10,9,8],[8,10,9],[9,8,10],[10,9,8]])

print(f'''Matrizes e seus exemplos
Matriz 0-D:
{matriz_zero}

Matriz 1-D:
{matriz_um}

Matriz 2-D:
{matriz_dois}

Matriz 3-D:
{matriz_n}
''')