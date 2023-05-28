#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()
if sexo[0] == 'M': print('Sexo masculino armazenado com sucesso')
elif sexo[0] == 'F': print('Sexo feminino armazenado com sucesso')
else: print('Sexo invalido.')