from Controlador.Automata import *
from Controlador.Operaciones import *

A = Automata()

A.cargar_automata('Data/automata1.json')

print("-----------------------------------------------")

B = Automata()

B.cargar_automata('Data/automata2.json')

O = Operaciones()
O.unionAutomatas(A, B)
O.interseccionAutomatas(A, B)

# complemento = O.complemento(A)
# complemento.imprimirAutomata()

# A.invertirTransiciones()
# A.borrarEstado('3')
# A.imprimirAutomata()

# O.reverso(B)