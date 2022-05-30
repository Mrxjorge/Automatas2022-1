import json
from collections import deque
from typing import List

from Modelo.Estado import *
from Modelo.Transicion import *
from copy import copy  # para realizar copias de objetos

class Automata():

    def __init__(self):
        self.ListaEstados: List[Estado] = []
        self.ListaTransiciones: List[Transicion] = []
        self.Alfabeto = []
        self.estadosAceptacion = []
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
                        self.estadosAceptacion.append(estado2)
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
            if self.verificarEstado(Origen, self.ListaEstados) and self.verificarEstado(Destino, self.ListaEstados) and (Valor in self.Alfabeto or Valor == "L"):
                self.ListaTransiciones.append(Transicion(Origen, Destino, Valor))
                # print(f"Agregando transición: {Valor}")
                # agrego la adyacencia

    def ingresarEstado(self, dato, esAceptacion:bool = False, esInicial:bool = False):
        if not self.verificarEstado(dato, self.ListaEstados):
            if esInicial:
                if not self.verificarEstadoInicial(dato):
                    self.ListaEstados.append(Estado(dato, esAceptacion, esInicial))
                else:
                    print("Ya existe un estado inicial")
            else:
                self.ListaEstados.append(Estado(dato, esAceptacion, esInicial))
        else:
            print("El estado ya existe, intente nuevamente")

    def verificarEstado(self, estado, listaEstados):
        for i in range(len(listaEstados)):
            if estado == listaEstados[i].getDato():
                return True
        return False
    
    def verificarEstadoInicial(self, dato):
        for estado in self.ListaEstados:
            if estado.getDato() == dato and estado.getEstadoInicial():
                return True
        return False
    
    def verificarEstadoAceptacion(self, dato):
        for estado in self.ListaEstados:
            if estado.getDato() == dato and estado.getEstadoAceptacion():
                return True
        return False

    def imprimirEstados(self):
        print("Estados:")
        for i in range(len(self.ListaEstados)):
            Aceptar = "Estado aceptación" if self.ListaEstados[i].getEstadoAceptacion() else ""
            Inicio = "Estado inicial" if self.ListaEstados[i].getEstadoInicial() else ""
            print(f"Estado : {self.ListaEstados[i].getDato()} - {Aceptar} {Inicio}")
        print("---------------------------")

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
    
    def obtenerDestino(self, origen, valor):
        for transicion in self.ListaTransiciones:
            if transicion.origen == origen and transicion.valor == valor:
                return transicion.destino
        return None
    
    def obtenerEstados(self) -> List[str]:
        Out: List[str] = []
        for estado in self.ListaEstados:
            Out.append(estado.getDato())
        return Out

    def imprimirTransiciones(self):
        print("Transiciones:")
        for i in range(len(self.ListaTransiciones)):
            print("Origen: {0}  -  Destino: {1}  :  Valor:{2}".format(self.ListaTransiciones[i].getOrigen(), self.ListaTransiciones[i].getDestino(), self.ListaTransiciones[i].getValor()))
        print("-----------------------------------")

    def imprimirAutomata(self):
        print("Autómata:")
        self.imprimirTransiciones()
        self.imprimirEstados()
        print(self.Alfabeto)
        print(self.estadosAceptacion)
        print("-----------------------")
        
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
            if (transicion.origen == dato or transicion.destino == dato):
                self.ListaTransiciones.remove(transicion)
                self.borrarTransicion(dato)
                
    def actulizarListaAceptacion(self):
        self.estadosAceptacion.clear()
        for estado in self.ListaEstados:
            if estado.getEstadoAceptacion():
                self.estadosAceptacion.append(estado.getDato())
                
    def obtenerEstadosIncompletos(self) -> List[str]:
        Out: List[str] = []
        for estado in self.ListaEstados:
            salidas = []
            for transicion in self.ListaTransiciones:
                if(transicion.getOrigen() == estado.getDato()):
                    salidas.append(transicion.getValor())
            for letra in self.Alfabeto:
                if not letra in salidas:
                    Out.append(estado.getDato())
                    break
        return Out
    
    def obtenerSalidas(self, estado: Estado) -> List[str]:
        salidas: List[str] = []
        for transicion in self.ListaTransiciones:
            if transicion.getOrigen() == estado.getDato():
                salidas.append(transicion.getValor())
        return salidas
    
    def obtenerSalidasFaltantes(self, estado: Estado) -> List[str]:
        salidas = self.obtenerSalidas(estado)
        faltantes: List[str] = []
        for letra in self.Alfabeto:
            if not letra in salidas:
                faltantes.append(letra)
        return faltantes

    def esCompleto(self) -> bool:
        for estado in self.ListaEstados:
            salidas = []
            for transicion in self.ListaTransiciones:
                if(transicion.getOrigen() == estado.getDato()):
                    salidas.append(transicion.getValor())
            for letra in self.Alfabeto:
                if not letra in salidas:
                    return False
        return True
    
    def crearSumidero(self):
        self.ingresarEstado("Sum")
        for letra in self.Alfabeto:
            self.ingresarTransicion("Sum", "Sum", letra)
    
    def completar(self):
        if self.esCompleto(): return
        self.crearSumidero()
        incompletos = self.obtenerEstadosIncompletos()
        for incompleto in incompletos:
            faltantes = self.obtenerSalidasFaltantes(self.ObtenerO(incompleto))
            for faltante in faltantes:
                self.ingresarTransicion(incompleto, "Sum", faltante)
        self.imprimirAutomata()