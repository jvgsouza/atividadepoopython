#Atividade - Estados e Cidades
class Estado:
    def __init__(self, nome,sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        self.populacao = 0

    def addCidades(self, cidade):
        self.populacao += cidade.getPopulacao()
        self.cidades.append(cidade)

    def returnPopulacao(self):
        return self.populacao

class Cidade:
    def __init__(self, nome,populacao):
        self.nome = nome
        self.populacao = populacao

    def getPopulacao(self):
        return self.populacao

estado1 = Estado("Minas Gerais","MG")
cidade1 = Cidade("Belo Horizonte",177475)
cidade2 = Cidade("Ibirité",1433000)
cidade3 = Cidade("Sete Lagoas",208847)
estado1.addCidades(cidade1)
estado1.addCidades(cidade2)
estado1.addCidades(cidade3)
print(estado1.returnPopulacao())


estado2 = Estado("São Paulo","SP")
cidade1 = Cidade("São Paulo",12180000)
cidade2 = Cidade("Bauru",1433000)
cidade3 = Cidade("Piracicaba",208847)
estado2.addCidades(cidade1)
estado2.addCidades(cidade2)
estado2.addCidades(cidade3)
print(estado2.returnPopulacao())


estado3 = Estado("Rio de Janeiro","RJ")
cidade1 = Cidade("Niterói",12180000)
cidade2 = Cidade("São Gonçalo",1433000)
cidade3 = Cidade("Duque de Caxias",208847)
estado3.addCidades(cidade1)
estado3.addCidades(cidade2)
estado3.addCidades(cidade3)
print(estado3.returnPopulacao())