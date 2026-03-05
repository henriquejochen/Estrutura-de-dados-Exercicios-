class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print("Foram abastecidos", litros, "litros")
        else:
            print("Não há combustível suficiente na bomba")

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print("Valor a pagar: R$", valor)
        else:
            print("Não há combustível suficiente na bomba")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade


bomba = BombaCombustivel("Gasolina", 5.50, 1000)

bomba.abastecerPorValor(55)
bomba.abastecerPorLitro(10)

bomba.alterarValor(5.80)
bomba.alterarCombustivel("Etanol")
bomba.alterarQuantidadeCombustivel(800)

print("Tipo:", bomba.tipoCombustivel)
print("Valor por litro:", bomba.valorLitro)
print("Quantidade restante:", bomba.quantidadeCombustivel)
