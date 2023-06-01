#Faça um programa que leia 5 números e informe o maior número.
numeros = []
for c in (range(1,6)):
    numero = int(input(f'Informe o {c}\u00b0 número: '))
    numeros.append(numero)
print(f'O maior valor foi o {max(numeros)}.')