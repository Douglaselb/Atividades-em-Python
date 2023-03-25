#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 adicional por km rodado.
distancia = float(input('Digite a distância da viagem em km: '))
custo = 0
custo_adicional = 0
if distancia < 200:
    custo = 0.5
    print(f'O custo da viagem ficou em R${distancia * custo}')
else: 
    custo = 0.5
    custo_adicional = 0.45
    print(f'O custo da viagem ficou em R${200*custo+((distancia-200)*custo_adicional)}')
