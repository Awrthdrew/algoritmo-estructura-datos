"""lista = [6,5,3,1,8,7,2,4]

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            print("---------------------------------------")
            print("i: " + str(i) + " - j: " + str(j) + " => " + str(lista))
            print(str().rjust(j*3+16) + "-  -")
            if lista[j] > lista[j+1]:
                print("    Intercambiando: " + str(lista[j]) + " : " + str(lista[j+1]))
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                #lista[j], lista[j+1] = lista[j+1], lista[j]"""
    
"""
#Burbuja abreviado (muy mala performance)
def ordenar(lista):
    j = 0
    while(j < len(lista) - 1):
        if lista[j] > lista[j+1]:            
            lista[j], lista[j+1] = lista[j+1], lista[j]
            j = -1
        j += 1
"""        

         
"""#print("Antes: " + str(lista))
ordenar_burbuja(lista)
#ordenar(lista)
print("Despúes: " + str(lista))"""

"""
Ejercicios:
1) crear una clase Persona con los atributos nombre y edad
2) crear una lista y en la lista agregar 5 instancias de Persona diferentes
3) aplicar la ordenación a la lista
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return (self.nombre + ' - ' + str(self.edad))
    def __gt__ (self, greater_than): # __gt__ | Sirve para poder operar con < con objetos. LO HACE DESDE LA COMPARACIÓN DE LA CLASE (OBJETOS), NO CON LOS VALORES. 
        return self.edad < greater_than.edad 
    def __lt__(self, less_than): # __lt__ | Sirve para poder operar con < con objetos. LO HACE DESDE LA COMPARACIÓN DE LA CLASE (OBJETOS), NO CON LOS VALORES. 
        return self.edad < less_than.edad
    def __ge__(self, greather_equal_than):
        return self.edad >= greather_equal_than
    def __le__(self, less_equal_than):
        return self.edad <= less_equal_than
    

        
lista = [
        Persona("Andrew", 21), 
        Persona("Joaquín", 18),
        Persona("Franco", 20), 
        Persona("Mispi", 19), 
        Persona ("Helena", 22)
        ]

def burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j].edad > lista[j+1].edad:
                print("Intecambiando: " + str(lista[j]) + " : " + str(lista[j+1]))
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                #lista[j], lista[j+1] = lista[j+1], lista[j]  Resultado de la ordenación 
                

def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        print(f"\nIteración {step}: OBJETO = {key}")
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda hasta encontrar un valor menor a este
        while j >= 0 and key < array[j]:
            print(f"Comparando {key} con {array[j]}")
            array[j + 1] = array[j]
            j = j - 1
            print(f"Intercambio: {[(persona.nombre, persona.edad) for persona in array]}")
        # Ubicar el valor rescatado justo por delante del valor menor a este
        array[j + 1] = key
        print(f"Insertado {key} en posición {j + 1}: {[(persona.nombre, persona.edad) for persona in array]}")

# Función para determinar el pivot
def partition(array, low, high):
  # seleccionar el último elemento del array como pivot
  pivot = array[high]
  # esta variable la usaremos para señalar elementos mas grandes que el pivot
  i = low - 1
  
  # Buscar todos los elementos menores al pivot y reubicarlos
  for j in range(low, high):
    if array[j] <= pivot:
      # Si hay un elemento menor que el pivot intercamabiarlos por el de la position i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  # finalmente, intercamabiar el pivot por el contenido del siguiente lugar de i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  # Retornar la posición dónde se partió
  print("semiprocesado: ", end='')
  print(*array)
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    # ordenar a la izq del punto particionado
    quickSort(array, low, pi - 1)
    # ordenar a la derecha del punto particionado
    quickSort(array, pi + 1, high)
          
                
#burbuja(lista) 
#insertion_sort(lista)
quickSort(lista, 0, len(lista) -1)

print()
print("--- LISTA ORDENADA ---")
for persona in lista: #Arranca listando en el orden de la lista original, después itera por persona ordenandola con el que se elija.  
    print(persona)



"""
BUBBLE SORT

original: 20, 11, 16, 9, 12, 14, 17, 19, 13, 15

1°: 11, 16, 9, 12, 14, 17, 19, 13, 15, 20

2°: 11, 9, 12, 14, 16, 17, 19, 13, 15, 20

3°: 

INSERTION SORT

original: 20, 11, 16, 9, 12, 14, 17, 19, 13, 15

1°: 11, 20, 16, 9, 12, 14, 17, 19, 13, 15

2°: 11, 16, 20, 9, 12, 14, 17, 19, 13, 15

3°:
"""

