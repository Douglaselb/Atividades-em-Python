#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
from calendar import isleap
ano = int(input('Digite o ano a ser verificado se é bissexto: '))
if isleap(ano):
    print('O ano é bissexto.') 
else:
    print('O ano não é bissexto.')
