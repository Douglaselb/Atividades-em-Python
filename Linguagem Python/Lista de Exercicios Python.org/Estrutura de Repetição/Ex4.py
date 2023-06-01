#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paisa, txa, paisb, txb, ano = 80000, 0.03, 200000, 0.015, 0
while paisa < paisb:
    paisa = paisa+(paisa*txa)
    paisb = paisb+(paisb*txb)
    ano +=1
print(f'Após {ano} anos, a população do pais A ultrapassou o pais B.\nAbaixo podemos observar a população total de cada país.\nPais A = {paisa:.2f}.\nPais B = {paisb:.2f}.')