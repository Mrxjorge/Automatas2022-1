from Controlador.Automata import *

class Operaciones():

    def complemento(self, automata):
        new = automata
        for estado in new.ListaEstados:
            estado.estadoAceptacion = not estado.estadoAceptacion
        return new
        
    def reverso(self, automata):
        if len(automata.estadosAceptacion) == 1:
            automata.invertirTransiciones()
            for estado in automata.ListaEstados:
                if (estado.getEstadoInicial() and not estado.getEstadoAceptacion()):
                    estado.setEstadoInicial(False)
                    estado.setEstadoAceptacion(True)
                    automata.estadosAceptacion.append(estado.getDato())
                elif (not estado.getEstadoInicial() and estado.getEstadoAceptacion()):
                    estado.setEstadoAceptacion(False)
                    estado.setEstadoInicial(True)
                    automata.estadosAceptacion.remove(estado.getDato())
                    
        automata.imprimirAutomata()
        