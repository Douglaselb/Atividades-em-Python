#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
resposta = ''
while resposta != 'n':
    num = int(input('\nInforme o valor a ser calculado: '))
    x = num
    fato = 1
    if num > 16:
        print('Número muito grande.')
    else:
        while x > 0:
            print(x, end='')
            print(' x ', end='') if x > 1 else print(' = ', end= '')
            fato *= x
            x -= 1
        print(fato)
    resposta = str(input('\nDeseja continuar [S/N]: ')).lower()
print('Programa finalizado.')
