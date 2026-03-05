class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


bola1 = Bola("vermelha", 30, "couro")

print("Cor da bola:", bola1.mostraCor())

bola1.trocaCor("azul")

print("Nova cor da bola:", bola1.mostraCor())
