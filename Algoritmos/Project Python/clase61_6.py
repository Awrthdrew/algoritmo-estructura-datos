class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
raiz = Node("F")

raiz.left = Node("B")
raiz.left.left = Node("A")
raiz.left.right = Node("D")
raiz.left.right.left = Node("C")
raiz.left.right.right = Node("E")

raiz.right = Node("G")
raiz.right.right = Node("I")
raiz.right.right.left = Node("H")

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
#test
Preorden(raiz)


alfabeto = {1: 'A', 2: 'B', 3: 'C', 4: 'D',
            5: 'E', 6: 'F', 7: 'G', 8: 'H',
            9: 'I', 10: 'J', 11: 'K', 12: 'L',
            13: 'M', 14: 'N', 15: 'O', 16: 'P',
            17: 'Q', 18: 'R', 19: 'S', 20: 'T',
            21: 'U', 22: 'V', 23: 'W', 24: 'X',
            25: 'Y', 26: 'Z'}