class Node:
    #left = None --- es lo mimso que declararlo abajo 

    def __init__(self, x):
        self.algo = x
        self.left = None
        self.right = None

#Level 0
Raiz = Node("X")
#Level 1
Raiz.left = Node("E")
Raiz.right = Node("L")
#Level 2
Raiz.left.left = Node("R")
Raiz.left.right = Node("O")
Raiz.right.left = Node("C")
Raiz.right.right = Node("A")
#Level 3
Raiz.right.right.left = Node("M")



niveles = []

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
    


#recorrer(Raiz)
#recorrido_especifico(Raiz, 0, 2)
#no_hojas(Raiz)

"""
for x, y in enumerate(niveles):
    print("Level: " + str(x))
    for a in y:
        print(a.algo)

"""

    