total = maior = menor = cont = 0
nbarato = ' '
while True:
    print('Cadastro de produtos')
    nome = str(input('Nome do produto : '))
    valor = float(input('Digite o valor do produto : '))
    total += valor
    concluir = str(input('Deseja continuar? : ')).upper().strip()[0]
    if valor >= 1000: maior += 1
    if concluir == 'N':break
print(f'''
A soma dos itens listados da {total}
Produtos de alto custo somam {maior} itens.''')