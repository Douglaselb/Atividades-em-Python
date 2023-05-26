#Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input('Informe um valor: '))
num2 = float(input('Informe um segundo valor: '))
print(f'{num1} é o maior.') if num1 > num2 else print(f'{num2} é o maior.')