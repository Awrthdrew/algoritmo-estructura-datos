# 2.1
class Comuna:
    def __init__(self, nombre):
        self.nombre = nombre

class Region:
    def __init__(self, nombre, comunas):
        self.nombre = nombre
        self.comunas = comunas

class Pais:
    def __init__(self, nombre, regiones):
        self.nombre = nombre
        self.regiones = regiones

class Mundo:
    def __init__(self, paises):
        self.paises = paises

# Crear comunas
comuna1 = Comuna("Comuna 1")
comuna2 = Comuna("Comuna 2")

# Crear regiones con comunas
region1 = Region("Región 1", [comuna1])
region2 = Region("Región 2", [comuna2])

# Crear país con regiones
pais1 = Pais("País 1", [region1, region2])

# Crear país con al menos 4 regiones
region3 = Region("Región 3", [])
region4 = Region("Región 4", [])
region5 = Region("Región 5", [])
region6 = Region("Región 6", [])

pais2 = Pais("País 2", [region3, region4, region5, region6])

# Crear mundo con 3 países
mundo = Mundo([pais1, pais2])

# Acceder a los datos del mundo
for pais in mundo.paises:
    print("País:", pais.nombre)
    for region in pais.regiones:
        print("  Región:", region.nombre)
        for comuna in region.comunas:
            print("    Comuna:", comuna.nombre)

# 2.2
def mostrar_geopolitica(arbol, nivel=0):
    if isinstance(arbol, Mundo):
        print("Mundo:")
        for pais in arbol.paises:
            mostrar_geopolitica(pais, nivel + 1)
    elif isinstance(arbol, Pais):
        print(f"{' ' * nivel}País: {arbol.nombre}")
        for region in arbol.regiones:
            mostrar_geopolitica(region, nivel + 1)
    elif isinstance(arbol, Region):
        print(f"{' ' * nivel}Región: {arbol.nombre}")
        for comuna in arbol.comunas:
            mostrar_geopolitica(comuna, nivel + 1)
    elif isinstance(arbol, Comuna):
        print(f"{' ' * nivel}Comuna: {arbol.nombre}")

# Utilizar la función con el árbol creado previamente
mostrar_geopolitica(mundo)
