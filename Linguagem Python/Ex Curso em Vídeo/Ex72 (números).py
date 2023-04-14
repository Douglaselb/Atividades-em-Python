num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
x = int(input('Digite um número (entre 0 e 5): '))
while True:
    if x <= 5:
        print(num[x])
        perg = str(input('Deseja continuar : ')).upper().strip()[0]
        if perg == 'S':x = int(input('Digite um número (entre 0 e 5): '))
        else:
            break
    else:
        print('tente novamente')
        x = int(input('Digite um número : '))
