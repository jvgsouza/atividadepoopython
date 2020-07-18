#Atividade - Televisão
class Televisao:
    def __init__(self,canal, min = 2,max = 14):
        self.ligada = False
        self.canal = canal
        self.tamanho = 0
        self.marca = ""
        self.min = min
        self.max = max

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def muda_canal_para_baixo(self):
        if (self.canal == 1):
            self.canal = self.max
        else:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if (self.canal == 14 ):
            self.canal = self.min
        else:
            self.canal += 1

tv1 = Televisao(5,6,40)
tv1.setTamanho(24)
tv1.setMarca("samsung")
print(tv1.getTamanho(),tv1.getMarca())

tv2 = Televisao(10,1,55)
tv2.setTamanho(40)
tv2.setMarca("lg")
print(tv2.getTamanho(),tv2.getMarca())



