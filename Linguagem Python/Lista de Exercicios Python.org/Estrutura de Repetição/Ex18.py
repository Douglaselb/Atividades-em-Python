#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
maior = menor = soma = 0
resposta = ''
conjunto = set()
while resposta != 'n':
    x = int(input('Informe o valor a ser adicionado no conjunto: '))
    soma += x
    conjunto.add(x)
    resposta = str(input('Deseja continuar a adicionar elementos: ')).lower()
    while resposta not in 'sn':
        print('resposta incorreta tente novamente.')
        resposta = str(input('Deseja continuar a adicionar elementos: ')).lower()
print(f'''Vejamos as informações:
      Conjunto: {conjunto}
      Menor valor: {min(conjunto)}
      Maior valor: {max(conjunto)}
      Soma dos valores: {soma}''')
