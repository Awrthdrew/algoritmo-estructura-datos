class Jugador:
    def __init__(self, p, g, par, n):
        self.peso = p
        self.goles = g
        self.partidos = par
        self.nombre = n

    def get_promedio(self):
        return self.goles / self.partidos
        



Messi = Jugador(70, 1000, 800, "Messi")
DiMaria = Jugador(73, 700, 900, "DiMaria")
Martinez = Jugador(91, 0, 200, "Martinez")
Paredes = Jugador(82, 50, 450, "Paredes")


array_jugadores = [Messi, DiMaria, Martinez, Paredes]


def insertion_sort(array_jugadores):
    for step in range(1, len(array_jugadores)):
        key = array_jugadores[step]
        j = step - 1

        while j >= 0 and key.get_promedio() < array_jugadores[j].get_promedio():
            array_jugadores[j + 1] = array_jugadores[j]
            j = j - 1

        array_jugadores[j + 1] = key
insertion_sort(array_jugadores)
print("--" * 50 + "Jugadores Ordenados" + "--" * 50)
for x in array_jugadores:
    print(str(x.nombre) + " Promedio de goles: " + str(round(x.get_promedio(), 2)))






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

prueba = []



def recorrer(raiz, prueba, d = ""):
    if raiz.id:
        prueba.append(d + "<" + raiz.tag + ' id="' + raiz.id + '">')
    else:
        prueba.append(d + "<" + raiz.tag + ">")
    if raiz.childs:
        for x in raiz.childs:
            recorrer(x, prueba, d + "   ")
    prueba.append(d + "<" + raiz.tag + "/>")


"""
Me acabo de dar cuenta que si remplazas todos los append con print tendras el mismo resultado, pero me queda poco tiempo asi que lo dejo asi
"""

recorrer(html, prueba)
for x in prueba:
    print(x)


"""
Alumno: Sebastian Perez
Fecha: 22-06-2023
Tema: B Metodo de insercion



1) Dada la siguiente información construir utilizando POO las 
instacias correspondientes y ponerlas dentro de una lista. Luego 
ordenar la lista utilizando el método que te tocó en el papel 
según promedio de cantidad de goles por partido

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


      


2) Dado la siguiente estructura de árbol que contiene un DOM (Document Object Model) de HTML:

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

     
3) Si tengo una lista con N cantidad de elementos y la estaba ordenando con un 
   algoritmo de complejidad O(n^2). Mañana tendrá N+1 elemento y tengo la 
   posibilidad de aplicar un algoritmo de ordenación de complejidad O(n):
   ¿me conviene cambiar el tipo de algortimo o sigo con el que estaba?

   Te conviene cambiar el algoritmo ya que, tal vez por esta vez el grado de complejidad no aumentara mucho si la cantidad de elementos es poca, (si tu cantidad de
   elementos es 1 por ejemplo el grado de complejidad en ambos algoritmos es el mismo), a medida que la cantidad de elementos vaya aumentando la diferencia de complejidad
   entre los algoritmos sera cada vez mas grande ya que el grado de complejidad del algoritmo O(n) crece linealmente pero el grado de complejidad del algoritmo O(n^2)
   crece EXPONENCIALMENTE. llegara un punto en el algoritmo O(n^2) donde con agregar 1 solo elemento el grado de complejidad crecera por un numero altisimo.
   la "perdida de tiempo" para implementar el algoritmo sera mucho menor a los recursos y el tiempo que tomara el algoritmo con O(n^2) cuando la cantidad de elementos es alta.
   
"""






