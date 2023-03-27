#print a pessoa com maior e menor peso
maior = 0
menor = 0
for c in range(1,6):
    kg = float(input(f'Informe o peso da {c}° pessoa: '))
    if c == 1:
        maior = c
        menor = c
    else:
        if kg > maior:
            maior = kg
        elif kg < menor:
            menor = kg
print(f'A pessoa com maior peso tem {maior}Kg\nE o menor tem {menor}Kg')