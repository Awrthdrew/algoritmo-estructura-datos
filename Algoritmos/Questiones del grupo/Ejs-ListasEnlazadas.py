class Nodo: 
    def __init__(self, x):
        self.nombre = x
        self.nodo = None

    def __str__(self):
        return self.nombre

raiz = Nodo("Algo")
raiz.nodo = Nodo("Otro")
raiz.nodo.nodo = Nodo("Otro mas")
raiz.nodo.nodo.nodo = Nodo("Another one mannn")

def mostrar(n):
    while n != None:
        print(n)
        n = n.nodo 

def agr_prin(x):
    global raiz 
    nuevaRaiz = Nodo(x)
    nuevaRaiz.nodo = raiz 
    raiz = nuevaRaiz

def agr_fin(x):
    global raiz
    i = raiz
    while i.nodo != None:
        i = i.nodo
    
    i.nodo = Nodo(x)

def agr_pos(x, p):
    global raiz
    i = raiz
    pos = 1
    ant = None
    while i.nodo != None and pos != p:
        ant = i
        i = i.nodo
        pos += 1
    if i.nodo == None:
        i.nodo = Nodo(x)
    elif p == 1:
        agr_prin(x)
    else:
        nodo = Nodo(x)
        nodo.nodo = ant.nodo
        ant.nodo = nodo

def sacar_prin():
    global raiz
    if raiz != None:
        raiz = raiz.nodo

def sacar_fin():
    global raiz
    if raiz == None:
        return
    if raiz.nodo == None:
        raiz = None
        return
    i = raiz
    while i.nodo.nodo != None:
        i = i.nodo
    i.nodo = None

def sacar_posicion(p, cantidad):
    global raiz
    if p == 1:
        for _ in range(cantidad):
            sacar_prin()
    else:
        i = raiz
        pos = 1
        ant = None
        while i.nodo != None and pos != p:
            ant = i
            i = i.nodo
            pos += 1
        for _ in range(cantidad):
            if i.nodo != None:
                ant.nodo = i.nodo
                i.nodo = None

def sacar_elementos(p, cantidad):
    sacar_posicion(p, cantidad)

agr_prin("ABC")
agr_pos("-<>-<>-<>-", 4)
agr_fin("XYZ")
mostrar(raiz)

print("-" * 50)

sacar_elementos(1, 0) #primero la posicion y despues la cantidad de elementos a partir de esa posicion
print("\nDespués de sacar los elementos a partir de la posición X:\n")
mostrar(raiz)

print("-" * 50)

















"""
def agr_fin(x):
    global raiz
    nuevoNodo = Nodo(x)
    if raiz == None or raiz.nombre > nuevoNodo.nombre:
        nuevoNodo.nodo = raiz
        raiz = nuevoNodo
    else:
        auxiliar = raiz
        while auxiliar.nodo != None and auxiliar.nodo.nombre < nuevoNodo.nombre:
            auxiliar = auxiliar.nodo
        nuevoNodo.nodo = auxiliar.nodo
        auxiliar.nodo = nuevoNodo
"""