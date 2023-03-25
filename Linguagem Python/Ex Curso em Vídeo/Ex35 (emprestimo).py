#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\tSimulador de financiamento de imovel')
valor_casa = float(input('Digite o valor do imovel pretendido: '))
salario = float(input('Informe o valor do seu salário: '))
prazo = int(input('Prazo do financiamento em meses: '))
valor_mensal = valor_casa / prazo
if valor_mensal > (salario*0.3):
    print('Infelizmente seu salário não permite fazer o financiamento, o valor mensal ultrapassa 30% do seu salário')
else:
    print(f'Parabens!!!\nCom os valores informados podemos dar continuidade ao financiamento.\nO valor da parcela mensal ficou em {valor_mensal} em {prazo} meses')