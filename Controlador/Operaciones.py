from Controlador.Automata import *

class Operaciones():

    def complemento(self, automata):
        new = automata
        for estado in new.ListaEstados:
            estado.estadoAceptacion = not estado.estadoAceptacion
        return new
        