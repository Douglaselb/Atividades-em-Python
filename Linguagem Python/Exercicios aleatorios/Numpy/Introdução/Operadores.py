# Usando alguns operadores matemáticos com array

import numpy as np

aleatorio = np.random.randint(10,20,(3,3))

print(aleatorio)

print('A soma dos elementos de índice [2][1] + [1][0]: ', aleatorio[2][1], '+' , aleatorio[1][0], '=', aleatorio[2][1] + aleatorio[1][0])

print('A multiplicação dos elementos de índice [0][1] x [2][0]: ', aleatorio[0][1], '+' , aleatorio[2][0], '=', aleatorio[0][1] * aleatorio[2][0])
