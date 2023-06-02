#Altere o programa anterior para mostrar no final a soma dos números.
inicio = int(input('Informe o primeiro da contagem: '))
fim = int(input('Informe o ultimo número da contagem: '))
soma = 0
while inicio < (fim-1):
    inicio += 1
    soma += inicio
    print(inicio, end=' ')
print(f'A soma dos número é de: {soma}.')