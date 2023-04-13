print('Simulação de caixa eletrônico')
valor = int(input('Digte o valor a ser sacado [maior nota é R$50 e R$5 a menor] : R$'))
total = valor
nota = 50
ttnota = 0
while True:
    if total >= nota:total -= nota;ttnota += 1
    else:
        if ttnota > 0:print(f'Total de {ttnota} cédulas de R${nota}.')
        elif nota == 50:nota = 20
        elif nota == 20:nota = 10
        elif nota == 10:nota = 5;ttnota = 0
        if total == 0:break
print('Volte sempre')