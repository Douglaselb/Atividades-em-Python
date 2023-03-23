#tratamento de string

nome = str(input('Digite seu nome: ')).strip()
print(f"""
Tudo maiusculo: {nome.upper()}
Tudo minusculo: {nome.lower()}
Quantas letras tem o nome: {len(nome)}
Quantas letras tem o primeiro nome: {nome.find(' ')}
""")