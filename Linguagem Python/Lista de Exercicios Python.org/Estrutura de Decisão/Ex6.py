#Faça um Programa que leia três números e mostre o maior deles
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número adicionado foi o {n1}.')
elif n2 > n1 and n2 > n3:
    print(f'O maior número adicionado foi o {n2}')
else:
    print(f'O maior número adicionado foi o {n3}.')