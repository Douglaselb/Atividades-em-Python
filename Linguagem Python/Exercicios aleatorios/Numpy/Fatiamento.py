# Exemplos de fatiamento de array sintaxe [inicio:fim:intervalo] por padrão [0:0:0] ou [:::]

import numpy as np

aleatorio = np.arange(1,20,2)
ndarray = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(aleatorio)
print('Fatiando array\nDo segundo até o final: ', aleatorio[1:])
print('Do inicio ao penúltimo: ', aleatorio[:-1])
print('Do inicio ao fim pulando dois: ', aleatorio[::2])
print('*-'*30)
print(ndarray)
print('Segunda array da metade ao final: ', ndarray[1:, 2:])
print('Soma dos elementos, três, quatro e cinco de cada', sum(ndarray[1:, 2:],ndarray[:1, 2:]))