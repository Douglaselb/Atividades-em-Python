# Cria uma array de números aleatorios com uma determinada probabilidade

from numpy import random

grafico = random.binomial(n= 5, p= 1, size=10) # p determina a probabilidade do n aparecer

print(grafico)
