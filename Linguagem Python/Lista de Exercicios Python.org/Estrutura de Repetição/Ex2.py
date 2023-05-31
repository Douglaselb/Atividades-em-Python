#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
user = str(input('Informe o nome do usuário: '))
senha = input('Crie uma senha: ')
while senha == user:
    print('A senha não pode ser igual ao usuário, tente novamente.')
    senha = input('Crie uma senha: ')
print('Usuário e senha cadastrado com sucesso.')