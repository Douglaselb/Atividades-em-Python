#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
maior = menor = soma = 0
resposta = ''
conjunto = set()
while resposta != 'n':
    x = int(input('Informe o valor a ser adicionado no conjunto: '))
    while x < 0 or x > 1000:
        print('Valor invalido, tente novamente.')
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
