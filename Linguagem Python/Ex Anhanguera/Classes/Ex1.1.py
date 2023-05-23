from time import sleep
class conta_banco():
    saldo = 0
    def depositar(self,valor):
        self.saldo += valor
    def saque(self,valor):
        if self.saldo >= valor:
            print('Operação realizada.')
            self.saldo -= valor
        else:
            print('Operação invalida, saldo insuficiente.')
conta = conta_banco()
"""print('''Sua conta bancaria foi criada com sucesso, as operações disponiveis são:
[1] Depositar.
[2] Saque.
[3] Saldo.
[4] Finalizar operações.
''')"""
resp = ''
"""resp = int(input('Digite a operação escolhida: '))"""
while resp != 4:
    print('''Sua conta bancaria foi criada com sucesso, as operações disponiveis são:
[1] Depositar.
[2] Saque.
[3] Saldo.
[4] Finalizar operações.
''')
    resp = int(input('Digite a operação escolhida: '))
    if resp == 1:
        valor_deposito = float(input('\nInforme o valor do Deposito: R$'))
        conta.depositar(valor_deposito)
        sleep(2)
        print('\n')
    elif resp == 2:
        valor_saque = float(input('\nInforme o valor do Saque: R$'))
        conta.saque(valor_saque)
        sleep(2)
        print('\n')
    elif resp == 3:
        print(f'\nSeu saldo atual é de R${conta.saldo}')
        sleep(2)
        print('\n')
    else:
        print('\nOperação invalida, tente novamente.')
        sleep(2)
        print('\n')
print('Operação finalizada.')
