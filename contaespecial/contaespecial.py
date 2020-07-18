#Atividade - Conta Especial
class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número

    def resumo(self):
        print(f"CC Número: {self.número} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            return True
        else:
            return False

    def deposito(self, valor):
        self.saldo += valor

class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def extrato(self):
        print("Limite: ",self.limite)
        print("Saldo: ", self.saldo)

    def saque(self, valor):
        if Conta.saque() == True:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            return "Saldo indisponível"