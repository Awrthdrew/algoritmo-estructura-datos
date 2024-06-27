class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor


# raiz = Node(8)

# raiz.left = Node(9)
# raiz.right = Node(5)

# raiz.left.left = Node(11)
# raiz.left.right = Node(7)
# raiz.right.left = Node(6)
# raiz.right.right = Node(12)

# raiz.left.left.left = Node(15)
# raiz.left.left.right = Node(20)
# raiz.left.right.left = Node(3)
# raiz.left.right.right = Node(1)
# raiz.right.left.left = Node(4)
# raiz.right.left.right = Node(14)
# raiz.right.right.left = Node(17)
# raiz.right.right.right = Node(18)

# raiz.left.left.left.left = Node(19)
# raiz.left.left.right.left = Node(21)
# raiz.left.right.left.left = Node(2)
# raiz.right.left.left.left = Node(13)
# raiz.right.left.right.left = Node(10)
# raiz.right.right.left.left = Node(10)
#--------------------------------------------Inorden = 12345678910 ---------------------------------------------
# raiz = Node(5)

# raiz.left = Node(4)
# raiz.left.left = Node(2)
# raiz.left.left.left = Node(1)
# raiz.left.left.right = Node(3)

# raiz.right = Node(9)
# raiz.right.left = Node(7)
# raiz.right.left.left = Node(6)
# raiz.right.left.right = Node(8)
# raiz.right.right = Node(10)

#--------------------------------------------Ejercicio 3 -------------------------------------------------------

raiz = Node("A")

raiz.left = Node("B")
raiz.right = Node("C")

raiz.left.right = Node("D")
raiz.right.left = Node("E")
raiz.right.right = Node("F")

raiz.left.right.left = Node("G")
raiz.left.right.right = Node("H")
raiz.right.left.left = Node("I")

raiz.left.right.right.left = Node("J")
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
        

def Preorden(n):
    print(n.valor)

    if(n.left):
        Preorden(n.left)

    if(n.right):
        Preorden(n.right)

def Postorden(n):
    if(n.left):
        Postorden(n.left)

    if(n.right):
        Postorden(n.right)

    print(n.valor)

levels = []

def bredth(n, nivel = 0):
    global levels
    if n:
        if len(levels) == nivel:
            levels.append([])
        levels[nivel].append(n.valor)
        bredth(n.left, nivel + 1)
        bredth(n.right, nivel + 1)

#Depende como lo recorres si tendras en profundidad o bredth


def buscador(r, nodo):
    if r:
        buscador(r.left, nodo)
        buscador(r.right, nodo)
        if r.algo == nodo.algo:
            return r
        

def no_hojas(r):
    if r:
        if (r.left != None or r.right != None): #O tambien: if not (r.left != None or r.right != None):
            print(r.algo)

        no_hojas(r.left)
        no_hojas(r.right)

def recorrer(r, nivel = 0):
    global niveles
    if r:
        if len(niveles) == nivel:
            niveles.append([])
        niveles[nivel].append(r)
        recorrer(r.left, nivel + 1)
        recorrer(r.right, nivel + 1)


def recorrido_especifico(r, nivel, nivelReq):
    if r:
        if(nivel == nivelReq):
            print(r.algo)
        recorrido_especifico(r.left, nivel + 1, nivelReq)
        recorrido_especifico(r.right, nivel + 1, nivelReq)
    


bredth(raiz)
print(levels)

#------------------------------------------------------------------Burbuja------------------------------------------------------------------
"""
Ejercicios:
1) crear una clase Persona con los atributos nombre y edad
2) crear una lista y en la lista agregar 5 instancias de Persona diferentes
3) aplicar la ordenacion a la lista
"""

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @property
    def get_edad(self):
        return self.edad
    
    
    
p = persona("francisco", 19)
q = persona("bernardo", 18)
z = persona("franchesco", 30)
h = persona("francisco", 32)
i = persona("jessie", 23)

array_personas = [p,q,z,h,i]

