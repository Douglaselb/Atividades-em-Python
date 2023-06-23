# Criando array simples

import numpy as np  # Importando biblioteca

lista = [1,2,3,4,5]
tupla = (6,7,8,9,10)
array_lista = np.array(lista) # Criando array a partir de uma lista
array_tupla = np.array(tupla) # Criando array a partir de uma tupla

print(f'Lista simples: {lista} - type: {type(lista)}\n')
print(f'Array a partir de uma lista: {array_lista} - type: {type(array_lista)}\n')
print(f'Tupla simples: {tupla} - type: {type(tupla)}\n')
print(f'Array a partir deu uma tupla {array_tupla} - type: {type(array_tupla)}')
