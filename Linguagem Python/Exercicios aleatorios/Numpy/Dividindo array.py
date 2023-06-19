# O array_split é um metodo para dividir uma array em outras sub-array

import numpy as np

array_um = (1,2,3,4,5,6,7,8)
array_split = np.array_split(array_um, 2) # A array será dividida em duas, podendo posteriormente ser acessada separadamente
#print(array_split)

definido = np.array_split(array_um, [2, 5, 8]) # Especifica onde a array será dividida neste caso [2, 5, 8]
print(definido)