for i in range(len(array_personas)):
    print(array_personas[i].get_edad)


def ordenar_burbuja(array_personas):
    for i in range(len(array_personas) - 1):
        print(i)
        for j in range(len(array_personas)-i-1):
            if array_personas[j].get_edad > array_personas[j + 1].get_edad:
                aux = array_personas[j]
                array_personas[j] = array_personas[j+1]
                array_personas[j+1] = aux
    
ordenar_burbuja(array_personas)

print("------------------------------------------------ Despues de Iteracion-----------------------------------------")

for i in range(len(array_personas)):
    print(array_personas[i].get_edad)




"""

class persona_sin:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    

    def get_edad(self):
        return self.edad
    




pl = persona("francisco", 19)
ql = persona("bernardo", 18)
zl = persona("franchesco", 30)
hl = persona("francisco", 32)
il = persona("jessie", 23)

array_personas = [pl,ql,zl,hl,il]

for i in array_personas:
    print(i.get_edad)


def ordenar_burbuja(array_personas):
    for i in range(len(array_personas)-1):
        for j in range(len(array_personas)-i-1):
            if array_personas[j].get_edad > array_personas[j + 1].get_edad:
                aux = array_personas[j]
                array_personas[j] = array_personas[j+1]
                array_personas[j+1] = aux
    
"""

#-----------------------------------------------------------------------Insercion-------------------------------------------------
def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
print('Original: ')
print(data)
insertion_sort(data)
print('Ordenado: ')
print(data)

class autos:
    def __init__(self, nombre, patente):
        self.nombre = nombre
        self.patente = patente
class motos:
    def __init__(self, nombre, patente):
        self.nombre = nombre
        self.patente = patente

Toyota = autos("SupraMK4", 334)
Yamaha = motos("Tz250", 455)
Honda = autos("NSX", 122)
KTM = motos("Duke290", 334)
Nissan = autos("SilviaS15", 123)

autosmotos = [Toyota, Yamaha, Honda, KTM, Nissan]


"""

"""



def insertion_sort(autosmotos):

    for step in range(1, len(autosmotos)):
        key = autosmotos[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key.nombre < autosmotos[j].nombre:
            autosmotos[j + 1] = autosmotos[j]
            j = j - 1
            print(autosmotos[j + 1].nombre)
            print(autosmotos[j].nombre)
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        autosmotos[j + 1] = key


insertion_sort(autosmotos)


for x in autosmotos:
    print(str(x.nombre) + " Patente: " + str(x.patente))

#-------------------------------------------------------Arboles no binarios---------------------------------
class Node:
    valor = ""
    subnodes = None
    def __init__(self, valor, numero):
        self.valor = valor
        self.numero = numero
        self.subnodes = []
        
#https://es.wikipedia.org/wiki/Taxonom%C3%ADa#/media/Archivo:Taxonomia-y-filogenia.gif
raiz = Node("Transporte", 3)
raiz.subnodes.append(Node("Automotor", 2))
raiz.subnodes.append(Node("Ciclomotor", 1))
raiz.subnodes.append(Node("Bicicleta", 4))
raiz.subnodes.append(Node("Cuadrúpedo", 7))

raiz.subnodes[0].subnodes.append(Node("Terrestre", 1))
raiz.subnodes[0].subnodes.append(Node("Aéreo", 7))
raiz.subnodes[0].subnodes.append(Node("Matítimo", 9))

raiz.subnodes[0].subnodes[0].subnodes.append(Node("Autos", 7))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Tren", 3))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Colectivos", 5))

raiz.subnodes[3].subnodes.append(Node("Caballo", 6))
raiz.subnodes[3].subnodes.append(Node("Camello", 4))
raiz.subnodes[3].subnodes.append(Node("Mula", 9))


def recorrer(r, sangria = ""):
    print(sangria + r.valor + "\n")
    sangria += "  "    
    for i in r.subnodes:
        recorrer(i, sangria)
    
recorrer(raiz)

"""
Para agregar:
1) medios de transporte aéreos
2) bajo "Autos" agregar marcas de autos
"""

