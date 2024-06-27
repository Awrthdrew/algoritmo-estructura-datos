import random


class Equipo:
    
    def __init__(self, cod , nom , punt , goles = 0):
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
    def __init__(self, equipo1 = None, equipo2 = None):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    


PaisesBajos = Equipo(7, "Paises Bajos", 1731.23, 0)
eeuu = Equipo(11, "USA", 1673.34, 0)
Argentina = Equipo(1, "Argentina", 1843.73, 0)
Australia = Equipo(27, "Australia", 1530.45, 0)
Japon = Equipo(20, "Japon", 1595.96, 0)
Croacia = Equipo(6, "Croacia", 1742.55, 0)
Brasil = Equipo(3, "Brasil", 1828.27, 0)
Corea = Equipo(28, "Corea", 1529.3, 0)

Inglaterra = Equipo(4, "Inglaterra", 1797.39, 0)
Senegal = Equipo(18, "Senegal", 1612.61, 0)
Francia = Equipo(2, "Francia", 1843.54, 0)
Polonia = Equipo(26, "Polonia", 1536.99, 0)
Marruecos = Equipo(13, "Marruecos", 1655.5, 0)
España = Equipo(10, "España", 1703.45, 0)
Portugal = Equipo(9, "Portugal", 1718.25, 0)
Suiza = Equipo(12, "Suiza", 1661.12, 0)

Qatar = Equipo(58, "Qatar", 1393.52, 0)
Ecuador = Equipo(40, "Ecuador", 1486.47)

Iran = Equipo(22, "Iran", 1556.59)
Wales = Equipo(35, "Wales", 1506.04, 0)

SaudiArabia = Equipo(53, "Saudi Arabia", 1421.46)
Mexico = Equipo(14, "Mexico", 1639.19)

Denmark = Equipo(19, "Denmark", 1597.37)
Tunisia = Equipo(31, "Tunisia", 1516.66)

CostaRica = Equipo(42, "Costa Rica", 1478.3)
Alemania = Equipo(15, "Alemania", 1636.32)

Canada = Equipo(45, "Canada", 1454.12)
Belgica = Equipo(5, "Belgica", 1788.55)

Serbia = Equipo(25, "Serbia", 1539.03)
Cameroon = Equipo(43, "Cameroon", 1470.97)

Ghana = Equipo(59, "Ghana", 1391.13)
Uruguay = Equipo(16, "Uruguay", 1633.13)
 

array_paises = [[Qatar, Ecuador, Senegal, PaisesBajos], [Inglaterra, Iran, eeuu, Wales], [Argentina, SaudiArabia, Mexico, Polonia], [Francia, Australia, Denmark, Tunisia], [España, CostaRica, Alemania, Japon], [Belgica, Canada, Marruecos, Croacia], [Brasil, Serbia, Suiza, Cameroon], [Portugal, Ghana, Uruguay, Corea]]


def fase_grupos(array_paises):
    for grupo in range(len(array_paises)):
        for equipo in range(len(grupo)):
            puntaje = array_paises[grupo][equipo].puntaje + array_paises[grupo][equipo + 1].puntaje
            ran = round(random.uniform(0, puntaje), 2)
            array_paises[grupo][equipo]













raiz = Node()
raiz.left = Node()
raiz.left.left = Node()
raiz.left.left.left = Node(PaisesBajos, eeuu)
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



ganador = None

def ganadorre(nodo, nivel = 0):
    
    if nodo.left:
        nodo.equipo1 = ganadorre(nodo.left, nivel + 1)


    if nodo.right:
        nodo.equipo2 = ganadorre(nodo.right, nivel + 1)
        
    if nodo.equipo1 and nodo.equipo2:
        if nivel == 3:
            print("Octavos de Final: ")
            print(nodo.equipo1.nombre + " vs " + nodo.equipo2.nombre)
        if nivel == 2:
            print("Cuartos de Final: ")
            print(nodo.equipo1.nombre + " vs " + nodo.equipo2.nombre)
        if nivel == 1:
            print("Semi Final: ")
            print(nodo.equipo1.nombre + " vs " + nodo.equipo2.nombre)
        if nivel == 0:
            print("Final: ")
            print(nodo.equipo1.nombre + " vs " + nodo.equipo2.nombre)
        print("\n")
        

        puntaje = nodo.equipo1.puntaje + nodo.equipo2.puntaje
        ran = round(random.uniform(0, puntaje), 2)

        if ran < nodo.equipo1.puntaje:
            ganador = nodo.equipo1
        elif ran > nodo.equipo1.puntaje:
            ganador = nodo.equipo2
        else:
            ganador = random.choice([nodo.equipo1, nodo.equipo2])
        print("Ganador: " + ganador.nombre)
        print("\n")

    return ganador
        # print("Gano " + str(ganador.nombre))

print(ganadorre(raiz).nombre)
#print("El equipo ganador del Mundial es:", ganador.nombre)
    


    
    
ganadorre(raiz)


