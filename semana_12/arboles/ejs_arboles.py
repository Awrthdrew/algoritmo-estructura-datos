#1. ¿Cuáles son las secuencias que se encuentran al atravesar el siguiente árbol en Inorden, Preorden y Postorden?

"""class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

# ÁRBOL SIN NINGÚN ORDEN     
raiz = Node("8")

raiz.left = Node("9")

raiz.left.left = Node("11")
raiz.left.right = Node("7")

raiz.left.left.right = Node("20")
raiz.left.left.left = Node("15")
raiz.left.right.right = Node("1")
raiz.left.right.left = Node("3")

raiz.left.right.left.right = Node("2")
raiz.left.left.left.left = Node("19")
raiz.left.left.right.left = Node("21")

raiz.right = Node("5")

raiz.right.right = Node("12")
raiz.right.left = Node("6")

raiz.right.right.right = Node("18")
raiz.right.right.left = Node("17")
raiz.right.left.left = Node("4")
raiz.right.left.right = Node("14")

raiz.right.left.left = Node("13")
raiz.right.left.right.right = Node("10")
raiz.right.right.left.right = Node("16")
                                   
# ÓRDENES DE RECORRIDO                   

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.valor)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
        
def preorden(n):
    #visitar nodo
    print(n.valor)
    #pasar por nodo izquierdo
    if(n.left):
        preorden(n.left)
    #pasar por nodo derecho
    if(n.right):
        preorden(n.right)
        
def postorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        postorden(n.left)
    #pasar por nodo derecho
    if(n.right):
        postorden(n.right)
    #visitar nodo
    print(n.valor)

def anchura_niveles():
    nivel = []
    
    if nodos: 
        for n in nodos:
            if (n.left):
                nivel.append(n.left)
            if (n.right):
                nivel.append(n.right)
            print(n.valor)
        anchura_niveles(nivel)
    
#inorden(raiz)
#preorden(raiz)
#postorden(raiz)
# anchura_niveles()"""
    
    
#3. Implementar los 3 tipos de recorridos de un árbol binario de búsqueda para verificar la solución.

"""class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

raiz = Node("A")

raiz.left = Node("B")

raiz.left.right = Node("D")

raiz.left.right.left = Node("G")
raiz.left.right.right = Node("H")

raiz.left.right.right.left = Node("J")

raiz.right = Node("C")

raiz.right.right = Node("F")
raiz.right.left = Node("E")

raiz.right.left.left = Node("I")

raiz.right.left.left.left = Node("K")

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.valor)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
        
def preorden(n):
    #visitar nodo
    print(n.valor)
    #pasar por nodo izquierdo
    if(n.left):
        preorden(n.left)
    #pasar por nodo derecho
    if(n.right):
        preorden(n.right)
        
def postorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        postorden(n.left)
    #pasar por nodo derecho
    if(n.right):
        postorden(n.right)
    #visitar nodo
    print(n.valor)
    
    
#inorden(raiz)
#preorden(raiz)
#postorden(raiz)"""

#4. Para el árbol anterior (Punto 3) implemente el recorrido de profundidad en anchura primero e imprima en pantalla.
"""class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

raiz = Node("A")

raiz.left = Node("B")

raiz.left.right = Node("D")

raiz.left.right.left = Node("G")
raiz.left.right.right = Node("H")

raiz.left.right.right.left = Node("J")

raiz.right = Node("C")

raiz.right.right = Node("F")
raiz.right.left = Node("E")

raiz.right.left.left = Node("I")

raiz.right.left.left.left = Node("K")


def verificarHijo(nodo):
    if (nodo.left or nodo.right):
        return True
    else:
        return False
    
def anchura(nodos):
    nivel = []
    if nodos:cf
        for nodo in nodos:
            if verificarHijo(nodo):
                hijos = []
                if nodo.left:
                    hijos.append(nodo.left.valor)
                if nodo.right:
                    hijos.append(nodo.right.valor)
                print(f'El nodo {nodo.valor} tiene a sus hijos {hijos}')
            else:
                print(f'El nodo {nodo.valor} no tiene hijos')
            if (nodo.left):
                nivel.append(nodo.left)
            if (nodo.right):
                nivel.append(nodo.right)
        anchura(nivel)
anchura([raiz])"""

