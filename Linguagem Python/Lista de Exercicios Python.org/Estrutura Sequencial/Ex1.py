#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print('Diferentes maneiras de printar o Ola mundo.')
texto = 'Ola Mundo'
tex = 'Ola '
to = 'Mundo'
print(f"""Digitando o texto no print:
Ola mundo

Criando uma variavel:
{texto}

Concatenando duas variaveis:
{tex+to}

Usando o input:
""")
var = str(input('Digite o texto "Ola Mundo" sem aspas: '))
print(var)