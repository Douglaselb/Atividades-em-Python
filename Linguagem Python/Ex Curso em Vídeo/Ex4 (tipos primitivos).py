#Tipos primitivos

x = input('Digite algo: ')
print(f"""
O tipo primitivo do ({x}) é {type(x)}
({x}) é um caracter? {x.isalpha()}
({x}) é um alpha númerico? {x.isnumeric()}
""")