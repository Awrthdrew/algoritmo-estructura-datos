class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return (self.nombre + ' - ' + str(self.edad))
    def __gt__(self, greater_than):
        return self.edad > greater_than.edad
    def __lt__(self, less_than):
        return self.edad < less_than.edad
    def __ge__(self, greater_equal_than):
        return self.edad >= greater_equal_than.edad
    def __le__(self, less_equal_than):
        return self.edad <= less_equal_than.edad

class Nodo:
    def __init__(self, persona):
        self.persona = persona
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, persona):
        if self.raiz is None:
            self.raiz = Nodo(persona)
        else:
            self._insertar(self.raiz, persona)

    def _insertar(self, nodo, persona):
        if persona < nodo.persona:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(persona)
            else:
                self._insertar(nodo.izquierdo, persona)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(persona)
            else:
                self._insertar(nodo.derecho, persona)

    def in_orden(self):
        self._in_orden(self.raiz)

    def _in_orden(self, nodo):
        if nodo is not None:
            self._in_orden(nodo.izquierdo)
            print(nodo.persona)
            self._in_orden(nodo.derecho)

# Crear la lista de personas
lista = [
    Persona("Andrew", 21), 
    Persona("Joaquín", 18),
    Persona("Franco", 20), 
    Persona("Mispi", 19), 
    Persona("Helena", 22)
]

# Crear el árbol e insertar las personas
arbol = ArbolBinarioBusqueda()
for persona in lista:
    arbol.insertar(persona)

# Imprimir el árbol en orden
print("--- ÁRBOL BINARIO DE BÚSQUEDA EN ORDEN ---")
arbol.in_orden()
