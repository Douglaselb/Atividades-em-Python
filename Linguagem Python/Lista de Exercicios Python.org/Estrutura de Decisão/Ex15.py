#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
print('Para sabermos se os valores formam um triangulo informe o tamanho dos lados dele.')
lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))
if lado1+lado2 < lado3 or lado2+lado3 < lado1:
    print('Um dos lados impede a criação do triangulo')
else:
    if lado1 == lado2 == lado3:
        print('Triangulo equilatero formado.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triangulo isosceles formado.')
    else:
        print('Triangulo Escaleno formado.')