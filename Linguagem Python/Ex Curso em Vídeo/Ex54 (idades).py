from datetime import date
menor = 0
maior = 0
quantidade = 0
resposta = ''
atual = date.today().year
while resposta != 'nao':
    quantidade += 1
    nascimento = int(input(f'Digite a data de nascimento do {quantidade}°: '))
    if (atual - nascimento) > 18:
        maior += 1
    else:
        menor += 1
    resposta = str(input('Deseja continuar? [Sim/nao]: ')).lower()

print(f'Foram informados {quantidade} datas de nascimento onde {menor} são menores de idade e {maior} maiores de idade.')