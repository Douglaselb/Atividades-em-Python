#repetir enquanto o valor for diferente do pedido
sexo = str(input('Digite seu sexo [F/M]: '))
while sexo not in ['M','F']:
    sexo = str(input('Dados invalidos tente novamente, digite sexo [M/F] : ')).upper().strip()[0]
    if sexo == 'F':
        print('Sexo feminino cadastrado.') 
    if sexo == 'M':
        print('Sexo masculino cadastrado.') 
print('Programa finalizado')