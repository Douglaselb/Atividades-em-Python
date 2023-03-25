#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = lambda n1, n2 : (n1 + n2) / 2
print(f'A media das notas informadas é {media(n1, n2)}')