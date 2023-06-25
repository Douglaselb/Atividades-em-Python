# Método repassa a possição de cada elemento na iteração

import numpy as np

matriz = np.array([[1,2,3],[4,5,6]])
for posicao, elemento in np.ndenumerate(matriz):
    print(posicao, elemento)
    