class Ciudad:
    def __init__(self, nombre, temp_promedio, temp_max, temp_min):
        self.nombre = nombre
        self.temp_promedio = temp_promedio
        self.temp_max = temp_max
        self.temp_min = temp_min

def calcular_promedio_temperatura(ciudades):
    suma_temperaturas = sum(ciudad.temp_promedio for ciudad in ciudades)
    return suma_temperaturas / len(ciudades)

def calcular_mediana_temperatura(ciudades):
    temperaturas = sorted(ciudad.temp_promedio for ciudad in ciudades)
    num_ciudades = len(ciudades)
    if num_ciudades % 2 == 0:
        indice_medio_1 = num_ciudades // 2 - 1
        indice_medio_2 = num_ciudades // 2
        mediana = (temperaturas[indice_medio_1] + temperaturas[indice_medio_2]) / 2
    else:
        indice_medio = num_ciudades // 2
        mediana = temperaturas[indice_medio]
    return mediana

def encontrar_ciudad_mas_calurosa(ciudades):
    ciudad_mas_calurosa = max(ciudades, key=lambda ciudad: ciudad.temp_max)
    return ciudad_mas_calurosa

def encontrar_ciudad_mas_fria(ciudades):
    ciudad_mas_fria = min(ciudades, key=lambda ciudad: ciudad.temp_min)
    return ciudad_mas_fria

def main():
    ciudades = [
        Ciudad("Ciudad A", 25, 35, 15),
        Ciudad("Ciudad B", 20, 30, 10),
        Ciudad("Ciudad C", 30, 40, 20)
    ]

    while True:
        print("Estadísticas climatológicas:")
        print("-----------------------------")
        print("a) Promedio de temperatura del país:", calcular_promedio_temperatura(ciudades))
        print("b) Mediana de temperatura del país:", calcular_mediana_temperatura(ciudades))
        ciudad_calurosa = encontrar_ciudad_mas_calurosa(ciudades)
        print("c) Ciudad más calurosa:", ciudad_calurosa.nombre, "(Temp. máx:", ciudad_calurosa.temp_max, ")")
        ciudad_fria = encontrar_ciudad_mas_fria(ciudades)
        print("d) Ciudad más fría:", ciudad_fria.nombre, "(Temp. mín:", ciudad_fria.temp_min, ")")

        respuesta = input("¿Deseas agregar otra ciudad? (s/n): ")
        if respuesta.lower() != "s":
            break

        nombre = input("Nombre de la ciudad: ")
        temp_promedio = float(input("Temperatura promedio anual: "))
        temp_max = float(input("Temperatura máxima registrada: "))
        temp_min = float(input("Temperatura mínima registrada: "))

        nueva_ciudad = Ciudad(nombre, temp_promedio, temp_max, temp_min)
        ciudades.append(nueva_ciudad)

if __name__ == "__main__":
    main()

