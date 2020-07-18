#Atividade - Conta
class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero

    def resumo(self):
        print(f"CC Nome: {self.clientes} Número: {self.numero}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            return "Saldo insuficiente!"

    def deposito(self, valor):
        self.saldo += valor

c1 = Conta("João,Jose",345435,500)