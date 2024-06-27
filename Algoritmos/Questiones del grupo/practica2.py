#1
class Pizza:
    tiempo = 30
    complejidad = 'media'
    costo = 500
    porciones = 4

    def __init__(self, c, p):
        self.costo = c
        self.porciones = p
        self.nombre = 'Pizza'

    def Costo_por_Porcion(self):
        if self.porciones:
            return (self.costo / self.porciones)

class GuisoLentejas:
    tiempo = 120
    complejidad = 'alta'
    costo = 900
    porciones = 6

    def __init__(self, c, p):
        self.costo = c
        self.porciones = p
        self.nombre = 'Guiso de lentejas'

    def Costo_por_Porcion(self):
        if self.porciones:
            return (self.costo / self.porciones)

class Empanadas:
    tiempo = 60
    complejidad = 'media'
    costo = 740
    porciones = 4

    def __init__(self, c, p):
        self.costo = c
        self.porciones = p
        self.nombre = 'Empanadas'

    def Costo_por_Porcion(self):
        if self.porciones:
            return (self.costo / self.porciones)
    
class MilanesaConPure:
    tiempo = 30
    complejidad = 'baja'
    costo = 800
    porciones = 4

    def __init__(self, c, p):
        self.costo = c
        self.porciones = p
        self.nombre = 'Milanesa con pure'

    def Costo_por_Porcion(self):
        if self.porciones:
            return (self.costo / self.porciones)

pizza = Pizza(500, 4)
#print(pizza.Costo_por_Porcion())

guiso = GuisoLentejas(900, 6)
#print(guiso.Costo_por_Porcion())

empanadas = Empanadas(740, 4)
#print(empanadas.Costo_por_Porcion())

milanesa = MilanesaConPure(800, 4)
#print(milanesa.Costo_por_Porcion())


lista = [
    (pizza.nombre, pizza.Costo_por_Porcion()),
    (guiso.nombre, guiso.Costo_por_Porcion()),
    (empanadas.nombre, empanadas.Costo_por_Porcion()),
    (milanesa.nombre, milanesa.Costo_por_Porcion())
]

"""
lista = [
    f"La porcion de {pizza.nombre} cuesta ${pizza.Costo_por_Porcion()}",
    f"La porcion de {guiso.nombre} cuesta ${guiso.Costo_por_Porcion()}",
    f"La porcion de {empanadas.nombre} cuesta ${empanadas.Costo_por_Porcion()}",
    f"La porcion de {milanesa.nombre} cuesta ${milanesa.Costo_por_Porcion()}"
]
"""
"""
def insertion_sort(lista):
    for step in range(1, len(lista)):
        key = lista[step]
        j = step - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = key

insertion_sort(lista)
"""

def insertion_sort(lista):
    for step in range(1, len(lista)):
        key = lista[step]
        j = step - 1
        key_costo = key[1]
        while j >= 0 and lista[j][1] > key_costo:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

insertion_sort(lista)

print("-" * 50)

for item in lista:
    nombre = item[0]
    costo_por_porcion = item[1]
    print(f"La porcion de {nombre} cuesta ${costo_por_porcion}")

print("-" * 50)

#2
class Node:
    valor = ""
    subnodes = None
    datos_extra = 0
    def __init__(self, valor, datos_extra):
        self.valor = valor
        self.subnodes = []
        self.datos_extra = datos_extra
        
raiz = Node("Mundo", 10)

raiz.subnodes.append(Node("Argentina", 2))
raiz.subnodes.append(Node("Brasil", 3))
raiz.subnodes.append(Node("Filipinas", 8))

raiz.subnodes[0].subnodes.append(Node("Buenos Aires", 4))
raiz.subnodes[0].subnodes.append(Node("La Pampa", 6))
raiz.subnodes[0].subnodes.append(Node("Mendoza", 8))
raiz.subnodes[0].subnodes.append(Node("Entre Rios", 8))

