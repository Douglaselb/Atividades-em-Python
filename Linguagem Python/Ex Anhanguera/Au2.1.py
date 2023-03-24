#Continuação de tratamento de strings

nome = 'Abner Ana Camila igor Drake Darli Bruno Barbara Claudio zenaide'.split()
nome2 = [nome.upper() for nome in nome] #list comprehension
nome3 = map(lambda x : x.title(), nome)
nome4 = list(nome3)
print(nome,'\n', nome2,'\n', nome4)