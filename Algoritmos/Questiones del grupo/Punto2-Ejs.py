class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
raiz = Node("1")

raiz.left = Node("2")
raiz.left.left = Node("3")
raiz.left.right = Node("4")
raiz.left.right.left = Node("5")
raiz.left.right.right = Node("6")

raiz.right = Node("7")
raiz.right.right = Node("8")
raiz.right.right.left = Node("9")

print("-" *50)
print("INORDEN")

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.valor)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
        
#test
inorden(raiz)

print("-" *50)

print("POSTORDEN")

def postorden(n):
    if(n.left):
        postorden(n.left)
    if(n.right):
        postorden(n.right)
    print(n.valor)

postorden(raiz)

print("-" *50)
print("PREORDEN")

def preorden(n):
    print(n.valor)
    if(n.left):
        preorden(n.left)
    if(n.right):
        preorden(n.right)

preorden(raiz)
