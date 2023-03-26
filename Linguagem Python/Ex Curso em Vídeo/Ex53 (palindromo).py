print('''\nPalindromos são palavras que lidas ao contrario não tem sua pronuncia alterada.\n''')
x = str(input('Digite uma palavra para saber se ela é um palindromo: '))
inv = x[::-1]
print(f'\nA palavra digitada foi {x} e seu inverso é {inv}\n')
if x == inv:
    print('O nome é um palindromo')
else:
    print('O nome não é um palindromo')