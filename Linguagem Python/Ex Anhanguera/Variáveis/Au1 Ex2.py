#Diferentes tipos de saida de dados
nome = input('Digite um nome: ')
print('\tSinataxe C\nOlá %s'%(nome))                #formatação usada na linguagem C/C++
print('\tSintaxe .format()\nOlá {}'.format(nome))   #formatação usada em versões antigas do python
print(f'\tSintaxe F-string\nOlá {nome}')            #formatação usada em versões python 3.6