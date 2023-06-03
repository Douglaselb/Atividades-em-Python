#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
impar = par = 0
for c in range(10):
    num = int(input(f'Informe o {c+1}\u00b0 valor: '))
    if num % 2 == 1:
        impar += 1
    else:
        par += 1
print(f'No total foram: {impar} números sendo impar\n{par} números sendo par.')
    
    