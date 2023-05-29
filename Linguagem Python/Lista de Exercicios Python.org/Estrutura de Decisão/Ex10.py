#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Atualmente os turnos de estudo são:\nMatutino    -   Vespertino  -   Noturno')
turno = str(input('\nInforme o turno que você estuda: ')).upper().strip()
if turno[0] in 'M': print('Bom dia!')
elif turno[0] in 'V': print('Boa tarde!')
elif turno[0] in 'N': print('Boa noite!')
else: print('Valor incorreto, programa finalizado.')