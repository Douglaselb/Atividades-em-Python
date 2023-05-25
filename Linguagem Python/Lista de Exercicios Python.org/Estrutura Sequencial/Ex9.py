#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius

fah = float(input('Informe a temperatura em Fahrenheit: '))
print(f'Convertendo {fah:.2f}\u00b0F para Celsius temos uma temperatura de {(fah-32)*(5/9):.2f}\u00b0C')