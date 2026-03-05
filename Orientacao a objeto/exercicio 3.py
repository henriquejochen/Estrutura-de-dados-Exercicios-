class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valores(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornar_valores(self):
        return self.base, self.altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


r1 = Retangulo(10, 5)

print("Base e Altura:", r1.retornar_valores())
print("Área:", r1.calcular_area())
print("Perímetro:", r1.calcular_perimetro())

r1.mudar_valores(20, 10)

print("Novos valores:", r1.retornar_valores())
print("Nova área:", r1.calcular_area())
