# Criando arrays a partir do módulo random da biblioteca numpy

from numpy import random
# Gerando números com random
inteiro = random.randint(100) # Tipo int
decimal = random.rand() # Tipo float

# Gerando arrays
array_int = random.randint(inteiro, size=(4)) # Tipo int
array_decimal = random.rand(2, 2) # Tipo float
array_escolha = random.choice(array_int) # Escolhendo um elemento aleatorio de uma array
array_escolha_dois = random.choice(array_int, size=(3, 4)) # Criando uma array 2-D aleatoriamente

print('Tipo int:\n', array_int)
print('Tipo float:\n', array_decimal)
print('Número selecionado da array int:\n', array_escolha)
print('Criando uma array 2-D aleatoriamente a partir da array tipo int:\n', array_escolha_dois)
