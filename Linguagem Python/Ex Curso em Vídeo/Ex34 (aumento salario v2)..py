#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('\tO aumento salarial depende do salario atual.\nSalário até R$1.250,00 terá aumento de 15%.\nPara quem recebe menos que R$1.250,00 o aumento será de 10%.')
salario = float(input('Digite o seu salario atual: '))
aumento = ''
if salario <= 1250:
    aumento = 0.15
else:
    aumento = 0.1
salario_novo = salario + (salario*aumento)
print(f'Salário antigo: R${salario}.\nSalário atualizado R${salario_novo}.')