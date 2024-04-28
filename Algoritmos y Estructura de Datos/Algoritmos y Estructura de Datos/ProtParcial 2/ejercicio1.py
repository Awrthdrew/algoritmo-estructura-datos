class Receta:
    def __init__(self, nombre, tiempo, costo, complejidad, porciones):
        self.nombre = nombre
        self.tiempo = tiempo
        self.costo = costo
        self.complejidad = complejidad
        self.porciones = porciones

    def __repr__(self):
        return f"Receta: {self.nombre} - Costo por porción: ${self.costo_por_porcion()}"

    def costo_por_porcion(self):
        return self.costo / self.porciones


def ordenar_recetas_por_costo_por_porcion(recetas):
    for i in range(1, len(recetas)):
        actual = recetas[i]
        j = i - 1
        while j >= 0 and actual.costo_por_porcion() < recetas[j].costo_por_porcion():
            recetas[j + 1] = recetas[j]
            j -= 1
        recetas[j + 1] = actual


# Crear las instancias de las recetas
receta1 = Receta("Pizza", 30, 500, "media", 4)
receta2 = Receta("Guiso Lentejas", 120, 900, "alta", 6)
receta3 = Receta("Empanadas", 60, 740, "media", 4)
receta4 = Receta("Milanesa con puré", 30, 800, "baja", 4)

# Crear la lista de recetas
recetas = [receta1, receta2, receta3, receta4]

# Ordenar las recetas por costo por porción
ordenar_recetas_por_costo_por_porcion(recetas)

# Imprimir las recetas ordenadas
for receta in recetas:
    print(receta)
