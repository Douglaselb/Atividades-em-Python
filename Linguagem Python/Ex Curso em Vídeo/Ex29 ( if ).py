#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('Tome cuidado e mantenha sempre o limite da via de 80Km/h')
velocidade = float(input('Informe a velocidade atual do veiculo: '))
print('Mantenha sempre abaixo dos 80Km/h para evitar ser multado!') if velocidade <= 80 else print(f'Você foi multado!!!\nO valor da multa ficou em R${(velocidade-80)*7}')