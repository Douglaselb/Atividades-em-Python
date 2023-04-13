pmaior = hom = mmenor = 0
while True:
    print('-'*30)
    print('CADASTRO DE PESSOA')
    print('-'*30)
    idade = int(input('Idade : '))
    pessoa = str(input('Sexo : ')).upper().strip()[0]
    cont = str(input('Deseja continuar? : ')).upper().strip()[0]
    if idade >= 18:pmaior+=1
    if pessoa == 'M':
        if idade <= 20:mmenor += 1
    if pessoa == 'H':hom += 1
    if cont == 'N':break
print('~*'*30)
print(f'''Foram cadastrados:
{hom} homens
{pmaior} pessoas maiores de 18 anos
{mmenor} mulheres menor de 20 anos''')
