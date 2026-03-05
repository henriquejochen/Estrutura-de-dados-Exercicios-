class Carro:

    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Carro ligado")
        else:
            print("O carro já está ligado")

    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print("Carro desligado")
        else:
            print("Pare o carro antes de desligar")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print("Velocidade:", self.velocidade)
        else:
            print("O carro precisa estar ligado")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print("Velocidade:", self.velocidade)
        else:
            print("O carro já está parado")


carro1 = Carro("Toyota", "Corolla", 2020, "Preto", "ABC1234")

print("Marca:", carro1.marca)
print("Modelo:", carro1.modelo)

carro1.ligar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.desligar()
