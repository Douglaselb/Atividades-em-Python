'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''
nome = str(input('Informe um nome: '))
idade = int(input('Informe uma idade: '))
salario = float(input('Informe um salário: '))
sexo = str(input('Informe um sexo [M/F]: ')).upper()
estado = str(input('Informe um Estado Civil:\nSolteiro [s]\nCasado[c]\nViuvo[v]\nDivorciado[d]\nResposta: ')).lower()
while len(nome) <= 3:
    print('\nNome muito curto, tente novamente.')
    nome = str(input('Informe um nome: '))
    while idade <= 0 and idade < 150:
        idade = int(input('\nIdade invalida, tente novamente.\nIdade entre 0 e 150: '))
        while salario <= 0:
            salario = float(input('\nSalario invalido, tente novamente.\nInforme um salário: '))
print(f'''Cadastro realizado, segue as informações cadastradas:
Nome = {nome}
Idade = {idade}
Salario = R${salario}
Sexo = {sexo[0]}
Estado Civil = {estado[0]}''')