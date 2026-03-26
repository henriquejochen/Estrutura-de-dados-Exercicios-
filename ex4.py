class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [None] * capacidade

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                break
            posicao += 1

        for i in range(self.ultima_posicao, posicao - 1, -1):
            self.valores[i + 1] = self.valores[i]

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i], end=" ")
            print()

    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    def remove(self, valor):  # ← corrigido (4 espaços)
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1

        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]

        self.ultima_posicao -= 1
        self.valores[self.ultima_posicao + 1] = None
        return posicao


vetor = VetorOrdenado(20)

nome = "HENRIQUE"

print("a) Inserindo caracteres:")
for letra in nome:
    print(f"Inserindo: {letra}")
    vetor.insere(letra)

print("\nb) Vetor após inserção:")
vetor.imprime()


print("\nc) Pesquisa de caracteres:")
for letra in ["H", "E", "U"]:
    pos = vetor.pesquisa(letra)
    if pos != -1:
        print(f"{letra} encontrado na posição {pos}")
    else:
        print(f"{letra} NÃO encontrado")


print("\nd) Remoções:")

inicio = vetor.valores[0]
print(f"Removendo início: {inicio}")
vetor.remove(inicio)


meio_index = vetor.ultima_posicao // 2
meio = vetor.valores[meio_index]
print(f"Removendo meio: {meio}")
vetor.remove(meio)

fim = vetor.valores[vetor.ultima_posicao]
print(f"Removendo fim: {fim}")
vetor.remove(fim)

print("\ne) Vetor após remoções:")
vetor.imprime()
