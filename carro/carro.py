class Motorista:

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCNH(self, cnh):
        self.__cnh = cnh

    def getCNH(self):
        return self.__cnh

class Chassi:
    def setVin(self, vin):
        self.__vin = vin

    def getVin(self):
        return self.__vin

class Roda:
    def setAro(self, aro):
        self.__aro = aro

    def getAro(self):
        return self.__aro

class Carro:
    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setMotorista(self, motorista):
        self.__motorista = motorista

    def getMotorista(self):
        return self.__motorista

    def setRodas(self, roda):
        self.__rodas = []
        self.__rodas.append(roda)

    def getRodas(self):
        return len(self.__rodas)

    def setChassi(self, chassi):
        self.__chassi = chassi

    def getChassi(self):
        return self.__chassi

cenora = Motorista();
cenora.setCNH(234567)
cenora.setNome("Samuel")

chassi = Chassi()
chassi.setVin("hgfshgshfghsfghsdgh")

step = Roda()
step.setAro(14)

cenoraMovel = Carro()
cenoraMovel.setChassi(chassi)
cenoraMovel.setMotorista(cenora)
cenoraMovel.setRodas(step)
cenoraMovel.setRodas(step)
cenoraMovel.setRodas(step)
cenoraMovel.setRodas(step)
cenoraMovel.setRodas(step)
cenoraMovel.setModelo("BigCarrot")

print(vars(cenoraMovel))

for roda in cenoraMovel:
    print(f' - {Roda.aro}')
