#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
resposta = ''
while resposta != 'n':
    num = int(input('Informe um número: '))
    if num < 2:
        print("Não é primo.")
    else:
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print("É primo.")
        else:
            print("Não é primo.")
    resposta = str(input('Gostaria de continuar?[S/N]: ')).lower()[0]
    print('Programa finalizado.')