#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
num = int(input('Digite um número de 1 a 7: '))
dias = {1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'}
semana = dias.get(num)
if dias: print(f'O dia referente ao número digitado é {semana}')
else: print('Valor invalido, programa finalizado.')
