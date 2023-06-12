# Diferente da copy(), quando alterada a matriz original o view() também será alterado e vice versa

import numpy as np

matriz = np.array([1,2,3,4,5])
visualizacao = matriz.view()

print(visualizacao)
print(matriz)

visualizacao[2] = 12

print(visualizacao)
print(matriz)

matriz[1] = 21

print(visualizacao)
print(matriz)
