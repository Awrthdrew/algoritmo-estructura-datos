class Nodo:
    right = None
    left = None

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def __gt__(self, otro):
        return self.valor > otro.valor

    def __lt__(self, otro):
        return self.valor < otro.valor

    def __ge__(self, otro):
        return self.valor >= otro.valor

    def __le__(self, otro):
        return self.valor <= otro.valor

# INORDEN: 14 - 9 - 12 - 15 - 5 - 3 - 7
"""raiz = Nodo(5)
raiz.left = Nodo(12)
raiz.right = Nodo(7)
raiz.left.left = Nodo(9)
raiz.left.right = Nodo(15)
raiz.left.left.left = Nodo(14)
raiz.right.left = Nodo(3)"""

#ÁRBOL SIN ORDEN
raiz = Nodo(8)

raiz.left = Nodo(9)

raiz.left.left = Nodo(11)
raiz.left.right = Nodo(7)

raiz.left.left.right = Nodo(20)
raiz.left.left.left = Nodo(15)
raiz.left.right.right = Nodo(1)
raiz.left.right.left = Nodo(3)

raiz.left.right.left.left = Nodo(2)
raiz.left.left.left.left = Nodo(19)
raiz.left.left.right.left = Nodo(21)

raiz.right = Nodo(5)

raiz.right.right = Nodo(12)
raiz.right.left = Nodo(6)

raiz.right.right.right = Nodo(18)
raiz.right.right.left = Nodo(17)
raiz.right.left.left = Nodo(4)
raiz.right.left.right = Nodo(14)

raiz.right.left.left.left = Nodo(13)
raiz.right.left.right.left = Nodo(10)
raiz.right.right.left.left = Nodo(16)

def inorden(nodo, nodos=[]):
    if nodo.left:
        inorden(nodo.left, nodos)
    nodos.append(nodo)
    if nodo.right:
        inorden(nodo.right, nodos)
    return nodos

nodos_desordenados = inorden(raiz)
print('ARBOL EN ARRAY DESORDENADO: ')
print(*nodos_desordenados)


"""
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

nodos_ordenados = nodos_desordenados[:]
quickSort(nodos_ordenados, 0, len(nodos_ordenados) - 1)
print('ARBOL EN ARRAY ORDENADO')
print(*nodos_ordenados)


def ordenar_burbuja(personas):
    for i in range(len(personas)-1):
        for j in range(len(personas)-i-1):
            if personas[j] > personas[j+1]:
                aux = personas[j]
                personas[j] = personas[j+1]
                personas[j+1] = aux

nodos_ordenados = nodos_desordenados[:]
ordenar_burbuja(nodos_ordenados)
print('Nodos Después Ordenación BURBUJA: ')
print(*nodos_ordenados)

def insertion_sort(personas):
    for step in range(1, len(personas)):
        key = personas[step]
        j = step - 1 
        while j >= 0 and key < personas[j]:
            personas[j + 1] = personas[j]
            j = j - 1
        personas[j + 1] = key

nodos_ordenados = nodos_desordenados[:]
insertion_sort(nodos_ordenados)
print('Nodos Después Ordenación INSERTION: ')
print(*nodos_ordenados)
"""

def mergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2
        L = array[:middle] #mitad izquierda
        R = array[middle:] #mitad derecha
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:#EN CASO DE QUERER QUE ORDENE DESCENDENTE ES ASI || L[i] > R[j] ||
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

nodos_ordenados = nodos_desordenados[:] 
mergeSort(nodos_ordenados)
print('Nodos Después Ordenación MERGE: ')
print(*nodos_ordenados)

def construirArbol(array, inicio, fin):
    if inicio > fin:
        return None

    medio = (inicio + fin) // 2
    nodo = Nodo(array[medio].valor) 
    nodo.left = construirArbol(array, inicio, medio - 1)
    nodo.right = construirArbol(array, medio + 1, fin)
    return nodo

raiz = construirArbol(nodos_ordenados, 0, len(nodos_ordenados) - 1)

def inorden_print(nodo):
    if nodo.left:
        inorden_print(nodo.left)
    print(nodo)
    if nodo.right:
        inorden_print(nodo.right)
        
def inorden_str(nodo):
    result = ""
    if nodo.left:
        result += inorden_str(nodo.left)
    result += str(nodo) + "\n"
    if nodo.right:
        result += inorden_str(nodo.right)
    return result

arbol_str = inorden_str(raiz)



print('ARBOL ESTABILIZADO: ')
print(inorden_print(raiz))


with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\parciales\arbol_estabilizado.php', "w", encoding='utf8', newline="\n") as file:
    file.write(arbol_str)