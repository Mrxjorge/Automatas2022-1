class Transicion():

    def __init__(self,Origen,Destino, valor):
        self.Origen=Origen
        self.valor = valor
        self.destino = Destino

    def getOrigen(self):
        return self.Origen

    def getDestino(self):
        return  self.destino

    def getValor(self):
        return self.valor

    def setOrigen(self, origen):
        self.Origen = origen

    def setDestino(self, destino):
        self.destino = destino

    def setValor(self, valor):
        self.valor = valor