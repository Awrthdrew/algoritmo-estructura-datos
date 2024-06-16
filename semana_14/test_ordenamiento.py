import time as t
import numpy as np
import random as r

# NUMPY ARRAY
lista = np.random.permutation(10001) # 0-10000 ELEMENTOS

"""for i in lista:
    print(f'{i}, ', end='')"""

# RANDOM ARRAY
#lista = [r.randint(0, 10) for _ in range(10)]
#print(data)

#-------------------------------------QUICK.SORT-------------------------------------------#
# Función para determinar el pivot
def partition(array, low, high):

  # seleccionar el último elemento del array como pivot
  pivot = array[high]

  # esta variable la usaremos para señalar elementos más grandes que el pivot
  i = low - 1

  # Buscar todos los elementos menores al pivot y reubicarlos
  for j in range(low, high):
    if array[j] <= pivot:
      # Si hay un elemento menor que el pivot intercambiarlo por el de la posición i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
      #print(f'Intercambio: {array[i]} <=> {array[j]} -> {array}')

  # finalmente, intercambiar el pivot por el contenido del siguiente lugar de i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  #t.sleep(1) 
  #print(f'Colocar pivot: {array[i + 1]} en la posición {i + 1} -> {array}')

  # Retornar la posición dónde se partió
  #print(f'Semiprocesado: {array}')
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    # ordenar a la izquierda del punto particionado
    quickSort(array, low, pi - 1)

    # ordenar a la derecha del punto particionado
    quickSort(array, pi + 1, high)


#print("Array original: ")
#print(lista)

quickSort(lista, 0, len(lista) - 1)

print('Luego de ordenar:')
print(lista)


#-------------------------------------INSERTION.SORT-------------------------------------------#
"""def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Iterar e ir comparando el valor rescatado con cada elemento de la izquierda hasta encontrar un valor menor a este
        while j >= 0 and key < array[j]:
            #print(f'Swap: {array[j]} > {key}, intercambiando posiciones {j} y {j+1}')
            array[j + 1] = array[j]
            j = j - 1

        # Ubicar el valor rescatado justo por delante del valor menor a este
        array[j + 1] = key
        #
        # 
        # 
        #t.sleep(1)
        #print(f'Colocar: {key} en la posición {j+1}')


print('Original:')
print(lista)
print()

insertion_sort(lista)
print()
print('Ordenado:')
print(lista)"""

#Tarda 5 segundos sin imprimir todos los swaps.
# +16 minutos si imprimo los swaps.