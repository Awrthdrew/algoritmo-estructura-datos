# 1) POO y ordenacion

# class Pizza:
#     tiempo = 30
#     complejidad = 'media'
#     # costo = 500 # $500 las 4 porciones
#     # porciones = 4

#     def __init__(self, c, p):
#         self.costo = c
#         self.porciones = p
#         self.nombre = 'Pizza'

# class GuisoLentejas:
#     tiempo = 120
#     complejidad = 'alta'
#     # costo = 900
#     # porciones = 6

#     def __init__(self, c, p):
#         self.costo = c
#         self.porciones = p
#         self.nombre = 'Guiso de lentejas'

# class Empanadas:
#     tiempo = 60
#     complejidad = 'media'
#     # costo = 740
#     # porciones = 4

#     def __init__(self, c, p):
#         self.costo = c
#         self.porciones = p
#         self.nombre = 'Empanadas'

# class MilanesaConPure:
#     tiempo = 30
#     complejidad = 'baja'
#     # costo = 800
#     # porciones = 4

#     def __init__(self, c, p):
#         self.costo = c
#         self.porciones = p
#         self.nombre = 'Milanesa con pure'

# def costo_por_porcion(self):
#     porcion = self.porciones
#     costo = self.costo
#     if porcion:
#         costo_porcion = costo / porcion
#         return f'La porcion de {self.nombre} cuesta ${round(costo_porcion, 2)}'

# # creacion de objetos
# porcion_pizza = Pizza(500, 4)
# porcion_guiso = GuisoLentejas(900, 6)
# porcion_empanada = Empanadas(740, 4)
# porcion_milanesa = MilanesaConPure(800, 4)

# def insertion_sort(lista):

#     for step in range(1, len(lista)):
#         key = lista[step]
#         j = step - 1
              
#         while j >= 0 and key < lista[j]:
#             lista[j + 1] = lista[j]
#             j = j - 1
        
#         lista[j + 1] = key

# lista = [costo_por_porcion(porcion_pizza), costo_por_porcion(porcion_guiso), costo_por_porcion(porcion_empanada), costo_por_porcion(porcion_milanesa)]
# print(f'COSTO POR PORCION'.center(150,'-'))
# print(f'\n{lista}\n\n')

class Comida:
    def __init__(self, nom, cos, por):
        self.costo = cos
        self.porciones = por
        self.nombre = nom
    def costo_por_porcion(self):
        if self.porciones:
            costo_porcion = self.costo / self.porciones
            return f'cada porcion de {self.nombre}, cuesta: {costo_porcion}'


Pizza = Comida("pizza", 500, 4)
Guiso_de_Lentejas = Comida("guiso", 900, 6)
Empanadas = Comida("empanadas", 740, 4)
Milanesas_Con_Pure = Comida("milanesas", 800, 4)

def insertion_sort(lista):

    for step in range(1, len(lista)):
        key = lista[step]
        j = step - 1
              
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        
        lista[j + 1] = key

lista = [Pizza.costo_por_porcion(), Guiso_de_Lentejas.costo_por_porcion(), Empanadas.costo_por_porcion(), Milanesas_Con_Pure.costo_por_porcion()]

print(f'COSTO POR PORCION'.center(150, '-'))
print(f'\n{lista}\n\n')

# 2) Arbol y POO
class Node:
    valor = ""
    region = None
    def __init__(self, valor):
        self.valor = valor
        self.region = []

# mundo
raiz = Node('Mundo')
# 3 paises
raiz.region.append(Node('Argentina'))
raiz.region.append(Node('Uruguay'))
raiz.region.append(Node('Brasil'))
# 4 regiones
raiz.region[0].region.append(Node('Córdoba'))
raiz.region[0].region.append(Node('Santa Fe'))
raiz.region[0].region.append(Node('Mendoza'))
raiz.region[0].region.append(Node('Buenos Aires'))
# 2 comunas
raiz.region[0].region[0].region.append(Node('Carlos Paz'))
raiz.region[0].region[0].region.append(Node('Ciudad de Córdoba'))

def recorrer(r, sangria = ''):
    print(sangria + r.valor + '\n')
    sangria += ' '
    for i in r.region:
        recorrer(i, sangria)

print(f'MUNDO'.center(150,'-'))
recorrer(raiz)

"""
Alumno: Evelyn Ernst
Fecha: 21/06/2023

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
"""