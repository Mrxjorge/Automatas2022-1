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
            # self.verificarEstadosInacccesibles(automata)
        else:
            automata.invertirTransiciones()
            for estado in automata.ListaEstados:
                if (estado.getEstadoInicial() and not estado.getEstadoAceptacion()):
                    estado.setEstadoInicial(False)
                    estado.setEstadoAceptacion(True)
                elif (not estado.getEstadoInicial() and estado.getEstadoAceptacion()):
                    estado.setEstadoAceptacion(False)
                    estado.setEstadoInicial(True)
            
        
        self.actulizarListaAceptacion(automata)    
        automata.imprimirAutomata()
    
    def actulizarListaAceptacion(self, automata):
        automata.estadosAceptacion.clear()
        for estado in automata.ListaEstados:
            if estado.getEstadoAceptacion():
                automata.estadosAceptacion.append(estado.getDato())

    def verificarEstadosInacccesibles(self, automata):
        destinos = []
        estadosInaccesibles = []
        for transicion in automata.ListaTransiciones:
            if transicion.getDisponible():
                destinos.append(transicion.getDestino())
        for estado in automata.ListaEstados:
            if (estado.getDato() not in destinos) or (estado.getDato() in destinos and estado.getDato()):
                estadosInaccesibles.append(estado.getDato())
        print(estadosInaccesibles)
        