'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''
salario_antigo = float(input('Informe o seu salario atual: '))
reajuste = ''
porc_aumento = ''
aumento = ''
salario_novo = ''
if salario_antigo <= 280:
    porc_aumento = 0.2
    reajuste = salario_antigo*porc_aumento
    salario_novo = salario_antigo + reajuste
elif 280 < salario_antigo <= 700:
    porc_aumento = 0.15
    reajuste = salario_antigo*porc_aumento
    salario_novo = salario_antigo + reajuste
elif 700 < salario_antigo <= 1500:
    porc_aumento = 0.1
    reajuste = salario_antigo*porc_aumento
    salario_novo = salario_antigo + reajuste
else:
    porc_aumento = 0.05
    reajuste = salario_antigo*porc_aumento
    salario_novo = salario_antigo + reajuste
print(f'''Segue as informações:
Salario antigo = R${salario_antigo}
Salario novo = R${salario_novo}
Seu salario teve um aumento de R${reajuste}, sendo um aumento de {porc_aumento*100}% de aumento.''')