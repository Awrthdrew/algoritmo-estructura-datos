class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
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
    los nodos visitados en cada camino y los imprime cuando alcanza una hoja.
"""
