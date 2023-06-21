# Método usado para por a array em ordem

import numpy as np

array_original = ([[3,2,1],[9,8,7]]) # Ordem crescente
array_um = (['Carina', 'Debora', 'Andreia']) # Ordem alfabetica
crescente = np.sort(array_original)

print(crescente)
print(np.sort(array_um))
