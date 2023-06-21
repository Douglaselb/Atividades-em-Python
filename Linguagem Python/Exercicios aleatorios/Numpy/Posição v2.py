# Uma segunda maneira de localizar a posição de um elemento na array é usando o método searchsorted

import numpy as np

array_um = np.array([1,2,3,4,5])
localizando = np.searchsorted(array_um, 3)
proximo_local = np.searchsorted(array_um, 3, side='right') # O side='' define qual posição a direita ou esquerda do elemento selecionado
multiplos = np.searchsorted(array_um, [2,5]) # Selecionado varios elementos

print('Matriz original:\n', array_um)
print('Localizando a posição do elemento 3: ', localizando)
print('Localizando a posição do elemento 2 e 5: ', multiplos)
