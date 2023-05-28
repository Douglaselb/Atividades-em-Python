#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
texto = str(input('Digite uma letra: ')).lower()
print(f'A letra digitada ({texto[0]}) é uma vogal.') if texto[0] in 'aeiou' else print(f'A letra ({texto[0]}) é uma consoante.')