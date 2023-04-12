c = 1
x = 10
quant = 0
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
quant = int(input('Quantidade de termos: '))
while x != 0:
    quant = quant + (x-10)
    while c <= quant:
        print(primeiro, end=' => ')
        primeiro += razao
        c += 1
    print('Aguardando...')
    x = int(input('Digite novamente os termos: '))
print('Concluido')