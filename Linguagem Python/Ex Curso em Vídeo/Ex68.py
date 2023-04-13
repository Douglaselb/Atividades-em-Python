wins = 0
from random import randint
while True:
    x = int(input('Digite um valor de 0 a 10: '))
    maq = randint(0,10)
    choice = ' '
    div = (x+maq)%2
    if choice not in 'PI':
        choice = str(input(f'Você escolhe Par ou Impar? ')).upper().strip()[0]
    print(f'Sua escolha foi {x}, a maquina escolheu {maq}, e a soma deu {x+maq}.')
    if choice == 'P':
        if div == 0: print('Você ganhou!!!');wins += 1
        else:print('Você perdeu =/')
    elif choice == 'I':
        if div == 1: print('Você ganhou!!!');wins += 1
        else:print('Você perdeu =/')
    y = str(input('Você quer continuar? ')).upper().strip()[0]
    if y == 'N':
        if wins > 1:print(f'Você ganhou {wins} vezes')
        elif wins <= 1:print(f'Você ganhou {wins} vez')
        break