from Controlador.Automata import *

class Operaciones():

    def complemento(self, automata):
        new = automata
        for estado in new.ListaEstados:
            estado.estadoAceptacion = not estado.estadoAceptacion
        return new
        
    def reverso(self, automata: Automata):
        automata.actulizarListaAceptacion()
        if len(automata.estadosAceptacion) > 1:
            self.singularizarAceptacion(automata)
            # automata.imprimirTransiciones()
            # automata.imprimirEstados()
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
        automata.actulizarListaAceptacion()
        automata.imprimirAutomata()

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

    def singularizarAceptacion(self, automata: Automata):
        if(automata.estadosAceptacion.__len__() == 1): return
        automata.ingresarEstado("ES")
        for estado in automata.estadosAceptacion:
            value: Estado = automata.ObtenerO(estado)
            value.estadoAceptacion = False
            automata.ingresarTransicion(value.getDato(), "ES", "L")
        automata.ObtenerO("ES").estadoAceptacion = True
        
    # def unionAutomatas(self, autoA: Automata, autoB: Automata) -> Automata:
        