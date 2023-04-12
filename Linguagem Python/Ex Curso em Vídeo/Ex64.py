x = soma = c = 0
while x != 999:
    soma += x; c += 1
    x = int(input('Digite um número inteiro (digitar 999 finaliza o programa): '))
print(f'Foram digitados {c-1} números e a soma deles é igual a {soma}')
print('Concluido')