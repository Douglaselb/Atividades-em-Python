#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base = int(input('Informe a base a ser calculada: '))
expo = int(input('Agora informe o expoente: '))
resultado = 1
while expo > 0:
    if expo % 2 == 1:
        resultado *= base
    base *= base
    expo //= 2
print(f'Resultado = {resultado}')


#print(f'Base: {base}\nExpoente: {expo}\nResultado: {base**expo}') #sem estrutura de repetição5