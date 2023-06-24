# A permutação é quando os indices dos elementos são alterados/embaralhados

import numpy as np
from numpy import random

array = np.array([1, 9, 3, 4, 2])
print(random.permutation(array)) # Usando a permutation() a array original não é alterada
random.shuffle(array) # O shuffler() para alterar os indices altera a array original
print(array)
