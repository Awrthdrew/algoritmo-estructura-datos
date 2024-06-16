class Nodo:
    
    right = None
    left = None
    father = None

    def __init__(self, valor):
        self.valor = valor

    def __str__ (self):
        return str(self.valor)

    def __gt__ (self, otro):
        return self.valor > otro.valor
    def __lt__ (self, otro):
        return self.valor < otro.valor
    def __ge__(self, otro):
        return self.valor >= otro.valor
    def __le__(self, otro):
        return self.valor <= otro.valor

#INORDEN: 14 - 9 - 12 - 15 - 5 - 3 - 7
raiz = Nodo(5)
raiz.left = Nodo(12)
raiz.right = Nodo(7)
raiz.left.left =  Nodo(9)
raiz.left.right = Nodo(15)
raiz.left.left.left = Nodo(14)
raiz.right.left = Nodo(3)

def inorden(nodo, nodos=[]):
    

    if(nodo.left):
        inorden(nodo.left, nodos)

    nodos.append(nodo)

    if(nodo.right):
        inorden(nodo.right, nodos)

    return nodos

nodos_desordenados = inorden(raiz)
print('ARBOL EN ARRAY DESORDENADO: ')
print(*nodos_desordenados)

def partition(array, low, high):

  # seleccionar el último elemento del array como pivot
  pivot = array[high]

  # esta variable la usaremos para señalar elementos mas grandes que el pivot
  i = low - 1

  # Buscar todos los elementos menores al pivot y reubicarlos
  for j in range(low, high):
    if array[j] <= pivot:
      # Si hay un element menor que el pivot intercamabiarlos por el de la position i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  # finalmente, intercamabiar el pivot por el contenido del sigueinte lugar de i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # Retornar la posición dónde se partió
  #print("semiprocesado: ", end='')
  #print(array)
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    # ordenar a la izq del punto particionado
    quickSort(array, low, pi - 1)

    # ordenar a la derecha del punto particionado
    quickSort(array, pi + 1, high)


nodos_ordenados = nodos_desordenados
quickSort(nodos_ordenados, 0, len(nodos_ordenados)-1)
print('ARBOL EN ARRAY ORDENADO')
print(*nodos_ordenados)



def generarArbolOrdenado(array, nodo, indices=[]):
    indice_nodo = array.index(nodo)

    #indices.append(indice_nodo)
    
    
    if indice_nodo != 0:
        left = array[int((indice_nodo-1)/2)]
        nodo.left = left
        array_left = array[:indice_nodo]
        #print(*array_left)
        generarArbolOrdenado(array_left, left)
    else:
        nodo.left, nodo.right = None, None

    if indice_nodo != len(array)-1:       
        right = array[int( (len(array)-indice_nodo) / 2 + indice_nodo)]
        nodo.right = right
        array_right = array[(indice_nodo+1):]
        #print(*array_right)
        generarArbolOrdenado(array_right, right)
    else:
        nodo.left, nodo.right = None, None
    
    






indice_raiz = int((len(nodos_ordenados)-1) / 2)
raiz = nodos_ordenados[indice_raiz]
generarArbolOrdenado(nodos_ordenados, raiz)




def inorden_print(nodo):
    
    if(nodo.left):
        inorden_print(nodo.left)

    print(nodo)

    if(nodo.right):
        inorden_print(nodo.right)

print('ARBOL ESTABILIZADO: ')
inorden_print(raiz)


