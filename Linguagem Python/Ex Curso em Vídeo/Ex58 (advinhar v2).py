#adivinhar o número sorteado
from random import randint
npc = randint(1,10)
usuario = 0
print('\tTente adivinhar o número que o computador escolheu!\nDigite um valor entre 1 e 10 e tente a sorte.')
while usuario != npc:
    usuario = int(input('Qual número escolheu?: '))
    print('Menos...') if usuario > npc else print('Mais...')
print(f'Você acertou !!!\nOs números foram,\nComputador: {npc}\nUsuário: {usuario}')

