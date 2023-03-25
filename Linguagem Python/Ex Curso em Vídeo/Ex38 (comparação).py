#Escreva um programa que leia dois números inteiros e compare-os.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro número digitado é o maior.')
elif n1 < n2:
    print('O Segundo número digitado é o maior.')
else:
    print('Os numeros são iguais')