#------------------------------------------------------------Lista Enlasada-------------------------------------------------------------------------------------
class Nodo: 
    def __init__(self, x):
        self.nombre = x
        self.Next_nodo = None

    def __str__(self):
        return self.nombre

raiz = Nodo("Algo")
raiz.Next_nodo = Nodo("Otro")
raiz.Next_nodo.Next_nodo = Nodo("Otro mas")
raiz.Next_nodo.Next_nodo.Next_nodo = Nodo("Another one mannn")

def mostrar(n):
    while n != None:
        print(n)
        n = n.Next_nodo 

def agr_prin(x):
    global raiz 
    nuevaRaiz = Nodo(x)
    nuevaRaiz.Next_nodo = raiz 
    raiz = nuevaRaiz

def agr_fin(x):
    global raiz
    i = raiz
    while i.Next_nodo != None:
        i = i.Next_nodo
    
    i.Next_nodo = Nodo(x)

def agr_pos(x, p):
    global raiz
    i = raiz
    pos = 1
    ant = None
    while i.Next_nodo != None and pos != p:
        ant = i
        i = i.Next_nodo
        pos += 1
    if i.Next_nodo == None:
        i.Next_nodo = Nodo(x)
    elif p == 1:
        agr_prin(x)
    else:
        nodo = Nodo(x)
        nodo.Next_nodo = ant.Next_nodo
        ant.Next_nodo = nodo

def sacar_prin():
    global raiz
    if raiz != None:
        raiz = raiz.Next_nodo

def sacar_fin():
    global raiz
    if raiz == None:
        return
    if raiz.Next_nodo == None:
        raiz = None
        return
    i = raiz
    while i.Next_nodo.Next_nodo != None:
        i = i.Next_nodo
    i.Next_nodo = None

def sacar_posicion(p, cantidad):
    global raiz
    if p == 1:
        for _ in range(cantidad):
            sacar_prin()
    else:
        i = raiz
        pos = 1
        ant = None
        while i.Next_nodo != None and pos != p:
            ant = i
            i = i.Next_nodo
            pos += 1
        for _ in range(cantidad):
            if i.Next_nodo != None:
                ant.Next_nodo = i.Next_nodo
                i.Next_nodo = None

def sacar_elementos(p, cantidad):
    sacar_posicion(p, cantidad)

agr_prin("ABC")
agr_pos("-<>-<>-<>-", 4)
agr_fin("XYZ")
mostrar(raiz)

print("-" * 50)

sacar_elementos(1, 0) #primero la posicion y despues la cantidad de elementos a partir de esa posicion
print("\nDespues de sacar los elementos a partir de la posicion X:\n")
mostrar(raiz)

print("-" * 50)


#----------------------------------------------------------------Parcial Eve--------------------------------------------------------------------

class pizzas:
    def __init__(self, t, c, co, p, nombre):
        self.tiempo = t
        self.costo = c
        self.complejidad = co
        self.porciones = p
        self.nombre = nombre

    def sacar_promedio(self):
        return self.costo / self.porciones

class Guiso_Lentejas:
    def __init__(self, t, c, co, p, nombre):
        self.tiempo = t
        self.costo = c
        self.complejidad = co
        self.porciones = p
        self.nombre = nombre

    def sacar_promedio(self):
        return self.costo / self.porciones

class Empanadas:
    def __init__(self, t, c, co, p, nombre):
        self.tiempo = t
        self.costo = c
        self.complejidad = co
        self.porciones = p
        self.nombre = nombre
    
    def sacar_promedio(self):
        return self.costo / self.porciones

class Milanesas_con_Pure:
        
    def __init__(self, t, c, co, p, nombre):
        self.tiempo = t
        self.costo = c
        self.complejidad = co
        self.porciones = p
        self.nombre = nombre        
        
    def sacar_promedio(self):
        return self.costo / self.porciones


