class NodoGenealogico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


class ArbolGenealogico:
    def __init__(self):
        self.raiz = None

    def agregar_miembro(self, nombre, padre=None):
        nuevo_miembro = NodoGenealogico(nombre)
        if padre is None:
            self.raiz = nuevo_miembro
        else:
            self._agregar_hijo_recursivo(self.raiz, padre, nuevo_miembro)

    def _agregar_hijo_recursivo(self, nodo_actual, padre, nuevo_miembro):
        if nodo_actual.nombre == padre:
            nodo_actual.agregar_hijo(nuevo_miembro)
        else:
            for hijo in nodo_actual.hijos:
                self._agregar_hijo_recursivo(hijo, padre, nuevo_miembro)

    def imprimir_genealogia(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz

        print("    " * nivel + nodo.nombre)

        for hijo in nodo.hijos:
            self.imprimir_genealogia(hijo, nivel + 1)

    def obtener_nombres_ordenados(self):
        nombres = []
        self._obtener_nombres_recursivo(self.raiz, nombres)
        self.burbuja(nombres)  # Ordenar los nombres utilizando el algoritmo Burbuja
        return nombres

    def _obtener_nombres_recursivo(self, nodo_actual, nombres):
        nombres.append(nodo_actual.nombre)
        for hijo in nodo_actual.hijos:
            self._obtener_nombres_recursivo(hijo, nombres)

    def burbuja(self, lista):
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if lista[j].lower() > lista[j + 1].lower():
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Crear el árbol genealógico de Abraham
arbol = ArbolGenealogico()
arbol.agregar_miembro("Abraham")
arbol.agregar_miembro("Agar", "Abraham")
arbol.agregar_miembro("Ismael", "Agar")
arbol.agregar_miembro("Sara", "Abraham")
arbol.agregar_miembro("Isaac", "Sara")
arbol.agregar_miembro("Rebeca", "Isaac")
arbol.agregar_miembro("Esaú", "Isaac")
arbol.agregar_miembro("Jacob", "Isaac")
arbol.agregar_miembro("Lea", "Jacob")
arbol.agregar_miembro("Zilpa", "Jacob")
arbol.agregar_miembro("Raquel", "Jacob")
arbol.agregar_miembro("Bilha", "Jacob")
arbol.agregar_miembro("Rubén", "Lea")
arbol.agregar_miembro("Simeón", "Lea")
arbol.agregar_miembro("Leví", "Lea")
arbol.agregar_miembro("Judá", "Lea")
arbol.agregar_miembro("Isacar", "Lea")
arbol.agregar_miembro("Zabulón", "Lea")
arbol.agregar_miembro("Gad", "Zilpa")
arbol.agregar_miembro("Aser", "Zilpa")
arbol.agregar_miembro("José", "Raquel")
arbol.agregar_miembro("Benjamín", "Raquel")
arbol.agregar_miembro("Dan", "Bilha")
arbol.agregar_miembro("Neftalí", "Bilha")

# Imprimir el árbol genealógico de forma recursiva
arbol.imprimir_genealogia()

# Obtener los nombres ordenados alfabéticamente utilizando el algoritmo Burbuja
nombres_ordenados = arbol.obtener_nombres_ordenados()
print(nombres_ordenados)
