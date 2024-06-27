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


Postorden(raiz)