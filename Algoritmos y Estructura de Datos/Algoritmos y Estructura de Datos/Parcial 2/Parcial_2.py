"""
Alumno:
Fecha: 
Tema: 

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
"""
class Jugador:
    def __init__(self, n, pe, g, pa):
        self.nombre = n
        self.peso = pe
        self.goles = g
        self.partidos = pa
        
    def promedio_goles_por_partido(self):
        return self.goles / self.partidos
        
lista = [Jugador("Messi", 70, 1000, 800), Jugador("DiMaría", 73, 700, 900), Jugador("Martinez", 91, 0, 200), Jugador("Paredes", 82, 50, 450)]

i = 0
while i < len(lista) - 1:
    if lista[i].promedio_goles_por_partido() < lista[i+1].promedio_goles_por_partido():
        aux = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = aux
        i = -1
    i += 1
    
for x in lista:
    print(x.nombre + ": " + str(x.promedio_goles_por_partido()))

"""


2) Dado la siguiente estructura de árbol que contiene un DOM (Document Object Model) de HTML:

"""
print("----------------------")
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

"""
realizar una función recursiva que genere la siguiente salida:

"""
def recorrer(t, s = ""):
    i = ""
    if(t.id != None):
        i = ' id="' + t.id + '"'
    print(s + '<' + t.tag + i + '>')
    for x in t.childs:
        recorrer(x, s + "    ")
    print(s + '</' + t.tag + '>')

recorrer(html)
    
""""

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
   
   Conviene cambiar a un algoritmo de ordenación de complejidad O(n), porque la
   cantidad de iteraciones aumenta de forma lineal y no exponencial como los es
   O(n^2). Es decir que a medida que crece la cantidad de elementos de la lista
   su procesamiento será más eficiente con O(n).
   
"""






