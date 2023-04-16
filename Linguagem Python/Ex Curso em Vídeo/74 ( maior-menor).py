from random import sample
x = sample((1,2,3,4,5,6,7,8,9,10), k=5)
print(f'''
Os números sorteados foram {x}
O maior foi o {max(x)}
O menor foi o {min(x)}
''')