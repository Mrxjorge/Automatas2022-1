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
                elif (not estado.getEstadoInicial() and estado.getEstadoAceptacion()):
                    estado.setEstadoAceptacion(False)
                    estado.setEstadoInicial(True)
            inalcanzables = self.verificarEstadosInacccesibles(automata)
            for estado1 in inalcanzables:
                automata.borrarEstado(estado1)
        else:
            automata.invertirTransiciones()
            for estado in automata.ListaEstados:
                if (estado.getEstadoInicial() and not estado.getEstadoAceptacion()):
                    estado.setEstadoInicial(False)
                    estado.setEstadoAceptacion(True)
                elif (not estado.getEstadoInicial() and estado.getEstadoAceptacion()):
                    estado.setEstadoAceptacion(False)
                    estado.setEstadoInicial(True)
            
            
        
        # self.verificarEstadosInacccesibles(automata)
        self.actulizarListaAceptacion(automata)    
        automata.imprimirAutomata()
    
    def actulizarListaAceptacion(self, automata):
        automata.estadosAceptacion.clear()
        for estado in automata.ListaEstados:
            if estado.getEstadoAceptacion():
                automata.estadosAceptacion.append(estado.getDato())

    def verificarEstadosInacccesibles(self, automata):
        destinos = []
        origenes = []
        estadosInaccesibles = []
        for transicion in automata.ListaTransicionesSinCiclos:
            if transicion.getDisponible() and (transicion.getOrigen() != transicion.getDestino()):
                destinos.append(transicion.getDestino())
                origenes.append(transicion.getOrigen())
        for estado in automata.ListaEstados:
            if (estado.getDato() not in origenes) and (not estado.getEstadoInicial()):
                estadosInaccesibles.append(estado.getDato())
        return estadosInaccesibles
        
    def ciclo(self, automata, dato):
        for transicion in automata.ListaTransiciones:
            if (transicion.getOrigen() == transicion.getDestino()) and (transicion.getOrigen() == dato):
                return True
        return False

    def estadoOrigen(self, automata, dato):
        for transicion in automata.ListaTransiciones:
            if transicion.getOrigen() == dato:
                return True
        return False

    def estadoDestino(self, automata, dato):
        for transicion in automata.ListaTransiciones:
            if transicion.getDestino() == dato:
                return True
        return False

        