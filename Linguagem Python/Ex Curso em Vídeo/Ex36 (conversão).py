#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

import math

num = int(input('Digite um número inteiro: '))
print("""
\tEscolha a opção desejada:
[1] Binário
[2] Octal
[3] Hexadecimal""")
x = int(input('Sua escolha: '))
if x == 1:
    print(f'{x} convertido para binário = {bin(num)}')
elif x == 2:
    print(f'{x} convertido para Octal = {oct(num)}')
elif x == 3:
    print(f'{x} convertido para hexadecimal = {hex(num)}')
else:
    print('Valor invalido.\nPrograma finalizado.')