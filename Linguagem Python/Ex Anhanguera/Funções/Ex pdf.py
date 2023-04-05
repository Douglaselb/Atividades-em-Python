#Visualização números pares com a função filter
num = list(range(0,22))
numpar = list(filter(lambda x: x % 2 == 0, num))
print('Números pares entre 0 e 22',numpar)