pizza = pizzas(30, 500, "media", 4, "Pizza")
Guiso = Guiso_Lentejas(120, 900, "alta", 6, "Guiso")
empanadas = Empanadas(60, 740, "media", 4, "Empanadas")
Milas = Milanesas_con_Pure(30, 800, "baja", 4, "Milas")


array_comida = [Guiso, pizza, empanadas, Milas]


def insertion_sort(array_comida):
    for step in range(1, len(array_comida)):
        key = array_comida[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key.sacar_promedio() < array_comida[j].sacar_promedio():
            array_comida[j + 1] = array_comida[j]
            j = j - 1
            # print(array_comida[j + 1].nombre)
            # print(array_comida[j].nombre)
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        array_comida[j + 1] = key
insertion_sort(array_comida)
for x in array_comida:
    print(x.nombre)

#-----------------------------------------------------punto 2---------------------------

class Node:
    valor = ""
    subnodes = None
    def __init__(self, valor, numero):
        self.valor = valor
        self.numero = numero
        self.subnodes = []


Mundo = Node("Tierra", 100)

Mundo.subnodes.append(Node("Canada", 10)) 
Mundo.subnodes.append(Node("Argentina", 9)) 
Mundo.subnodes.append(Node("Chile", 6))

Mundo.subnodes[0].subnodes.append(Node("Northern", 8))
Mundo.subnodes[0].subnodes.append(Node("Southern", 10))
Mundo.subnodes[0].subnodes.append(Node("Western", 7))
Mundo.subnodes[0].subnodes.append(Node("Costal", 5))

Mundo.subnodes[0].subnodes[1].subnodes.append(Node("Edmonton", 10))
Mundo.subnodes[0].subnodes[1].subnodes.append(Node("Calgary", 9))
Mundo.subnodes[0].subnodes[1].subnodes.append(Node("Red-Deer", 7))



def recorrer(r, sangria = ""):
    print(sangria + r.valor + "\n")
    sangria += "  "    
    for i in r.subnodes:
        recorrer(i, sangria)
    

def recorrer_nivel_arbol(nodo, nivel_deseado, nivel_actual=0):
    if nivel_actual == nivel_deseado:
        print(nodo.valor)
    elif nivel_actual < nivel_deseado:
        for subnodo in nodo.subnodes:
            recorrer_nivel_arbol(subnodo, nivel_deseado, nivel_actual + 1)

def recorrer_nodo_especifico(nodo, valor_deseado):
    if nodo.valor == valor_deseado:
        print(nodo.valor)
        for x in nodo.subnodes:
            print(x.valor)
            recorrer_nodo_especifico(x, valor_deseado)

        # Realizar el recorrido a partir de este nodo, si es necesario
        # Puedes agregar aquí la lógica adicional para recorrer los subnodos
        
    for subnodo in nodo.subnodes:
        recorrer_nodo_especifico(subnodo, valor_deseado)

def recorrer_profundidad(nodo):
    if len(nodo.subnodes) != 0:
            for x in nodo.subnodes:
                recorrer_profundidad(x)
    else:
        for x in nodo.subnodes:
            print(x.valor)
            recorrer_profundidad(x, nodo)
        

recorrer_profundidad(Mundo)

#Hacer: Busqueda en profundidad, con los numeros

#-------------------------------------------------------------------------respuesta macaca -------------------------
class Node:
    valor = ""
    left = None
    right = None
    def _init_(self, valor):
        self.valor = valor

    def _str_(self):
        return self.valor
        
#crea la arbol del ejercicio 7
raiz = Node("B")

raiz.left = Node("U")
raiz.left.left = Node("E")
raiz.left.right = Node("R")
raiz.left.right.right  = Node("R")
raiz.left.right.right.left = Node("A")
raiz.left.right.right.right = Node("O")
raiz.left.right.right.right.left = Node("S")

raiz.left.left.left = Node("N")
raiz.left.left.left.left = Node("O")
raiz.left.left.left.right = Node("A")
raiz.left.left.left.right.right = Node("S")

raiz.right = Node("I")
raiz.right.right = Node("L")
raiz.right.left = Node("E")
raiz.right.left.left = Node("N")

raiz.right.right.left = Node("B")
raiz.right.right.left.left = Node("A")
raiz.right.right.left.left.left = Node("O")


caminos = [] # lista vacia que se va a usar para almacenar los nodos visitados durante la exploracion de caminos

#ejercicio 7 con pre orden

#Encuentra y miuestra todos los caminos desde la raiz hasta la hoja del arbol usando pre-orden

def print_caminos(tree): #se define la funcion que toma un nodo "tree" como parametro
    if tree == None:  return #si el nodo tree es None no hay nada mas que explorar en el camino y no hace mas nada

    global caminos
    caminos.append(tree) #se agrega el nodo actual tree a la lista "caminos" 
    print_caminos(tree.left) #se invoca recursivamente la función print_caminos en el hijo izquierdo del nodo actual (tree.left)

    #cuando llega en una hoja imprime el camino

    if(tree.left ==None and tree.right==None): #si el nodo actual es una hoja se imprime el camino completo que esta almacenado en "caminos"
        print(*caminos) #esto hace que desempaquete los elementos d ela lista y los imprima separados con espacios

    print_caminos(tree.right) #se invoca recursivamente la función print_caminos en el hijo derecho del nodo actual (tree.right)
    caminos.remove(tree) #se elimina el nodo actual ("tree") de la lista "caminos", esto es necesario para poder explorar otros caminos


# test
print_caminos(raiz)

"""
    - print_caminos encuentra y muestra todos los caminos desde la raíz hasta las hojas de un árbol binario 
    utilizando un enfoque de recorrido de preorden. Cada camino se muestra como una secuencia de nodos 
    visitados en orden desde la raíz hasta la hoja. La función utiliza una lista (caminos) para rastrear 
    los nodos visitados en cada camino y los imprime cuando alcanza una hoja.
"""

#---------------------------------------------------Polaco-----------------
class Node:
    valor = ""
    subnodes = None
    def _init_(self, valor, datos_extras):
        self.valor = valor
        self.datos_extras = datos_extras
        self.subnodes = []
        
#https://es.wikipedia.org/wiki/Taxonom%C3%ADa#/media/Archivo:Taxonomia-y-filogenia.gif
raiz = Node("Transporte",2)
raiz.subnodes.append(Node("Automotor",4))
raiz.subnodes.append(Node("Ciclomotor",5))
raiz.subnodes.append(Node("Bicicleta",-3))
raiz.subnodes.append(Node("Cuadrúpedo",8))

raiz.subnodes[0].subnodes.append(Node("Terrestre",6))
raiz.subnodes[0].subnodes.append(Node("Aéreo",7))
raiz.subnodes[0].subnodes.append(Node("Matítimo",7))

raiz.subnodes[0].subnodes[0].subnodes.append(Node("Autos",1))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Tren",3))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Colectivos",5))

raiz.subnodes[3].subnodes.append(Node("Caballo",1))
raiz.subnodes[3].subnodes.append(Node("Camello",0))
raiz.subnodes[3].subnodes.append(Node("Mula",-2))

"""
def recorrer(Node, sangria = "",promedio = []):
    if Node == None:
        return
    promedio.append(Node.datos_extras)
    print(sangria + Node.valor + "\n")
    sangria += "  "   
    for subnode in Node.subnodes:
        recorrer(subnode, sangria, promedio)
    if not Node.subnodes:
        #print(sum(promedio)/len(promedio))
        return (sum(promedio)/len(promedio))
"""


def es_ultimo_nodo(nodo):
    return len(nodo.subnodes) == 0

def recorrer(nodo, sangria = "",promedio = []):
    if nodo is None:
        return 0
    
    promedio.append(nodo.datos_extras)
    
    for i, subnodo in enumerate(nodo.subnodes):
        promedio.append(recorrer(subnodo))
        
        if es_ultimo_nodo(subnodo):
            print("Último nodo:", subnodo.valor)
    
    return (sum(promedio)/len(promedio))