resposta = 's'
quant = soma = maior = menor = media = 0
while resposta in 's':
    num = int(input('Digite um número inteiro: '))
    resposta = str(input('Deseja adicionar outro valor? [S/N]: ')).lower().strip()[0]
    soma += num
    quant +=1
    media = soma / quant
    if quant == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num
print(f'''Você informou {quant} números e o total da soma é {soma}
O maior número digitado foi o {maior}
O menor número digitado foi o {menor}
A media dos números informados é {media}''')