"""5. Considerando la implementación de la árbol anterior, incluir en la clase nodo, el puntero para el padre y hacer funciones para determinar los siguientes puntos.
a. Nodo interno: Un nodo con al menos un hijo. La función recibe un nodo y retorna un booleano.
b. Grado: Número de sub_árboles de un nodo. La función recibe un nodo y retorna un numero.
c. Nivel: El nivel de un nodo se define por 1 + (el número de brazos entre el nodo y la raíz). La función recibe un nodo y retorna un número.
d. Altura de un nodo: La altura de un nodo es el número de brazos en el camino más largo entre ese nodo y una hoja. La función recibe un nodo y retorna un número.
e. Altura de un árbol: La altura de un árbol es la altura de su nodo raíz. La función recibe un nodo y retorna un número.
f. Profundidad: La profundidad de un nodo es el número de brazos desde la raíz del árbol hasta un nodo. La función recibe un nodo y retorna un número.
g. Rama: Una ruta del nodo raíz a cualquier otro nodo. La función recibe dos nodos (punto inicial y punto final) y retorna una string con el camino."""

"""class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

raiz = Node("A")

raiz.left = Node("B")

raiz.left.right = Node("D")

raiz.left.right.left = Node("G")
raiz.left.right.right = Node("H")

raiz.left.right.right.left = Node("J")

raiz.right = Node("C")

raiz.right.right = Node("F")
raiz.right.left = Node("E")

raiz.right.left.left = Node("I")

raiz.right.left.left.left = Node("K")"""

#A NODO INTERNO
"""def nodo_interno(nodos):
    if nodos.left or nodos.right:
        return True
    else:
        return False
print(nodo_interno(raiz))"""


#B NODO GRADO
"""def nodo_grado(nodos):
    nivel = []
    if nodos:
        for n in nodos:
            grado = 0
            if n.left:
                nivel.append(n.left)
                grado += 1
            if n.right:
                nivel.append(n.right)
                grado += 1
            print(f'El nodo {n.valor} tiene grado: N° {grado}')
        nodo_grado(nivel)
nodo_grado([raiz])"""
            
#C
"""nivelNodo = 0

def nodo_nivel(nodos, nodoBuscado):
    nivel = []
    global nivelNodo
    if nodos:
        for n in nodos:
            if n.valor == nodoBuscado:
                print(f'El nodo {n.valor} está en el nivel {nivelNodo}')
            if (n.right):
                nivel.append(n.right)
            if (n.left):
                nivel.append(n.left) 
        nivelNodo += 1
        nodo_nivel(nivel, "E")
nodo_nivel([raiz], "E")"""
 
#D 
"""def nodo_altura(nodo):
    if nodo == None:
        return 0
    else:
        return 1 + max(nodo_altura(nodo.left), nodo_altura(nodo.right))"""

#7
"""caminos = []

def print_caminos(arbol):
    if arbol == None: 
        
        global caminos
        caminos.append(arbol)
        print_caminos(arbol.left)
    
    #CUANDO LLEGA EN UNA HOJA IMPRIME EL CAMINO
    if arbol.left == None and arbol.right == None:
        print(*caminos)
    
    print_caminos(arbol.right)
    caminos.remove(arbol)
    
print_caminos(raiz)"""

# Pasar de un árbol a un array con orden de anchura de árbol
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
    def __str__(self):
        return self.valor

    def __repr__(self):
        return self.valor
# ÁRBOL SIN NINGÚN ORDEN     
raiz = Node("8")

raiz.left = Node("9")

raiz.left.left = Node("11")
raiz.left.right = Node("7")

raiz.left.left.right = Node("20")
raiz.left.left.left = Node("15")
raiz.left.right.right = Node("1")
raiz.left.right.left = Node("3")

raiz.left.right.left.left = Node("2")
raiz.left.left.left.left = Node("19")
raiz.left.left.right.left = Node("21")

raiz.right = Node("5")

raiz.right.right = Node("12")
raiz.right.left = Node("6")

raiz.right.right.right = Node("18")
raiz.right.right.left = Node("17")
raiz.right.left.left = Node("4")
raiz.right.left.right = Node("14")

raiz.right.left.left.left = Node("13")
raiz.right.left.right.left = Node("10")
raiz.right.right.left.left = Node("16")


# Árbol con orden de anchura
arrayArbol = []
def arbol_to_array_anchura(nodo):
    nivel = []
    global arrayArbol
    if nodo:
        for n in nodo:
            if n is None:
                arrayArbol.append(None)
            else:
                arrayArbol.append(n)
                if n.left or n.right:
                    nivel.append(n.left)
                    nivel.append(n.right)
        arbol_to_array_anchura(nivel)
    return arrayArbol

print(*arbol_to_array_anchura([raiz]))
#SE AGREGA EL * PARA QUE DEVUELVA EN FORMA DE STR, SIN CORCHETES Y COMILLAS
