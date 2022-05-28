class Estado():

    def __init__(self, dato):
        self.dato = dato
        self.estadoAceptacion = False
        self.estadoInicial = False

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getEstadoAceptacion(self):
        return self.estadoAceptacion

    def setEstadoAceptacion(self, estadoAceptacion):
        self.estadoAceptacion = estadoAceptacion

    def getEstadoInicial(self):
        return self.estadoInicial

    def setEstadoInicial(self, estadoInicial):
        self.estadoInicial = estadoInicial