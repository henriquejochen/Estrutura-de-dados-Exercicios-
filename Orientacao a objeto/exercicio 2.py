class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado * self.lado


q1 = Quadrado(10)


print("Lado:", q1.retornar_lado())

print("Área:", q1.calcular_area())

q1.mudar_lado(10)

print("Novo lado:", q1.retornar_lado())
print("Nova área:", q1.calcular_area())
