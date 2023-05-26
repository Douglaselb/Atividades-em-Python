'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''

salario_hora = float(input('Informe o valor do seu salario por hora trabalhada: '))
hora_mes = float(input('Informe quantas horas trabalha no mês: '))
salario_bruto = salario_hora*hora_mes
ir , inss, sindicato = salario_bruto*0.11, salario_bruto*0.08, salario_bruto*0.05
salario_liq = salario_bruto-(ir+inss+sindicato)
print(f'''Com base nas informações passadas os valores são:
INSS = {inss}
Imposto de Renda = {ir}
Sindicato = {sindicato}
Salario Liquido = {salario_liq}
''')