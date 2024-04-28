# Definición de la clase Receta
class Receta:
    def __init__(self, nombre, tiempo, costo, complejidad, porciones):
        self.nombre = nombre
        self.tiempo = tiempo
        self.costo = costo
        self.complejidad = complejidad
        self.porciones = porciones
    
    def __str__(self):
        return f"{self.nombre} - Costo por porción: {self.costo / self.porciones}"

# Definición de la clase Mundo
class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paises = []
    
    def agregar_pais(self, pais):
        self.paises.append(pais)
    
    def mostrar_mundo(self):
        print(self.nombre)
        for pais in self.paises:
            pais.mostrar_pais(1)
            print()
    
# Definición de la clase País
class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.regiones = []
    
    def agregar_region(self, region):
        self.regiones.append(region)
    
    def mostrar_pais(self, nivel):
        indent = "\t" * nivel
        print(f"{indent}País: {self.nombre}")
        for region in self.regiones:
            region.mostrar_region(nivel + 1)
    
# Definición de la clase Región
class Region:
    def __init__(self, nombre):
        self.nombre = nombre
        self.comunas = []
    
    def agregar_comuna(self, comuna):
        self.comunas.append(comuna)
    
    def mostrar_region(self, nivel):
        indent = "\t" * nivel
        print(f"{indent}Región: {self.nombre}")
        for comuna in self.comunas:
            comuna.mostrar_comuna(nivel + 1)
    
# Definición de la clase Comuna
class Comuna:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_comuna(self, nivel):
        indent = "\t" * nivel
        print(f"{indent}Comuna: {self.nombre}")


# 1) Ordenamiento de recetas por costo por porción
recetas = [
    Receta("Pizza", 30, 500, "media", 4),
    Receta("Guiso Lentejas", 120, 900, "alta", 6),
    Receta("Empanadas", 60, 740, "media", 4),
    Receta("Milanesa con puré", 30, 800, "baja", 4)
]

recetas_ordenadas = sorted(recetas, key=lambda receta: receta.costo / receta.porciones)

for receta in recetas_ordenadas:
    print(receta)


# 2) Representación de la división geopolítica del mundo
mundo = Mundo("Mundo")
pais1 = Pais("País 1")
pais2 = Pais("País 2")
pais3 = Pais("País 3")

region1 = Region("Región 1")
region2 = Region("Región 2")
region3 = Region("Región 3")
region4 = Region("Región 4")

comuna1 = Comuna("Comuna 1")
comuna2 = Comuna("Comuna 2")
comuna3 = Comuna("Comuna 3")
comuna4 = Comuna("Comuna 4")

region1.agregar_comuna(comuna1)
region1.agregar_comuna(comuna2)
region2.agregar_comuna(comuna3)
region2.agregar_comuna(comuna4)

pais1.agregar_region(region1)
pais1.agregar_region(region2)
pais2.agregar_region(region3)
pais3.agregar_region(region4)

mundo.agregar_pais(pais1)
mundo.agregar_pais(pais2)
mundo.agregar_pais(pais3)

mundo.mostrar_mundo()


# 3) Análisis del algoritmo de ordenación
# Si la lista tiene N elementos y se utiliza un algoritmo de complejidad O(n^2),
# el tiempo de ejecución será proporcional a N^2.

# Si se agrega un elemento a la lista, la cantidad de elementos será N + 1.
# Si se utiliza un algoritmo de complejidad O(n), el tiempo de ejecución será proporcional a N.
# En este caso, el tiempo de ejecución del nuevo algoritmo será menor que el tiempo de ejecución del algoritmo anterior.

# Por lo tanto, en términos de eficiencia, conviene cambiar al nuevo algoritmo de ordenación con complejidad O(n) cuando se agrega un elemento adicional a la lista.
