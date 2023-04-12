x = int(input('Digite quantos termos quer mostrar da sequência de Fibonacci: '))
x1 = 0
x2 = 1
c = 3
print(f'{x1} > {x2}', end=' ')
while c <= x:
    x3 = x1 + x2
    print(f' > {x3}', end=' ')
    x1 = x2;x2 = x3;c += 1
print('Concluido.')