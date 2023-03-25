"""crie um programa que leia uma frase e mostre
quantas vezes aparece a letra 'A"
em que posição ela aparece a primeira vez
em que posição ela aparece a ultima vez"""

texto = str(input('Digite uma frase: '))
x = str(input('Digite a letra que gostaria de pesquisar: '))
print(f"""A letra (a) na frase digitada ({texto}) repete {texto.count(x)} vezes.
A primeira vez que ele aparece é na posição {texto.find(x)+1}
E por ultimo na posição {texto.rfind(x)+1}""")

