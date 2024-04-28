class Ciudad:
    def __init__(self, N, p, tM, tm):
        self.Nombre = N
        self.Promedio = p
        self.TempMax = tM
        self.TempMin = tm

    def get_nombre(self):
        return self.Nombre
    
    def get_promedio(self):
        return self.Promedio
    
    def get_TempMax(self):
        return self.TempMax
    
    def get_TempMin(self):
        return self.TempMin
    

BuenosAires = Ciudad("Buenos Aires", 18, 40, -3)
LibertadorSanMartin = Ciudad("Libertador San Martin", 23, 45, 0)
Balcarce = Ciudad("Balcarce", 14, 35, -8)

array_paises = [BuenosAires, LibertadorSanMartin, Balcarce]


def calcular_datos(array_paises):
    promedio = 0
    max = 0
    min = 0
    media = 0
    NombreMax = ""
    NombreMin = ""
    for x in array_paises:
        promedio += x.Promedio

    for x in array_paises:
        max += x.TempMax
        min += x.TempMin
    media = (max + min) / 2
    max = 0
    min = 1000
    for x in array_paises:
        if max < x.TempMax:
            max = x.TempMax
            NombreMax = x.Nombre
        
        if min > x.TempMin:
            min = x.TempMin
            NombreMin = x.Nombre
    return round(promedio / len(array_paises), 2), media, max, NombreMax, min, NombreMin



opcion = 100

while opcion != 0:
    opcion = 100
    print("1. Agregar ciudad")
    print("2. Modificar Ciudad")
    print("3. Imprimir promedio")

    opcion = (int)(input("Que desea hacer hoy: "))
    if opcion == 1:
        nueva_ciudad = Ciudad(input("Nombre de la ciudad: "), int(input("Promedio de temperatura: ")), int(input("Temperatura maxima: ")), int(input("Temperatura Minima: ")))
        array_paises.append(nueva_ciudad)

    if opcion == 2:
        pass

    if opcion == 3:
        promedio, media, max, NombreMax, min, NombreMin = calcular_datos(array_paises)
        print("La tamperatura promedio es: " + str(promedio) + ", La media es: " + str(media) + ", La temperatura maxima: " + str(max) + ", En la ciudad de: " + str(NombreMax) + ", La tempera minima: " + str(min) + ", En la ciudad de: " + str(NombreMin))