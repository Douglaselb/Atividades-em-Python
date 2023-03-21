#Estrutura if com operadores lógicos

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2
freq = int(input('Digite o valor em porcentagem da frequência do aluno: '))
if media < 6.5 and freq < 55:           # usando (and) as 2 condições precisam ser verdadeiras
    print('Aluno reprovado')
elif media <= 8 and freq > 55:
    print('Aluno aprovado')
else:
    print('Aluno aprovado acima da media')

#usando (or) precisa apenas de uma condição verdadeira