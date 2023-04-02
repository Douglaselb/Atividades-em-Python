#Usando while
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o valor da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = primeiro + (10 - 1) * razao
termo = primeiro
c = 1
while c <= 10:
    print(termo,'> ', end= '')
    termo += razao
    c += 1
"""for c in range(valor, ultimo + razao, razao):
    print(c,' > ',end='')"""
print('Programa finalizado.')