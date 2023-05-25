#Faça um Programa que converta metros para centímetros.
medida = float(input('Informe o valor em centimetros e veja o resultado de sua conversão: '))
mili = medida * 10
metro = medida / 100
print(f'''O valor para simulação foi o {medida}cm, segue as converções:
\n{mili}mm <--- {medida}cm\n{medida}cm ---> {metro}m''')