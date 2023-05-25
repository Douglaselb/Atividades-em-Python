#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal

altura = float(input('Informe a sua altura: '))
kg = float(input('Informe o seu peso: '))
print(f'Com base na sua altura e peso o seu IMC é de {kg/(altura**2):.0f}.')