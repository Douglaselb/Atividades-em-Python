'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
port = float(input('Digite o valor da nota em português: '))
mat = float(input('Digite o valor da nota em matemática: '))
media = (port+mat)/2
if media == 10:
    print(f'Aluno aprova do com Distinção.')
elif media >= 7:
        print('Aluno aprovado.')
elif media > 10:
    print('Valor ultrapassou o limite de 10 pontos.')
else:
    print('Aluno Reprovado.')