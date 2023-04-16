lista = ('Desodorante', 12,
         'Sabonete', 2,
         'shampoo', 13)
print('~-'*20)
print(f'{"Lista de produtos e preços":^40}')
print('~-'*20)
for x in range(0,len(lista)):
    if x % 2 == 0:print(f'{lista[x]:-<30}',end=' ')
    else:print(f'R${lista[x]:>6.2f}')