#Ex com operadores e função anônima
escolha = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segunod número: '))
somar = lambda n1 , n2 : n1 + n2
multiplicar = lambda n1 , n2 : n1 * n2
while escolha != 5:
    print("""\n\t[1] Somar\n\t[2] Multiplicar\n\t[3] Maior\n\t[4] Novos valores\n\t[5] Finalizar""")
    escolha = int(input('Opção escolhida: '))
    if escolha == 1:
        print(f'{n1} + {n2} = {somar(n1, n2)}')
    elif escolha == 2:
        print(f'{n1} x {n2} = {multiplicar(n1, n2)}')
    elif escolha == 3:
        print(f'O maior é o {n1}') if n1 > n2 else print(f'O maior é o {n2}')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segunod número: '))
print('Programa finalizado.')