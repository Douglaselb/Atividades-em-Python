#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
valor1 = float(input('Informe o valor do primeiro produto: '))
valor2 = float(input('Informe o valor do segundo produto: '))
valor3 = float(input('Informe o valor do terceiro produto: '))
if valor1 < valor2 and valor1 < valor3:
    print(f'Com base nos preços infomados o primeiro produto é o mais barato, custando R${valor1}')
elif valor2 < valor1 and valor2 < valor3:
    print(f'Com base nos preços infomados o segundo produto é o mais barato, custando R${valor2}')
else:
    print(f'Com base nos preços infomados o terceiro produto é o mais barato, custando R${valor3}')