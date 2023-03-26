#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('''
O JOKENPO é uma brincadeira simples e divertida onde você escolhe entre três opções

    [0] Pedra   -   [1] Papel   -   [2] Tesoura

Lembrando que:
papel ganha da pedra mas perde para a tesoura,
tesoura ganha de papel mas perde para pedra,
pedra ganha de tesoura mas perde para papel.

''')
escolha = int(input('Digite sua escolha! '))
maq = randint(0,2)
sleep(1)
print('JO\n')
sleep(1)
print('KEN\n')
sleep(1)
print('PO\n')
sleep(1)
if escolha == 0: #Pedra
    if maq == 1: print('Você perdeu! Pedra perde para Papel, tente novamente mais tarde.')
    elif maq == 2: print('Você ganhou!!! Pedra ganha de Tesoura, PARABENS!!!')
    else: print('HEHEHE Deu empate, ambos escolheram Pedra')
if escolha == 1: #Papel
    if maq == 0: print('Você ganhou!!! Papel ganha de Pedra, PARABENS!!!')
    elif maq == 2: print('Você perdeu! Papel perde para Tesoura, tente novamente mais tarde.')
    else: print('HEHEHE Deu empate, ambos escolheram Papel')
if escolha == 2: #Tesoura
    if maq == 0: print('Você perdeu! Tesoura perde para Pedra, tente novamente mais tarde.')
    elif maq == 1: print('Você ganhou!!! Tesoura ganha de Papel, PARABENS!!!')
    else: print('HEHEHE Deu empate, ambos escolheram Tesoura')