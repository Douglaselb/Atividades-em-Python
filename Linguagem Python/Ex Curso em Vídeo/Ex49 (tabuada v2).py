num = int(input('Digite o valor da tabuada: '))
produto = lambda num, c: num * c
for c in range (1,11):
    print(f'{num} x {c} = {produto(num, c)}')