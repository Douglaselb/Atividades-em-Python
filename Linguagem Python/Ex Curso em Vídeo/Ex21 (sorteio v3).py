#Sorteio de apresentação

import random
a1 = str(input('Digite o nome do 1° aluno: '))
a2 = str(input('Digite o nome do 2° aluno: '))
a3 = str(input('Digite o nome do 3° aluno: '))
a4 = str(input('Digite o nome do 4° aluno: '))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(f'Segue a sequencia de apresentação {lista}')