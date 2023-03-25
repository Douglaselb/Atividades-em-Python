#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('\tPara iniciarmos nosso simulador digite 3 números inteiros.')

x1 = int(input('Digite um valor: '))
x2 = int(input('Digite um valor: '))
x3 = int(input('Digite um valor: '))

if x1 > x2 and x1 > x3:         #maior
    maior = x1
elif x2 > x1 and x2 > x3:
    maior = x2
elif x3 > x1 and x3 > x2:
    maior = x3
if x1 < x2 and x1 < x3:         #menor
    menor = x1
elif x2 < x1 and x2 < x3:
    menor = x2
elif x3 < x1 and x3 < x2:
    menor = x3

print(f'O número maior é o {maior}.\nE o número menor é o {menor}.')
