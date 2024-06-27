class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return self.valor


raiz = Node("A")
raiz.left = Node("B")
raiz.left.left = None
raiz.left.father = raiz
raiz.left.right = Node("D")
raiz.left.right.left = Node("G")
raiz.left.right.right = Node("H")
raiz.left.right.right.left = Node("J")
raiz.left.right.right.right = None
raiz.left.right.right.left.right = Node("M")

raiz.right = Node("C")
raiz.right.father = raiz
raiz.right.left = Node("E")
raiz.right.left.father=raiz.right.left
raiz.right.left.left = Node("I")
raiz.right.left.left.father=raiz.right.left
raiz.right.left.right = None
raiz.right.left.left.left = Node("K")
raiz.right.left.left.right = None
raiz.right.right = Node("F")
raiz.right.left.left.left = Node("K")
raiz.right.left.left.right = Node("L")



#ejercicio 4 - Recorrido en orden de anchura o recorrido por niveles
def print_width_search(tree): #Tree se refiere al nodo raiz del arbol
    if tree is None: #Si el arbol esta vacio osea None la funcion retorna sin hacer nada 
        return

    #Se crea una cola vacía llamada "queue" para almacenar los nodos del árbol que se imprimirán. Se inicializa la cola con el nodo raíz.
    queue = [tree]

    while queue: # Se ejecuta mientras "queue" no esta vacia, osea que mientras hayan nodos en la cola se seguira ejecutando el bucle
        node = queue.pop(0) #En cada iteracion del bucle se extrae el primer nodo usando el "pop". Se hace para seguir el orden de anchura
                                # donde los nodos se procesan en el orden que se agregaron a la cola. 
        print(node.valor, end=" ") #Se imprime el valor del nodo actual 
        if node.left is not None: #Se verifica si el nodo actual tiene un hijo izquierdo
            queue.append(node.left) #Si tiene uno lo agrega a la cola para que despues sea procesado
        if node.right is not None: #Se verifica si el nodo actual tiene un hijo derecho
            queue.append(node.right) #Si tiene uno lo agrega a la cola para que despues sea procesado

    #El bucle while se ejecuta hasta que no haya mas nodos en la cola, osea que ya fueron procesados todos los nodos del arbol. 

print_width_search(raiz)