class Estado():

    def __init__(self, dato):
        self.dato = dato
        self.listaAdyacentes = []
        self.estadoAceptacion = False
        self.estadoInicial = False

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getlistaAdyacentes(self):
        return self.listaAdyacentes

    def setlistaAdyacentes(self, listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes

    def getEstadoAceptacion(self):
        return self.estadoAceptacion

    def setEstadoAceptacion(self, estadoAceptacion):
        self.estadoAceptacion = estadoAceptacion

    def getEstadoInicial(self):
        return self.estadoInicial

    def setEstadoInicial(self, estadoInicial):
        self.estadoInicial = estadoInicial