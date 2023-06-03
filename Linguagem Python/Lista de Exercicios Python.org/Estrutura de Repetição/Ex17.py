#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Informe o valor a ser calculado: '))
x = num
fato = 1
while x > 0:
    print(x, end='')
    print(' x ', end='') if x > 1 else print(' = ', end= '')
    fato *= x
    x -= 1
print(fato)