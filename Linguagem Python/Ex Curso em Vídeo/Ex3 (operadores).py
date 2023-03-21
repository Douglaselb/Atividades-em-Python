#Exemplos com operadores

x = int (input('Digite um valor: '))
y = int (input('Digite um segundo valor: '))
print(f"""
Adição: {x}+{y}={x+y}
Subtração: {x}-{y}={x-y}
Multiplicação: {x}x{y}={x*y}
""")

"""
Ordem em que as operações seram executadas:
1° ()
2° **
3° * / // %
4° + -
"""