#print a pessoa com maior e menor peso
max = 0
min = 0
for c in range(1,6):
    kg = float(input(f'Informe o peso da {c}° pessoa: '))
    if c == 1:
        maior = c
        menor = c
    else:
        if kg > max:
            max = kg
        elif kg < min:
            min = kg
print(f'A pessoa com maior peso tem {max}Kg\nE o menor tem {min}Kg')