''''
    Como acessar os elementos de uma array, seguindo os indices da programação
    o primeiro elemento de uma array se encontra no indice zero
'''

import numpy as np

aleatorios_inteiros = np.random.randint(10,20, size=(3,3))

print(aleatorios_inteiros)
print('O primeiro elemento da primeira linha acessamos com o indice [0][0]: ',aleatorios_inteiros[0][0])
print('Para identificar o terceiro elemento da segunda linha usamos o indice [1][2]:',aleatorios_inteiros[1][2])
