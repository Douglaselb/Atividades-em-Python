# Faça um programa que calcule o mostre a média aritmética de N notas

resposta = ''
numero = soma = contador = 0
while resposta != 'n':
    contador += 1
    numero = float(input(f'Informe o {contador}\u00b0 número: '))
    soma += numero
    resposta = str(input('Deseja continuar? [S/N]: ')).lower()[0]
print('Programa finalizado.')
print(f'O total de notas informadas foi de {contador}, a soma total foi {soma}, e a media é {soma/contador}')
