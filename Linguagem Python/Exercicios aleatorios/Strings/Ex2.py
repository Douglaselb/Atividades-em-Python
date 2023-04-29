texto = '      hello WORLD'
print(f'''Exemplo de tratamento de Strings
Texto usado no exemplo '{texto}'
texto.upper(): {texto.upper()}
texto.lower(): {texto.lower()}
texto.casefold(): {texto.casefold()}
texto.strip(): {texto.strip()}
texto.replace('h', 'R'): {texto.replace('h', 'R')}
texto.split('W'): {texto.split('W')}
texto.capitalize(): {texto.capitalize()}
texto.center(70) {texto.center(70)}
texto.endswith('Silva'): {texto.endswith('Silva')}
texto.endswith('WORLD'): {texto.endswith('WORLD')}
texto.startswith('hello'): {texto.startswith('hello')}
texto.find('l'): {texto.find('l')}
texto.count('l'): {texto.count('l')}
texto.lower().count('l'): {texto.lower().count('l')}
len(texto): {len(texto)}
''')