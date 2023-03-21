#Calculo hipotenusa

import math
print('Para calcular a hipotenusa precisamos de algumas informações')
oposto = float(input('Informe o valor do cateto oposto: '))
adjacente = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = ((oposto**2)+(adjacente**2))
hyp = math.hypot(oposto, adjacente)
print(f"""
F-strings
\tCateto oposto {oposto} x {oposto} = {oposto**2}
\tCateto adjacente {adjacente} x {adjacente} = {adjacente**2}
\tValor da hipotenusa é {hipotenusa**0.5:.2f}

Biblioteca math
\tCateto oposto {oposto} x {oposto} = {oposto**2}
\tCateto adjacente {adjacente} x {adjacente} = {adjacente**2}
\tValor da hipotenusa é {hyp:.2f}
""")