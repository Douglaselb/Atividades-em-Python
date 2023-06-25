# Continuação da filtragem

import numpy as np

array_original = np.array([99, 88, 77, 66, 55, 44])
condicao = array_original > 70
filtro_um = array_original[condicao] # Filtrando números maiores que 70
condicao_dois = array_original % 2 == 0
filtro_dois = array_original[condicao_dois]

print('Array original:', array_original)
print('Condição (maior que 70): ', filtro_um)
print('Condição (números pares): ', filtro_dois)
