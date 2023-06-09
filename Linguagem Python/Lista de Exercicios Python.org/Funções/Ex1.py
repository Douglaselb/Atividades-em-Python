'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

valor = int(input('Informe um valor inteiro: '))


def numeros(valor):
    for c in range(valor):
        c += 1
        print(str(c) * c)


print(numeros(valor))