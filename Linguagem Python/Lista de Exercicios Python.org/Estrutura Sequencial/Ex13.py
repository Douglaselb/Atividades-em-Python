altura = float(input('Informe a sua altura: '))
kg = float(input('Informe o seu peso: '))
imc = kg/(altura**2)
print(f'Com base na sua altura e peso o seu IMC é de {imc:.0f}.')
if imc < 18.6:
    print('Segundo o IMC você esta com baixo peso.')
elif imc < 25:
    print('Segundo o IMC você esta com peso normal.')
elif imc < 30:
    print('Segundo o IMC você esta com excesso de peso.')
elif imc < 35:
    print('Segundo o IMC você esta obeso.')
else:
    print('Você esta com obesidade extrema')