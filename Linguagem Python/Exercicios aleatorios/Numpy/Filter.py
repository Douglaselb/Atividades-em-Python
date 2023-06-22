# A filtragem faz uma array derivada de outra após passar por uma condição especifica

import numpy as np

array_original = np.array([11, 22, 33, 44, 55])
condicao = [True, False, True, False, True]
filtro = array_original[condicao] # Filtrando os valores com condição True

condicao_dois = []
for elementos in array_original:
    if elementos > 25:
        condicao_dois.append(True)
    else:
        condicao_dois.append(False)
filtro_dois = array_original[condicao_dois] # Filtro dos números maiores que 25

print('Array original: ', array_original)
print('Valores com condição True', filtro)
print('Números maiores que 25: ', filtro_dois)
