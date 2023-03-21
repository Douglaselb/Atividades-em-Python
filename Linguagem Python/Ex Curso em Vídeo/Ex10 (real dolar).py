real = float(input('Informe quantos reais serão convertidos: '))
dolar = 5.28 #valor do dolar 19/03/2023
print(f"""
Valor informado em real R${real}
Valor atual do dolar U${dolar}
Convertendo R${real} para dolar o valor fica em U${(real*dolar):.2f}
""")