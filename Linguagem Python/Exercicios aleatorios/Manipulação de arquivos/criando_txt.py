# Criando arquivos txt

teste = open('teste.txt', 'a')
teste.write('''Testando a criação de um arquivo txt com texto simples.
Para criação de arquivos é simples, fazendo usoo do método open().

    teste = open('teste.txt, 'a')

O código acima a variável teste cria um arquivo e o .txt determina o tipo do arquivo.
O parâmetro 'a' abre um arquivo em modo anexo, ao escrever algo novo, o conteúdo será adicionado no final do arquivo.
''')
teste.close()
