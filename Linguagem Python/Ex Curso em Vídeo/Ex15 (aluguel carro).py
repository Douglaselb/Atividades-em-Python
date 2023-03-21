print("""Segue abaixo os valores do aluguel de carros em nossa loja:
A cada dia é cobrado o valor de R$60/dia e R$0.15/KM."""
)
dias = int(input('Informe quantos dias pretende passar com o carro: '))
km = float(input('Informe em quilomestros a distância percorrida: '))
print(f"""\tSegue os valores da viagem:
Valor total do carro R${(dias * 60)}
Valor da distância percorrida R${(km * 0.15)}
Valor total: R${(dias * 60)+(km * 0.15)}
""")