'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

port = float(input('Informe a nota obtida em portugues entre 0 e 10: '))
mat = float(input('Informe a nota obtida em matematica: '))
conceito = ''
if port > 10 or mat > 10:
    print('Alguma nota esta acima do limite.')
else:
    media = (port+mat)/2
    if 0 < media <= 4: media, conceito = 'E', 'Reprovado'
    elif 4 < media <= 6: media, conceito = 'D', 'Reprovado'
    elif 6 < media <= 7.5: media, conceito= 'C', 'Aprovado'
    elif 7.5 < media <= 9: media, conceito= 'B', 'Aprovado'
    elif 9 < media <= 10: media, conceito= 'A', 'Aprovado'
print(f'Aluno {conceito}!!!, a media do aluno foi {media}')