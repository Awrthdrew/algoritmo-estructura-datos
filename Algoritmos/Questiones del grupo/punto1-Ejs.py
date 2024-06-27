class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
raiz = Node("8")

raiz.left = Node("9")
raiz.left.left = Node("11")
raiz.left.right = Node("7")
raiz.left.right.left = Node("3")
raiz.left.right.left.right = Node("2")
raiz.left.right.left.left = None
raiz.left.right.right = Node("1")
raiz.left.left.left = Node("15")
raiz.left.left.right = Node("20")
raiz.left.left.left.left = Node("19")
raiz.left.left.left.right = None
raiz.left.left.right.left = Node("21")
raiz.left.left.right.right = None   

raiz.right = Node("5")
raiz.right.right = Node("12")
raiz.right.right.left = Node("17")
raiz.right.right.left.left = Node("16")
raiz.right.right.left.right = None
raiz.right.right.right = Node("18")
raiz.right.left = Node("6")
raiz.right.left.left = Node("4")
raiz.right.left.left.left = Node("13")
raiz.right.left.left.right = None
raiz.right.left.right = Node("14")
raiz.right.left.right.left = Node("10")
raiz.right.left.right.right = None


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
