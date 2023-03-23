#Tratamento de strings ( busca linear )

def busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False

nome = 'Abner Ana Camila Igor Drake Darli Bruno Barbara Claudio Zenaide'.split()
print(f'Os nomes listados são : {nome}')
print('\tBuscando o nome Carlos de diferentes maneiras')
print('Buscando com in o resultado é: ', 'Carlos' in nome)
print('Buscando Carlos com if o resultado é: ',end='')
print('Sim') if 'Carlos' in nome else print('Não')
print('Buscando o nome Carlos por funcção o resultado é:',busca_linear(nome, 'Carlos'))
alvo = nome.index('Darli') #Buscando a posição
print('O nome Darli na nossa lista esta na posição: ',alvo+1)
