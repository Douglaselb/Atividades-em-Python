'''Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25 00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''
from math import ceil, floor
area_total = float(input('Informe a área total em m\u00b2: '))
total_litros = area_total/6
total_litros += total_litros*0.1
total_lata, total_lata18 = ceil(total_litros/3.6), ceil(total_litros/18)    #Quantidade total de latas
total_lata_preco, total_lata18_preco = total_lata*25, total_lata18*80   #Valor total
lata18_floor = floor(total_litros/18)   #Quantidade de latas 18L arredondando para baixo
resto = total_litros%18 #Quantidade falta
precisa = ceil(resto/3.6)   #Quantidade de lata 3.6L que precisa
print(f'''Vejamos os diferentes orcamentos, lembrando que já consta a folga de 10% para uma area de {area_total}m\u00b2.
Usando Galão de 3,6 Litros:
Total de latas: {total_lata}
Valor total: R$ {total_lata_preco:.2f}
{'*'*20}
Usando Lata de 18 Litros:
Total de latas: {total_lata18}
Valor total: R$ {total_lata18_preco:.2f}
{'*'*20}
Usando ambas as latas:
Total de lata 3,6: {precisa}
total de latas 18: {floor(total_litros/18)}
Valor total: R$ {(lata18_floor*80)+(precisa*25):.2f}
''')