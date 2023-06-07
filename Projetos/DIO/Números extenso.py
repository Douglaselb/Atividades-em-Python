#criar um programa para ler um número de 0 até 999 e em seguida mostrar o valor dele por extenso.
unidades = ['zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezena10 = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
def escrita(numero):
    extenso = ''
    if numero < 0 or numero > 999:
        extenso = 'Número invalido, o número tem q ser entre 0 e 999'
    elif numero == 0:
        extenso = unidades[numero]
    elif numero < 10:
        extenso = unidades[numero]
    elif numero < 20:
        extenso = dezena10[numero - 10]
    elif numero < 100:
        dezena = numero // 10
        unidade = numero % 10
        if unidade == 0:
            extenso = dezenas[dezena - 2]
        else:
            extenso = dezenas[dezena - 2] + ' e ' + unidades[unidade]
    else:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            extenso = centenas[centena]
        elif resto < 10:
            extenso = centenas[centena] + ' e ' + unidades[resto]
        elif resto < 20:
            extenso = centenas[centena] + ' e ' + dezena10[resto - 10]
        else:
            dezena = resto // 10
            unidade = resto % 10
            if unidade == 0:
                extenso = centenas[centena] + ' e ' + dezenas[dezena - 2]
            else:
                extenso = centenas[centena] + ' e ' + dezenas[dezena - 2] + ' e ' + unidades[unidade]
    return extenso
resposta = ''
while resposta != 'n':
    numero = int(input('Digite um número de 0 a 999: '))
    extenso = escrita(numero)
    print(f'O número {numero} por extenso é: {extenso}')
    resposta = str(input('Deseja continuar? [S/N]: ')).lower()[0]
print('Programa finalizado.')