raiz.subnodes[0].subnodes[0].subnodes.append(Node("Vte. Lopez", 8))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Munro", 9))


cont = 0
prom = 0

def recorrer(r, sangria = ""):
    global cont
    global prom
    print(sangria + r.valor + '\n')
    prom = prom + r.datos_extra
    sangria += "    "    
    cont += 1
    for i in r.subnodes:
        recorrer(i, sangria)
    
recorrer(raiz)

print((prom / cont))


"""
1) Dado el siguiente listado de información genere un modelo utilizando POO y
aplique los algoritmos de ordenación por inserción a la lista según la
relación de costo por porción: primero las recetas más baratas por porción.

Recetas:
1) Pizza:
	* Tiempo: 30 min
	* Costo: $500
	* Complejidad: media
	* Porciones: 4
	
2) Guiso Lentejas:
	* Tiempo: 120 min
	* Costo: $900
	* Complejidad: alta
	* Porciones: 6
	
3) Empanadas:
	* Tiempo: 60 min
	* Costo: $740
	* Complejidad: media
	* Porciones: 4
	
4) Milanesa con puré:
	* Tiempo: 30 min
	* Costo: $800
	* Complejidad: baja
	* Porciones: 4


2) Utilizando estructura de árbol y POO realizar:
2.1) La reprensentación de la división geopolítica del mundo. El mundo está
     dividido en países, estos en regiones y las regiones en comunas. Construir
     un mundo con 3 países, 1 país con almenos 4 regiones y 1 región con almenos
     2 comunas.
     
2.2) Realizar una función recursiva que recorra el árbol y muestre los países 
     con sus regiones y comunas.
     Cada subnivel debe estar con una sangría más adentro para destacar al nivel
     que pertenece.
     
3) Si tengo una lista con N cantidad de elementos y la estaba ordenando con un 
   algoritmo de complejidad O(n^2). Mañana tendrá N+1 elemento y tengo la 
   posibilidad de aplicar un algoritmo de ordenación de complejidad O(n):
   ¿me conviene cambiar el tipo de algortimo o sigo con el que estaba?
   
    me conviene cambiaro, ya que el algoritmo de ordenacion es menos complejo al 
    que tenia antes. el primero era un algoritmo de complejidad exponencial en cambio
    el segundo es uno lineal lo que lo hace mas sencillo y liviano a la hora de ordenar.

    Si tienes una lista con N elementos y la estás ordenando utilizando un algoritmo de complejidad O(n^2), 
    y mañana esa lista crecerá a N+1 elementos, tendrías que considerar el tiempo requerido para realizar la 
    ordenación con ambos algoritmos para tomar una decisión informada.

    Si sigues utilizando el algoritmo de complejidad O(n^2) para una lista con N+1 elementos, el tiempo requerido 
    para ordenarla aumentaría significativamente. La complejidad O(n^2) implica que el tiempo de ejecución aumenta 
    cuadráticamente con el tamaño de la lista. Por lo tanto, si N+1 es solo un incremento pequeño en comparación 
    con N, el aumento en el tiempo de ejecución puede no ser muy significativo y podrías optar por seguir utilizando 
    el mismo algoritmo.

    Sin embargo, si el crecimiento de N a N+1 es considerable, es posible que desees considerar cambiar al algoritmo de 
    complejidad O(n) para aprovechar su eficiencia. Un algoritmo de complejidad O(n) significa que el tiempo de ejecución 
    aumenta linealmente con el tamaño de la lista, lo que es mucho más eficiente que O(n^2). Si el nuevo elemento se puede 
    insertar de manera eficiente en la lista ordenada utilizando el algoritmo O(n), podrías obtener un mejor rendimiento 
    en términos de tiempo de ejecución global.

    En resumen, si el crecimiento de N a N+1 es significativo, te convendría cambiar al algoritmo de complejidad O(n). 
    Si el incremento es pequeño y el tiempo de ejecución adicional no es un problema, puedes seguir utilizando el 
    algoritmo de complejidad O(n^2).
"""