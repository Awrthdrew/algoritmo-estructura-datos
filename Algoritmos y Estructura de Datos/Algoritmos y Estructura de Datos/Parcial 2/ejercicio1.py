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
