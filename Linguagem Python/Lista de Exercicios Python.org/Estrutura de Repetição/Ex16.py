#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
n = int(input('Informe quantos termos será mostrado: '))
x1, x2 = 0, 1
print(x1, x2,end=' ')
c = 3 
while c <= n:
    x3 = x1 + x2
    print(x3, end=' ')
    x1 = x2
    x2 = x3
    c += 1
    if x3 >= 500:
        break