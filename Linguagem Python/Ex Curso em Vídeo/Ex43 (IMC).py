#calculo de indice de massa corporea

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso atual: '))
imc = lambda peso, altura : (peso / (altura**2))
print(f'Pelos dados informados o seu IMC é de {imc(peso, altura)}')