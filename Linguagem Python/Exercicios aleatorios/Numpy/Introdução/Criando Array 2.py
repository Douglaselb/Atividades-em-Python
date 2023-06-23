# Outras maneiras de criar array

import numpy as np

var = 5
zeros = np.zeros((2,3)) # Array com zeros com tamanho definido
uns = np.ones((2,3)) # Array com de valor 1 e de tamanho definido 

# Array a partir de um número/variável específico, o tamanho da Array é determinado pelo usuario
array_var = np.full((2,3),var)

# Array sequêncial a partir de um intervalo, sendo similar ao range() nativo do Python
sequencia = np.arange(50,60,3)

# Parecido com a np.arange() porém o terceiro valor determina a quantidade de elementos entre o intervalo escolhido
sequencia_dois = np.linspace(0,1,3)

aleatorios = np.random.rand(2,3) # Array com valores aleatórios com tamanho definido

aleatorios_inteiros = np.random.randint(10,20, size=(2,5)) # Array aleatória com intervalo e tamanho específico

#dados = np.loadtxt('nome_do_arquivo.txt', delimiter=',')  Criando Array a partir de um arquivo com o delemitador ','

funcao_lambda = np.fromfunction(lambda i, j: i + j, (3,3))

print(funcao_lambda)
print(zeros.ndim)
