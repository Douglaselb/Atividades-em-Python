resposta = 's'
quant = soma = 0
while resposta in 's':
    num = int(input('Digite um número inteiro: '))
    resposta = str(input('Deseja adicionar outro valor? [S/N]: ')).lower().strip()[0]
    soma += num
    quant +=1
print(f'Você informou {quant} números e o total da soma é {soma}')