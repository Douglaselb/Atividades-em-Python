#Números pares
x1 = int(input('Digite o primeiro número: '))
x2 = int(input('Digite o ultimo número: '))
num = list(range(x1,x2+1))
numpar = list(filter(lambda x: x % 2 == 0, num))
print(f'Números pares entre {x1} e {x2}',numpar)