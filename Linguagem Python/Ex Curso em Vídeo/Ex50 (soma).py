#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
par = 0
impar = 0
for c in range (1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        num += c
    else:
        impar += c
print(f'A soma dos valores pares digitados é {par}, e os impares é {impar}')