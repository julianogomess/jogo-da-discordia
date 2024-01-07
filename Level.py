import random


class Level:
    def __init__(self):
        self.palavras1 = []
        self.palavras2 = []
        self.palavras = []
        self.vez = 1
        self.escolhida = ""

    def trocaVez(self):
        if 1 == self.vez:
            self.vez = 2
        else:
            self.vez = 1

    def addPalavra(self, palavra):
        if self.vez==1:
            self.palavras1.append(palavra)
        else:
            self.palavras2.append(palavra)
        self.palavras.remove(palavra)

    def buscaPalavra(self):
        self.escolhida=random.choice(self.palavras)
        return self.escolhida