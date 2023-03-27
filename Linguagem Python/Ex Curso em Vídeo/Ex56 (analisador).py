#analisador de pessoa idade e kg
quant = 0
soma_idade = 0
feminino_maior = 0
nome_max_velho = ''
homem_max = 0
for pessoa in range(1,5):
    print(f'\t - - - {pessoa}° PESSOA - - - ')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    quant += 1
    soma_idade += idade
    media = soma_idade / quant
    if sexo in 'Ff' and idade > 19:
        feminino_maior += 1
    if pessoa == 1 and sexo in 'Mm':
        homem_max = idade
        nome_max_velho = nome
    if sexo in 'Mm' and idade > homem_max:
        homem_max = idade
        nome_max_velho = nome
print(f'A media das idades informadas é de: {media}.\nForam informadas {feminino_maior} mulheres maiores de 20 anos.\nO {nome_max_velho} é o mais velho da lista com {homem_max} de idade.')