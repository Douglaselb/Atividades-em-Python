#crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
#true ou false

nome = str(input('Digite seu nome completo: ')).split()
print('Existe o sobrenome Silva no nome digitado?',end=' ')
print('Sim') if 'Silva' in nome else print('Não')