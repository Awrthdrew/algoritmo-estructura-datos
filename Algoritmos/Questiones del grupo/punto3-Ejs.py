class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
raiz = Node("a")

raiz.left = Node("b")
raiz.left.left = None
raiz.left.right = Node("d")
raiz.left.right.left = Node("g")
raiz.left.right.right = Node("h")
raiz.left.right.right.left = Node("j")
raiz.left.right.right.right = None 

raiz.right = Node("c")
raiz.right.right = Node("f")
raiz.right.left = Node("e")
raiz.right.left.right = None
raiz.right.left.left = Node("i")
raiz.right.left.left.left = Node("k")
raiz.right.left.left.right = None



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
