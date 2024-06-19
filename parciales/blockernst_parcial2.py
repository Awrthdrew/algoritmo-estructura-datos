import json
import csv

"""
1. Ordenación
Dada la siguiente información construir utilizando POO las instacias correspondientes y ponerlas dentro de una lista. 
Luego ordenar la lista utilizando el método que te tocó en el papel según promedio de cantidad de goles por partido

Jugadores selección:
1) Messi:
    * Peso: 70KG
    * Goles: 1000
    * Partidos: 800
    
2) DiMaría:
    * Peso: 73KG
    * Goles: 700
    * Partidos: 900
    
3) Martinez:
    * Peso: 91KG
    * Goles: 0
    * Partidos: 200
    
4) Paredes:
    * Peso: 82KG
    * Goles: 50
    * Partidos: 450
    

2. Árbol
Dado la siguiente estructura de árbol que contiene un DOM (Document Object Model) de HTML:

class Tag:
    def __init__(self, n, i):
        self.tag = n
        self.id = i
        self.childs = []

html = Tag("html", None)
html.childs.append(Tag("head", None))
html.childs.append(Tag("body", None))
html.childs[1].childs.append(Tag("header", None))
html.childs[1].childs.append(Tag("article", None))
html.childs[1].childs.append(Tag("footer", None))

html.childs[1].childs[1].childs.append(Tag("div", "content"))
html.childs[1].childs[1].childs[0].childs.append(Tag("p", "text"))
realizar una función recursiva que genere la siguiente salida:


<html>
    <head>
    </head>
    <body>
        <header>
        </header>
        <article>
            <div id="content">
                <p id="text">
                </p>
            </div>
        </article>
        <footer>
        </footer>
    </body>
</html>

3. 
"""
    
#1 ORDENACIÓN

class Jugador:
    def __init__(self, nombre_completo, peso, goles, partidos):
        self.nombre_completo = nombre_completo
        self.peso = peso
        self.goles = goles
        self.partidos = partidos
        
        
    def __str__(self):
        return self.nombre_completo + " * PARTIDOS: " + str(self.partidos) + " * GOLES: " + str(self.goles) 

    
    def promedio_goles_por_partido(self):
        if self.partidos >= 0:
            return self.goles / self.partidos
        else:
            return False
        
    def to_dict(self): # Método para convertir a diccionario el objeto
        return {
            'nombre_completo': self.nombre_completo,
            'peso': self.peso,
            'goles': self.goles,
            'partidos': self.partidos,
            'promedio_goles_por_partido': self.promedio_goles_por_partido()
        }

 
once_inicial = [
                Jugador("Lionel Andrés MESSI", 70, 1000, 800), 
                Jugador("Ángel DI MARÍA", 73, 700, 900 ),
                Jugador("Lautaro MARTÍNEZ", 91, 0, 200 ),
                Jugador("Leandro PAREDES", 82, 50, 450)
               ]


# BUBBLE SORT
def bubbleSort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j].promedio_goles_por_partido() > lista[j+1].promedio_goles_por_partido():
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux #ESTÁ DECRECIENTE, SI PONE - EN VEZ DE + SERÁ ASCECENDENTE
   
                
# INSERTION SORT
def insertionSort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j].promedio_goles_por_partido() > key.promedio_goles_por_partido():
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
        
        
# QUICK SORT 
def partition(array, low, high):
  # seleccionar el último elemento del array como pivot
  pivot = array[high].promedio_goles_por_partido()
  # esta variable la usaremos para señalar elementos mas grandes que el pivot
  i = low - 1
  # Buscar todos los elementos menores al pivot y reubicarlos
  for j in range(low, high):
    if array[j].promedio_goles_por_partido() <= pivot:
      # Si hay un elemento menor que el pivot intercamabiarlos por el de la position i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  # finalmente, intercamabiar el pivot por el contenido del siguiente lugar de i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  # Retornar la posición dónde se partió
  return i + 1


def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    # ordenar a la izq del punto particionado
    quickSort(array, low, pi - 1)
    # ordenar a la derecha del punto particionado
    quickSort(array, pi + 1, high)


# MERGE SORT
def mergeSort(array):
    if len(array) > 1:

        #FASE de dividir el array en 2 partes
        
        # middle es el puntero donde el array es dividido en 2 subarrays
        middle = len(array) // 2
        L = array[:middle] #mitad izquierda
        R = array[middle:] #mitad derecha

        # Ordenar las 2 mitades
        mergeSort(L)
        mergeSort(R)
        
        #FASE de hacer el merge de los subarrays

        # necesitamos 3 punteros:
        # 2 para para ir señalando elementos en los subarrays (mitades)
        # y un 3ro para usar con el el array combinado arbol_htmlante
        i = j = k = 0


        # Recorrer tanto el subarrays L como M hasta alcanzar el final de alguno
        # de ellos. Compara el elemento de L contra el de M y reubicar en el
        # array general
        while i < len(L) and j < len(R):
            if L[i].promedio_goles_por_partido() < R[j].promedio_goles_por_partido():
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Pasamos los restantes elemenos de L al array general 
        # (en el caso que M tenga menos elementos que L)
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        # Lo mismo que lo anterior pero si M tenía más elementos que L
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    
    
# ORDENAMIENTO A USAR
    
#bubbleSort(once_inicial) 
#insertionSort(once_inicial)
#quickSort(once_inicial, 0, len(once_inicial)-1)
#mergeSort(once_inicial)


# PRINT DE LOS JUGADORES ORDENADOS POR PROMEDIO DE GOLES POR PARTIDO
"""for jugador in once_inicial:
    promedio = round(jugador.promedio_goles_por_partido(), 2)
    print(jugador)
    print(f"Promedio de {jugador.nombre_completo} por partido: ", promedio)
    print()"""
    

# 2 ESTRUCTURA DE ÁRBOL HTML
class Tag:
    def __init__(self, nodo, identacion):
        self.tag = nodo
        self.id = identacion
        self.childs = []

html = Tag("html", None)
html.childs.append(Tag("head", None))
html.childs.append(Tag("body", None))
html.childs[1].childs.append(Tag("header", None))
html.childs[1].childs.append(Tag("article", None))
html.childs[1].childs.append(Tag("footer", None))
html.childs[1].childs[1].childs.append(Tag("div", "content"))
html.childs[1].childs[1].childs[0].childs.append(Tag("p", "text"))

def print_html(tag, indent=''):
    arbol_html = []
    if tag.id:
        arbol_html.append(f"{indent}<{tag.tag} id='{tag.id}'>")
    else:
        arbol_html.append(f"{indent}<{tag.tag}>")
    for child in tag.childs:
        arbol_html.append(print_html(child, indent + '    '))
    arbol_html.append(f"{indent}</{tag.tag}>")
    return '\n'.join(arbol_html)

# Generar la estructura HTML como una cadena
html_structure = print_html(html)

# Imprimir la estructura HTML
print(html_structure)

# Guardar la estructura HTML en un archivo
with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\parciales\estructura_html.html', "w", encoding='utf8', newline="\n") as file:
    file.write(html_structure)


