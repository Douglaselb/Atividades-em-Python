#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
paisb, txb, ano = 200000, 0.015, 0
paisa = int(input('Informe a população inicial: '))
txa = float(input('Informe a taxa de crescimento anual[%]: '))
while paisa < paisb:
    paisa += paisa * txa
    paisb += paisb * txb
    ano += 1
print(f'Após {ano} anos, a população do pais A ultrapassou o pais B.\nAbaixo podemos observar a população total de cada país.\nPais A = {paisa:.2f}.\nPais B = {paisb:.2f}.')