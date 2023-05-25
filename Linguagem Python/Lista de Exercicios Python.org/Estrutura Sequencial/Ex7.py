#Faça um Programa que calcule a área de um retangulo, em seguida mostre o dobro desta área para o usuário.
print('Para fazer um calculo completo de um retangulo favor preencher as informações abaixo.')
base = float(input('Informe a base: '))
comp = float(input('Informe o comprimento: '))
altura = float(input('Informe a altura: '))

print(f'Com as informações preenchidas temos uma area de {base*comp}m\u00b2 e {base*altura*comp}m\u00b3 de volume.')