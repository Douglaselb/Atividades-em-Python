#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#Área de cobertura 1L = 3m², 1Lt = 18L, 1Lt = R$80.
from math import ceil
print('Para saber quanto de tinta será usada precisamos saber a área e para fazer o calculo informe a altura e largura da parede.')
altura = float(input('Altura: '))
largura = float(input('Largura: '))
area = altura*largura
lt = 80
print(f'Área informada é um total de {area}m\u00b2, e para cobrir toda esta área precisaremos de {ceil(area/3)}L')
print(f'Você precisará apenas de uma lata para cobrir a área informada, que custará R$ {ceil(area/18)*lt:.2f}.') if (area/18) <= 1 else print(f'Você precisará {ceil(area/18)} Latas, que custará R$ {ceil(area/18)*lt:.2f}.')

'''if (area/18) <= 1:
    print('Você precisará apenas de uma lata para cobrir a área informada')
else:
    print(f'Você precisará {ceil(area/18)} Latas.')'''