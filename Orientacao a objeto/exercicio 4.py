class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for i in range(anos):
            if self.idade < 21:
                self.altura += 0.5
            self.idade += 1

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


p1 = Pessoa("Joazinho", 20, 70, 175)

print("Nome:", p1.nome)
print("Idade:", p1.idade)
print("Peso:", p1.peso)
print("Altura:", p1.altura)

p1.envelhecer(2)

print("\nDepois de envelhecer:")
print("Idade:", p1.idade)
print("Altura:", p1.altura)

p1.engordar(3)
print("Peso após engordar:", p1.peso)

p1.emagrecer(1)
print("Peso após emagrecer:", p1.peso)
