#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

cel = float(input('Informe a temperatura em Celsius: '))
print(f'Convertendo {cel:.2f}\u00b0C para Fahrenheit temos uma temperatura de {cel*(9/5)+32:.2f}\u00b0F')