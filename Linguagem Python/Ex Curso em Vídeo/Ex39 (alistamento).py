#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
nascimento = int(input('Digite o ano de seu nascimento: '))
atual = datetime.date.today().year
if (atual - nascimento) == 18:
    print('Já está na hora de ir se alistar!')
elif (atual - nascimento) > 19:
    print('Já passou da hora de se alistar, se você não foi ainda possivelmente terá que pagar uma multa.')
else:
    print('Ainda não está na hora, aguarde mais um pouco.')