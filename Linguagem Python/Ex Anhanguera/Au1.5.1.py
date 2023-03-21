#Estrutura de repetição usando for

nome = 'Zhin'           #O nome é uma arrai de caracter (lista) cada letra representa uma posição especifica iniciando em 0

for c in nome:
   #print(c)
    print(c, end='')

for i, c in enumerate(nome):
    print(f'\nPosição {i}, Valor {c}')

