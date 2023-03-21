#Descontos a depender da escolha do usuário 

print("""
\tBem Vindo a nossa loja!
Nossa loja trabalha com descontos a depender da opção de pagamento
""")
resposta = int(input("""
\tAbaixo escolha a opção de pagamento:
[1] À vista 15% de desconto
[2] À vista no credito 10% de desconto
[3] 3x no credito, 5% de desconto
[4] Acima de 3x, não tem desconto

Qual das opções você prefere: 
"""))
compras = float(input('Digite o valor total da sua compra: '))
if resposta == 1:
    print(f'Pagamento à vista a sua compra total fica em R${(compras-(compras * 0.15))}')
elif resposta == 2:
    print(f'Pagamento à vista no credito a sua compra total fica em R${(compras-(compras * 0.1))}')
elif resposta == 3:
    print(f'Pagamento em até 3x a sua compra total fica em R${(compras-(compras * 0.05))}')
else:
    print(f'A opção escolhida infelizmente não tem desconto, valor da compra fica em R${compras}')
