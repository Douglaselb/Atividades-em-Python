x = (int(input('Digite o primeiro número : ')),
    int(input('Digite o segundo número : ')),
    int(input('Digite o terceiro número : ')),
    int(input('Digite o quarto número : ')))
print(f'''
Os números digitados foram {x}
O número 9 apareceu {x.count(9)} vezes
''')
if 3 in x:print(f'O número 3 aparece na {x.index(3)+1}° posição')
else:print('O número 3 não foi digitado')
print('Os números pares digitados foram')
for c in x:
    if c % 2 == 0:
        print(c,end=' ')
