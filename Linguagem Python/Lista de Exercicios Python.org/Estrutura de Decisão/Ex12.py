'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
'''
valor_hora = float(input('Informe o valor da sua hora trabalhada: '))
horas_mes = float(input('Informe o quanto trabalhou no mes: '))
salario = valor_hora*horas_mes
ir = ''
inss = 0.1
fgts = 0.11
sindicato = 0.03
if salario <= 900:
    ir = 0
elif 900 < salario <= 1500:
    ir = 0.05
elif 1500 < salario <= 2500:
    ir = 0.1
else:
    ir = 0.2
print(f'''Salario bruto: R${salario}
(-)IR ({ir*100}%): R${salario*ir}
(-)INSS ({inss}%): R${salario*inss}
FGTS ({fgts*100}%): R${salario*fgts}
Total de desconto: R${(salario*ir)+(salario*inss)}
Salario Liquido: R${salario-((ir*salario)+(salario*inss))}''')