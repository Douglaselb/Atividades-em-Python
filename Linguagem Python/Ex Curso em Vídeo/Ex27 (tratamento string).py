#crie um programa que leia o nome completo de uma pessoa e mostre

#primeiro nome
#ultimo nome

nome1 = str(input('Digite seu nome completo: '))
nome = nome1.split()
print(f"""O nome informaro foi o: {nome1}
O primeiro nome é: {nome[0]}
O ultimo sobrenome foi o: {nome[-1]} 
""")