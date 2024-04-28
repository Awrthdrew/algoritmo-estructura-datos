"""
    Final AyED
    ----------
    07/12/2022    
    
    Dado el siguiente árbol binario, defina una función recursiva
    que retorne el valor máximo, el mínimo y el promedio.
    Considerar en la función que la cantidad de nodos del árbol es dinámica,
    es decir que puedo agregar un nodo más y poder recalcular.
    (no hay que agregar un nodo más, solo diseñar la recursivad para que
    sirva para un árbol con x cantidad de nodos)
    
    Enviar solución antes de las 19:30hs por email a nicolas.giqueaux@uap.edu.ar
"""

class Node:
    value = ""
    left = None
    right = None

    def __init__(self, value):
        self.value = value


root =  Node(20);
root.left =  Node(3);
root.left.left =  Node(10);
root.left.right =  Node(5);
root.left.right.left =  Node(4);
root.left.right.right =  Node(33);
root.right =  Node(13);
root.right.right =  Node(7);
root.right.right.left =  Node(23);
root.right.right.right =  Node(1);


promedio = 0
max = 0
min = 10000
count = 0

def recorrer(n):
    global max
    global min
    global promedio
    global count
    if(n.left):
        recorrer(n.left)

    if(n.right):
        recorrer(n.right)
    
    if n.value > max:
        max = n.value
    if n.value < min:
        min = n.value
    promedio += n.value
    count += 1

recorrer(root)
print("El valor maximo es: " + str(max) + ", El valor minimo es: " + str(min) + ", El valor promedio es: " + str(promedio / count))