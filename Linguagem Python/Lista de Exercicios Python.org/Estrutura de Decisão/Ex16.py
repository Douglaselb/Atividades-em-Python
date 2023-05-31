'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
1 - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
2 - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
3 - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
4 - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
from math import sqrt
var_a = float(input('Informe o valor de A: '))
var_b = float(input('Informe o valor de B: '))
var_c = float(input('Informe o valor de C: '))
if var_a == 0:
    print('Programa finalizado, a equação não é de segundo grau.')
else:
    delta = var_b**2 - (4*var_a*var_c)
    if delta < 0:
        print('Programa finalizado, equação não possui raiz real.')
    elif delta == 0:
        raiz = -var_b / (2*var_a)
        print('Equação possui apenas uma raiz real ',raiz,' .')
    else:
        raiz1 = ((-var_b+(sqrt(delta)))/(2*var_a))
        raiz2 = ((-var_b-(sqrt(delta)))/(2*var_a))
        print(f'A equação possue duas raizes: {raiz1:.2f} e {raiz2:.2f}.')