#Calcular valor do aluguel de um carro (valores, uma diaria R$60, mais R$0.15/Km)

import math
print("""Segue abaixo os valores do aluguel de carros em nossa loja:
A cada dia é cobrado o valor de R$60 e R$0.15/KM.
""")
days = float(input('Nos informe quantos dias pretende permanecer com o veiculo: '))
km = float(input('Nos informe a quilometragem que será percorrida: '))
print(f"""
Com as informações passadas segue seus respectivos valores:
{days} custará R${days*60:.2f}, e {km}KM custará R${km*0.15:.2f}.
O total do aluguel será de R${days*60+km*0.15:.2f}.

Usando a função trunc {math.trunc(days*60+km*0.15)}
Usando o modulo ceil {math.ceil(days*60+km*0.15)}
""")