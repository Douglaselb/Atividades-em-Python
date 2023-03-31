#Estrutura de repetição While.

x = 1
while x != 0:
    x = int(input('Digite um valor (para sair do loop digite 0): '))
    if x % 2 == 0:print('O número é par')
    else:print('O número é impar')

#While é usado quando não sabemos quantas vezes precisamos repetir o código