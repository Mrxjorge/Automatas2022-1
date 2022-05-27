from Controlador.Automata import *
from Controlador.Operaciones import *

A = Automata()

A.cargar_automata('Data/automata1.json')

# B = Automata()

# B.cargar_automata('Data/automata2.json')

O = Operaciones()

# complemento = O.complemento(A)
# complemento.imprimirAutomata()

# A.invertirTransiciones()

A.borrarEstado('1')
A.imprimirAutomata()