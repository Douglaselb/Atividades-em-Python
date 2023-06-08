'''
    Faça um programa que peça para n pessoas a sua idade, ao final
    o programa devera verificar se a média de idade da turma varia entre
    0 e 25, 26 e 60 e maior que 60;
    e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

resposta = ''
situacao = ''
contador = soma = idade = media_idade = media = 0

while resposta != 'n':
    contador += 1
    idade = int(input(f'Inform a {contador}\u00b0 idade: '))
    soma += idade
    resposta = str(input('Deseja continuar? [S/N]: ')).lower()[0]

media = soma/contador
if media > 0 and media <= 25:
    media_idade = '0 e 25'
    situacao = 'jovem'
elif media > 25 and media <= 60:
    media_idade = '26 e 60'
    situacao = 'adulta'
else:
    media_idade = 'maior que 60'
    situacao = 'idosa'
print('Programa finalizado.')
print(f'A media da idade dos alunos esta entre {media_idade} anos, sendo assim uma turma {situacao}.')
