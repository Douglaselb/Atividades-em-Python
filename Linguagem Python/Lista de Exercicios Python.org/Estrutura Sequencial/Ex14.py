#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

kg_peixe = float(input('Informe o peso total do peixe: '))
limite = 50
if kg_peixe > limite:
    multa = (kg_peixe-limite)*4
    print(f'O peixe passou do limite permitido por lei, com a multa o peixe fica no valor de {multa}')
else:
    print('O peixe esta no peso permitido por lei, sendo assim não foi multado.')