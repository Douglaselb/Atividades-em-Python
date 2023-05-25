#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o segundo.
#o segundo elevado ao cubo.

n1 = int(input('Informe um numero: '))
n2 = float(input('Informe um segundo numero: '))
print(f'''A) mostre o produto do dobro do primeiro com metade do segundo.
\tResposta: {(n1*2)+(n2/2)}.
B) A soma do triplo do primeiro com o segundo.
\tResposta: {(n1*3)+n2}.
C) O segundo elevado ao cubo.
\tResposta: {n2**3}.
''')