import json
from collections import deque

from Modelo.Estado import *
from Modelo.Transicion import *
from copy import copy  # para realizar copias de objetos

class Automata():

    def __init__(self):
        self.ListaEstados = []
        self.ListaTransiciones = []
        self.Alfabeto = []
        self.ruta = ''

    def cargar_automata(self, ruta):
        self.ruta = ruta
        with open(ruta) as contenido:
            automatas = json.load(contenido)
            for automata in automatas:
                estados = automata.get("Estados")
                for estado1 in estados:
                    self.ingresarEstado(estado1)
                inicial = automata.get("EstadoInicial")
                listaAceptacion = automata.get("EstadosAceptacion")
                for estado2 in estados:
                    if estado2 == inicial:
                        E = self.ObtenerO(estado2)
                        if E:
                            E.setEstadoInicial(True)
                    if estado2 in listaAceptacion:
                        E = self.ObtenerO(estado2)
                        if E:
                            E.setEstadoAceptacion(True)
                for alfabeto in automata.get("Alfabeto"):
                    self.Alfabeto.append(alfabeto)
                for transicion in automata.get("Transiciones"):
                    origen = transicion.get('origen')
                    destino = transicion.get('destino')
                    valor = transicion.get('con')
                    self.ingresarTransicion(origen, destino, valor)
        self.imprimirAutomata()


    def ingresarTransicion(self, Origen, Destino, Valor):
        if not self.verificarTransicion(Origen, Destino, Valor, self.ListaTransiciones):
            if self.verificarEstado(Origen, self.ListaEstados) and self.verificarEstado(Destino, self.ListaEstados) and Valor in self.Alfabeto:
                self.ListaTransiciones.append(Transicion(Origen, Destino, Valor))
                self.ObtenerO(Origen).getlistaAdyacentes().append(
                    Destino)
                # agrego la adyacencia

    def ingresarEstado(self, dato):
        if not self.verificarEstado(dato, self.ListaEstados):
            self.ListaEstados.append(Estado(dato))
        else:
            print("El estado ya existe, intente nuevamente")

    def verificarEstado(self, estado, listaEstados):
        for i in range(len(listaEstados)):
            if estado == listaEstados[i].getDato():
                return True
        return False

    def imprimirEstados(self):
        for i in range(len(self.ListaEstados)):
            Aceptar = "Estado aceptación" if self.ListaEstados[i].getEstadoAceptacion() else ""
            Inicio = "Estado inicial" if self.ListaEstados[i].getEstadoInicial() else ""
            print(f"Estado : {self.ListaEstados[i].getDato()} - {Aceptar} {Inicio}")

    def verificarTransicion(self, Origen, Destino, Valor, lista):
        for i in range(len(lista)):
            if Origen == lista[i].getOrigen() and Destino == lista[i].getDestino() and Valor == lista[i].getValor():
                print("Transicion repetida")
                return True
        return False

    def ObtenerO(self, dato):
        for i in range(len(self.ListaEstados)):
            if dato == self.ListaEstados[i].getDato():
                return self.ListaEstados[i]
        return None

    def imprimirTransiciones(self):
        for i in range(len(self.ListaTransiciones)):
            print("Origen: {0}  -  Destino: {1}  :  Valor:{2}".format(self.ListaTransiciones[i].getOrigen(), self.ListaTransiciones[i].getDestino(), self.ListaTransiciones[i].getValor()))

    def imprimirAutomata(self):
        self.imprimirTransiciones()
        self.imprimirEstados()
        print(self.Alfabeto)
        
    def invertirTransiciones(self):
        for transicion in self.ListaTransiciones:
            tmp = transicion.origen
            transicion.origen = transicion.destino
            transicion.destino = tmp
            
    def borrarEstado(self, dato):
        for estado in self.ListaEstados:
            if estado.dato == dato:
                self.ListaEstados.remove(estado)
                self.borrarTransicion(dato)
                break
            
    def borrarTransicion(self, dato):
        for transicion in self.ListaTransiciones:
            if transicion.origen == dato or transicion.destino == dato:
                self.ListaTransiciones.remove(transicion)