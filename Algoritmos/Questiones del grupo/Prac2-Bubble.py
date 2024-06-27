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

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

bubble_sort(lista)

print("-" * 50)

for item in lista:
    nombre = item[0]
    costo_por_porcion = item[1]
    print(f"La porción de {nombre} cuesta ${costo_por_porcion}")

print("-" * 50)

