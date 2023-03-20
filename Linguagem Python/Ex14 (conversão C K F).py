print('\tSimulador de conversor de temperatura')
temperatura = float(input('Informe a temperatura em graus celsius: '))
print(f"""
Celsius {temperatura}°C
Fahrenheit {((temperatura * (9/5))+32)}°F
Kelvin {temperatura + 273}K
""")