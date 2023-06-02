#Faça um Programa que leia três números e mostre o maior e o menor deles.
'''numeros = []
for c in range(1,4):
    numero = int(input(f'Informe o {c}\u00b0 número: '))
    numeros.append(numero)
print(f'O maior foi o {max(numeros)}, o menor foi o {min(numeros)}.')'''

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f'O maior é o {maior} e o menor é o {menor}.')