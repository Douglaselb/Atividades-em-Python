#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('\tPar? ou Impar?')
resposta = ''
while resposta != 'nao':
    num = int(input('Digite um número inteiro: '))
    print('O número é par.') if num % 2 == 0 else print('O número é impar.')
    resposta = str(input('Deseja continuar?: ')).lower()
if resposta == 'nao': print('\tSimulador finalizado.')