class Listinha:
    def __init__(self, itens):
        self.itens = itens

    def __iter__(self):
        return self.itens.__iter__()

    def __len__(self):
        return len(self.itens)

meu_objeto = Listinha([1, 2, 4])

contador = 0
for item in meu_objeto:
    contador += 1

if len(meu_objeto) == contador:
    print('São iguais!')
else:
    print('Não são iguais!')