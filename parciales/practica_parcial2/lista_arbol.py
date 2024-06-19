class Nodo:
    papucho = None
    right = None
    left = None
    
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return(str(self.valor))
    def __gt__(self, otro):
        return self.valor > otro.valor
    def __lt__(self, otro):
        return self.valor < otro.valor
    def __ge__(self, otro):
        return self.valor >= otro.valor
    def __le__(self, otro):
        return self.valor <= otro.valor
    
raiz = Nodo("Dios")
raiz.left = Nodo("Adán y Eva")

def inorden(nodo, nodos = []):
    if(nodo.left):
        inorden(nodo.left, nodos)
    nodos.append(nodo)
    
    if(nodo.right):
        inorden(nodo.right, nodos)
    return nodos


