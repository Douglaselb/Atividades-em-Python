#calculo de indice de massa corporea

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso atual: '))
imc = peso / (altura**2)
if imc < 25:
    print('IMC abaixo de 25, seu peso esta normal.')
elif imc <= 29 and imc >= 25:
    print('IMC entre 25 e 29, você esta com excesso de peso.')
elif imc <= 35 and imc >= 30:
    print('IMC entre 30 e 35, você esta obeso')
else:
    print('IMC acima de 35 é diagnosticado como super obesidade.')
print(f'Pelos dados informados o seu IMC é de {imc:.2f}')