#Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for c in range(5):
    c +=1
    num = float(input(f'Informe o {c}\u00b0: '))
    soma += num

print(f'A soma do números é {soma}, e a media é {soma/(c):.2f}.')