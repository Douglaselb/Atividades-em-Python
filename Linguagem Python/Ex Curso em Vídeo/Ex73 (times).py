lista = ('Corintinhans','Palmeiras','Santos','Grêmio','Cruzeiro',
         'Flamengo','Vasco','Chapecoense','Atletico','Botafogo',
         'Atletico-PR','Bahia','São Paulo','Fluminense','Sport',
         'Vitoria','Curitiba','Avai','Ponte preta','Atletico - GO')
print('~*'*30)
print(f'Os seis primeiros colocados na lista são:\n{lista[:6]}')
print('~*'*30)
print(f'Os quatro ultimos colocados são:\n{lista[-4:]}')
print('~*'*30)
print(f'Segue a lista dos times em ordem alfabetica:\n{sorted(lista)}')
print('~*'*30)
print(f'O Chapecoense esta na {lista.index("Chapecoense")}° posicção.')