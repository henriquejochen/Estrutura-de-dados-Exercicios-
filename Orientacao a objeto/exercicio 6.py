class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(self.nome, "comeu", alimento)

    def ver_bucho(self):
        print("Bucho de", self.nome, ":", self.bucho)

    def digerir(self):
        if self.bucho:
            alimento = self.bucho.pop(0)
            print(self.nome, "digeriu", alimento)
        else:
            print(self.nome, "não tem nada no bucho")


macaco1 = Macaco("kako")
macaco2 = Macaco("kuka")

macaco1.comer("banana")
macaco1.comer("maçã")
macaco1.comer("laranja")

macaco1.ver_bucho()

macaco2.comer("uva")
macaco2.comer("pera")
macaco2.comer("manga")

macaco2.ver_bucho()

macaco1.comer(macaco2.nome)

macaco1.ver_bucho()

macaco1.digerir()
macaco1.ver_bucho()
