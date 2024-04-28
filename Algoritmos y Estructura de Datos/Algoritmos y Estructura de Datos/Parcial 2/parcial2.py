# Ejercicio 1:
# se crea la clase jugador
class Jugador:
    # se definen sus atributos
    def __init__(self, nombre, peso, goles, partidos):
        self.nombre = nombre
        self.peso = peso
        self.goles = goles
        self.partidos = partidos    
    # se calcula su promedio de gol
    def promedio_goles_por_partido(self):
        if self.partidos > 0:
            return self.goles / self.partidos
        else:
            return 0.0

# se crean las instancias de cada jugador
messi = Jugador("Lionel Andres Messi", 70, 1000, 800)
dimaria = Jugador("Angel Di Maria", 73, 700, 900)
martinez = Jugador("Lautaro Martinez", 91, 0, 200)
paredes = Jugador("Leandro Paredes", 82, 50, 450)

# lista de jugadores
jugadores = [messi, dimaria, martinez, paredes]

# se ordena la lista con el metodo de insercion
for i in range(1, len(jugadores)):
    key = jugadores[i]
    j = i - 1
    while j >= 0 and jugadores[j].promedio_goles_por_partido() > key.promedio_goles_por_partido():
        jugadores[j + 1] = jugadores[j]
        j -= 1
    jugadores[j + 1] = key

# se imprime la lista ordenada con los atributos y resultados de cada jugador
for jugador in jugadores:
    # redondear los resultados
    promedio_redondeado = round(jugador.promedio_goles_por_partido(), 2) 
    # atributos sin redondear
    print("Nombre:", jugador.nombre)
    print("Peso:", jugador.peso, "KG")
    print("Goles:", jugador.goles)
    print("Partidos:", jugador.partidos)
    print("Promedio de goles por partido:", promedio_redondeado)
    print()

#-------------------------------------------------------------------------------------------------------------
# Ejercicio 2:
# se crea la clase Tag
class Tag:
    def __init__(self, n, i):
        self.tag = n
        self.id = i
        self.childs = []

# se crea una función recursiva para imprimir la estructura del árbol en un formato HTML
def print_html(tag, indent=''):
    print(f"{indent}<{tag.tag}{' id=' + str(tag.id) if tag.id else ''}>")
    for child in tag.childs:
        print_html(child, indent + '    ')
    print(f"{indent}</{tag.tag}>")

# se crea estructura del árbol DOM de HTML
html = Tag("html", None)
html.childs.append(Tag("head", None))
html.childs.append(Tag("body", None))
html.childs[1].childs.append(Tag("header", None))
html.childs[1].childs.append(Tag("article", None))
html.childs[1].childs.append(Tag("footer", None))
html.childs[1].childs[1].childs.append(Tag("div", "content"))
html.childs[1].childs[1].childs[0].childs.append(Tag("p", "text"))

# se imprime estructura del árbol llamando a la función recursiva
print_html(html)

#-------------------------------------------------------------------------------------------------------------
# Ejercicio 3:
# Al utilizar un algoritmo de complejidad O(n^2) para ordenar una lista inicial con N elementos, el tiempo 
# de ejecución será proporcional a N^2. Pero, si se utiliza un algoritmo de complejidad O(n) para ordenar 
# la lista, el tiempo de ejecución será proporcional a N, lo cual es más eficiente. En el caso de agregar un 
# elemento adicional a la lista, el cambio al algoritmo de complejidad O(n) es mejor, porque el tiempo de 
# ejecución seguira proporcional a la cantidad de elementos en la lista, esto daría un mejor rendimiento.
