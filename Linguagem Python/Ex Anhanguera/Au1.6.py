#Usando funções
#def é usado para definir uma função

def imprimir_mensagem(disciplina, curso):   
    print(f'Usando função da disciplina {disciplina} do curso {curso}')
imprimir_mensagem('Python', 'Data Science')

def somar(a, b):
    return a + b
r = somar(2,3)
print(r)