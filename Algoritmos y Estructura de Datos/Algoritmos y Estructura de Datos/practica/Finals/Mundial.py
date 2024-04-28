#Mundial, cada nodo del arbol es un partido entre dos equipos, se tiene que pasar los resultados de la hoja final a la hora anterior.
import random


class Equipo:
    
    def __init__(self, cod = 0, nom = "", punt = 0, goles = 0):
        self.codigo = cod
        self.nombre = nom
        self.puntaje = punt
        self.goles = goles
    
    def reset(self):
        self.codigo = 0
        self.nombre = ""
        self.puntaje = 0
        self.goles = 0 




class Node:
    left = None
    right = None
    def __init__(self, equipo1 = Equipo(), equipo2 = Equipo()):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    


PaisesBajos = Equipo(7, "Paises Bajos", 1731.23, random.randint(0,4))
USA = Equipo(11, "USA", 1673.34, random.randint(0,4))
Argentina = Equipo(1, "Argentina", 1843.73, random.randint(0,4))
Australia = Equipo(27, "Australia", 1530.45, random.randint(0,4))
Japon = Equipo(20, "Japon", 1595.96, random.randint(0,4))
Croacia = Equipo(6, "Croacia", 1742.55, random.randint(0,4))
Brasil = Equipo(3, "Brasil", 1828.27, random.randint(0,4))
Corea = Equipo(28, "Corea", 1529.3, random.randint(0,4))

Inglaterra = Equipo(4, "Inglaterra", 1797.39, random.randint(0,4))
Senegal = Equipo(18, "Senegal", 1612.61, random.randint(0,4))
Francia = Equipo(2, "Francia", 1843.54, random.randint(0,4))
Polonia = Equipo(26, "Polonia", 1536.99, random.randint(0,4))
Marruecos = Equipo(13, "Marruecos", 1655.5, random.randint(0,4))
España = Equipo(10, "España", 1703.45, random.randint(0,4))
Portugal = Equipo(9, "Portugal", 1718.25, random.randint(0,4))
Suiza = Equipo(12, "Suiza", 1661.12, random.randint(0,4))







raiz = Node()
raiz.left = Node()
raiz.left.left = Node()
raiz.left.left.left = Node(PaisesBajos, USA)
raiz.left.left.right = Node(Argentina, Australia)

raiz.left.right = Node()
raiz.left.right.left = Node(Japon, Croacia)
raiz.left.right.right = Node(Brasil, Corea)

raiz.right = Node()
raiz.right.left = Node()
raiz.right.left.left = Node(Inglaterra, Senegal)
raiz.right.left.right = Node(Francia, Polonia)

raiz.right.right = Node()
raiz.right.right.left = Node(Marruecos, España)
raiz.right.right.right = Node(Portugal, Suiza)


Ganador = Equipo()

# def postorden(partido):
#     global Ganador

#     # if partido.equipo1:
#     #     print(partido.equipo1.nombre)
#     #     print(partido.equipo2.nombre)

#     if Ganador.nombre != "":
#         print(Ganador.nombre)
#         if partido.equipo1 == "":
#             partido.equipo1 = Ganador  
#         else:
#             partido.equipo2 = Ganador

#     Ganador.reset()

#     if partido.left:
#         postorden(partido.left)

#     if partido.right:
#         postorden(partido.right)
    
#     if partido.equipo1.nombre != "" and partido.equipo2.nombre != "":
#         print("entro1")
#         print(partido.equipo1.nombre)
#         print(partido.equipo1.goles)
#         print(partido.equipo2.nombre)
#         print(partido.equipo2.goles)

#         if partido.equipo1.goles > partido.equipo2.goles:
#             #print("entro2")
#             print(partido.equipo1.nombre)
#             Ganador = partido.equipo1
            
#         else:
#             #print("entro2.1")
#             print(partido.equipo2.nombre)
#             Ganador = partido.equipo2
levels = []

def bredth(n, nivel = 0):
    global levels
    if n:
        if len(levels) == nivel:
            levels.append([])
        levels[nivel].append(n.equipo1.nombre)
        levels[nivel].append(n.equipo2.nombre)
        bredth(n.left, nivel + 1)
        bredth(n.right, nivel + 1)


# def Postorden(n):
#     if(n.left):
#         Postorden(n.left)

#     if(n.right):
#         Postorden(n.right)
#     if n.equipo1 != "":
#         print(n.equipo1.nombre)
#         print(n.equipo2.nombre)

bredth(raiz)
print(levels)

    


# array_equipos = []
# array_equipos.extend(argentina = Equipo(1, "Argentina", 1843.73), australia)


