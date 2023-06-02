#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
inicio = int(input('Informe o primeiro da contagem: '))
fim = int(input('Informe o ultimo número da contagem: '))
while inicio < (fim-1):
    inicio += 1
    print(inicio, end=' ')