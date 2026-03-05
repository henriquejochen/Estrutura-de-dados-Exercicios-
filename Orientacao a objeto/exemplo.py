class Conta:
    def __init__(self, numero, titular, saldo=0, limite=0):
        self.saldo = saldo
        self.numero = numero
        self.titular = titular
        self.limite = limite
        print("Construindo objeto...{}".format(self))

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))


conta1 = Conta(10, "Anna", 100, 200)
conta1.saque(50)
conta1.extrato()
conta1.deposita(200)
conta1.extrato()


conta2 = Conta(20, " Zequinha", 100.00, 350.00)
conta2.extrato()

conta2.saque(50)
conta2.extrato()

conta2.deposita(500)
conta2.extrato()

conta2.saque(2000)
