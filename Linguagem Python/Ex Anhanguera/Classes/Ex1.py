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
print(conta.saldo)
conta.depositar(15)
conta.saque(10)
print(conta.saldo)