# Diferente da copy(), quando alterada a array original o view() também será alterado e vice versa

import numpy as np

array = np.array([1,2,3,4,5])
visualizacao = array.view()

print(visualizacao)
print(array)

visualizacao[2] = 12

print(visualizacao)
print(array)

array[1] = 21

print(visualizacao)
print(array)
