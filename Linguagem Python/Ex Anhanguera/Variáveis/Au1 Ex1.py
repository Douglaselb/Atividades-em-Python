"""no python podemos declarar o tipo da variavel ou não.
Em outros tipos de linguagem é obrigatorio declarar o tipo da variavel no inicio.
Por se uma linguagem orientada a objeto o retorno do type() no python será <class ' '> """
ano = 2023
nome = 'Zhin'
altura = 1.95
flag = True
print('\tVariavel não tipada:')
print(type(ano))
print(type(nome))
print(type(altura))
print(type(flag))
print('~*~'*10)
print('\tVariavel tipada:')
ano = int(2023)
nome = str('Zhin')
altura = float(1.95)
flag = bool(True)
print(type(ano))
print(type(nome))
print(type(altura))
print(type(flag))