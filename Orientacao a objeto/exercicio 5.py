class TV:

    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido")

    def aumentar_volume(self):
        if self.volume < 50:
            self.volume += 1
        else:
            print("Volume máximo")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo")


tv = TV()

print("Canal inicial:", tv.canal)
print("Volume inicial:", tv.volume)

tv.mudar_canal(10)
print("Novo canal:", tv.canal)

tv.aumentar_volume()
print("Volume:", tv.volume)

tv.diminuir_volume()
print("Volume:", tv.volume)
