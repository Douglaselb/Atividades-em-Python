#Usando funções anônimas, no lugar do def se usa a atribuição lambda

x = int(input('Digite um valor: '))
y = int(input('Digite um valor: '))
soma = lambda x, y: x + y
print(soma(x, y))
