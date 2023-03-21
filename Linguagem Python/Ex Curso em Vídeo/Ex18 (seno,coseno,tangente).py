import math
ang = float(input('Favor digitar o ângulo a ser calculado: '))
seno = math.sin(math.radians(ang))
print(f"""ângulo usado para calculo foi o {ang}
Seno = {seno}""")
cos = math.cos(math.radians(ang))
print(f'Cosseno = {cos:.3f}')
tang = math.tan(math.radians(ang))
print(f'Tangente = {tang:.3f}')