#Sorteio aleatório de um aluno

from random import randint
print("""\tSegue a lista dos alunos que estão participando do sorteio
[1] Ana
[2] Clara
[3] Danilo
[4] Emanoel
""")
escolhido = randint(1,4)
if escolhido == 1:
    print(f'Por sorteio a Ana foi a premiada, número sorteado {escolhido}')
elif escolhido == 2:
    print(f'Por sorteio a Clara foi a premiada, número sorteado {escolhido}')
elif escolhido == 3:
    print(f'Por sorteio o Danilo foi o premiado, número sorteado {escolhido}')
else:
    print(f'Por sorteio o Emanoel foi o premiado, número sorteado {escolhido}')