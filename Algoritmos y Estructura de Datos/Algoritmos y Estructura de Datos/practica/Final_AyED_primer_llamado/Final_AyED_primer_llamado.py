#    Dado el siguiente árbol binario, defina una función recursiva
#    que retorne el valor máximo, el mínimo y el promedio.
#    Considerar en la función que la cantidad de nodos del árbol es dinámica,
#    es decir que puedo agregar un nodo más y poder recalcular.
#    (no hay que agregar un nodo más, solo diseñar la recursivad para que
#    sirva para un árbol con x cantidad de nodos)    


class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(3)
root.left.left = Node(10)
root.left.right = Node(5)
root.left.right.left = Node(4)
root.left.right.right = Node(33)
root.right = Node(13)
root.right.right = Node(7)
root.right.right.left = Node(23)
root.right.right.right = Node(1)

def calcular(n):
    # TODO: completar la función recursiva
    pass

print("El valor máximo es: ")
print("El valor mínimo es: ")
print("El valor promedio es: ")
print("\n")
