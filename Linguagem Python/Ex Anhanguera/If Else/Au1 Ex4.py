#Estrutura composta if/else
#if simples usa apenas if
#if composto usa if e else
#if encadeado usa if elif e else
x = int(input('Digite um valor: '))
if x % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')
print('O valor é maior que 10') if x > 10 else print('O valor é menor que 10')
