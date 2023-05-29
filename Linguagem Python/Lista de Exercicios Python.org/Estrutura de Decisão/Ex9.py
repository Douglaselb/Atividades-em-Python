#Faça um Programa que leia três números e mostre-os em ordem decrescente.
sequencia = []
for c in range(1,4):
    numeros = int(input(f'Informe o {c}\u00b0 número: '))
    sequencia.append(numeros)
print(f'Os números em sequencia crescente = {sorted(sequencia)}.')