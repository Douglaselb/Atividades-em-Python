#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

valor = int(input('Digite o valor da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = valor + (10 - 1) * razao
for c in range(valor, ultimo + razao, razao):
    print(c,' > ',end='')
print('Programa finalizado.')