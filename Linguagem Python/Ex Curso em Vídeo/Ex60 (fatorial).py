import math
x = int(input('Digite o valor da fatorial: '))
fator = 1
cont = x
fact = math.factorial(x)
while cont > 0:
    print (cont, end= '')
    print(' x ' if cont > 1 else ' = ', end= '')
    fator *= cont
    cont -= 1 
print(fator)
#print(fact)


