class Jogo:
    def __init__(self):
        self.ponto1 = 0
        self.ponto2 = 0
        self.levels = 3
        self.palavras = []
        self.numeroPalavras = 3
        self.level = 1
        self.estado = 0

    def addPonto(self, time):
        if time == 1:
            self.ponto1 += 1
        else:
            self.ponto2 += 2

    def addPalavra(self, palavra):
        self.palavras.append(palavra)
        
    def checkLevel(self,vez):
        if vez == 1:
            self.level+=1
        if self.level==self.levels+1:
            self.estado=2

