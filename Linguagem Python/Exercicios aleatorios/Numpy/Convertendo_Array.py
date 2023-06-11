# Maneiras de converter matrizes

import numpy as np

array_um = np.arange(10.1,20.2, 3)

'''
    O ('i') pode ser substituido por (int) sem alterar o final
    Alguns exemplos de valores que são usados e suas substituições
    i → int
    b → bool
    f → float
'''
tipo_int = array_um.astype('i')


print('Matriz raiz: ', array_um, '.\nTipo: ', array_um.dtype)
print('\nMatriz derivada da raiz: ', tipo_int, '\nTipo: ', tipo_int.dtype)
