class Transicion():

    def __init__(self,Origen,Destino, valor):
        self.origen=Origen
        self.valor = valor
        self.destino = Destino

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return  self.destino

    def getValor(self):
        return self.valor

    def setOrigen(self, origen):
        self.origen = origen

    def setDestino(self, destino):
        self.destino = destino

    def setValor(self, valor):
        self.valor = valor