print('A empresa tomou uma decisão de aumentar o salario dos funcionarios que recebem menos de R$1.450,00')
salario = float(input('Favor informar o seu salario atual: '))
print(f'Seu salario atual passa a ser {(salario+(salario*0.15))}') if salario < 1450 else print('Seu é acima da media.\nPor esse motivo você ficou de fora do aumento de 15%')