'''Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''
var = int(input('Digite um número entre 0 e 10: '))
while var <= 0 and var > 10:
    print('Valor invalido.')
    var = int(input('Informe um número entre 0 e 10: '))
