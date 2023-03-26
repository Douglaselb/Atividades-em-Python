#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria

import datetime
nascimento = int(input('Informe o ano de nascimento do atleta: '))
atual = datetime.datetime.today().year
idade = atual - nascimento
categoria = ''
if idade < 9:
    categoria = 'Mirim'
elif idade > 8 and idade < 14:
    categoria = 'Infantil'
elif idade > 13 and idade < 18:
    categoria = 'Júnior'
elif idade > 17 and idade < 24:
    categoria = 'Sénior'
elif idade > 23:
    categoria = 'Master'
print(f'Pela idade informada sua categoria é {categoria}')