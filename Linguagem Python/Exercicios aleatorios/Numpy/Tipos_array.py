# Identificando os tipos de dados

import numpy as np

numeros = np.array([1,2,3,4])
nomes = np.array(['Abc', 'Def','Ghi'])
decimais = np.array([0.1,0.2,9.9])
boleano = np.array([True, False])
definido = np.array([1,2], dtype='i2') # Tipo e tamanho definido

print('Matriz: ', numeros, 'Tipo: ', numeros.dtype)
print('Matriz: ', nomes, 'Tipo: ', nomes.dtype)
print('Matriz: ', decimais, 'Tipo: ', decimais.dtype)
print('Matriz: ', boleano, 'Tipo: ', boleano.dtype)
