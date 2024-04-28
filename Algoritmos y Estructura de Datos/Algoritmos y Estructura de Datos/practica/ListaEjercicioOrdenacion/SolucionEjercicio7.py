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


caminos = []

#ejercicio 7 con pre orden
def print_caminos(tree):
    if tree == None:  return

    global caminos
    caminos.append(tree)
    print_caminos(tree.left)

    #cuando llega en una hoja imprime el camino
    if(tree.left ==None and tree.right==None):
        print(*caminos)

    print_caminos(tree.right)
    caminos.remove(tree)


# test
print_caminos(raiz)

