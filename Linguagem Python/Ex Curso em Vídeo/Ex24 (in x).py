#crie um programa que leia o nome da cidade
#e diga se ela comeca ou nao com o nome santo


cidade = str(input('Digite o nome da sua cidade: ')).strip().title()
print('Existe Santo no nome da cidade digitada?: ', 'Santo' in cidade)
