#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
var_pc = randint(1,5)
resposta = ''
print('\tSimulador de adivinhação!')

while resposta != 'sim':
    var_usuario = int(input('Digite um número inteiro entre 1 e 5: '))
    sleep(3)
    print(f'Você acertou!!! Parabens!!!\nEscolha do usurário: {var_usuario}\nEscolha da maquina: {var_pc}') if var_usuario == var_pc else print(f'HEHEHE infelizmente você perdeu\nEscolha do usurário: {var_usuario}\nEscolha da maquina: {var_pc}')
    resposta = str(input('Deseja continuar? [sim/não]: ')).lower()