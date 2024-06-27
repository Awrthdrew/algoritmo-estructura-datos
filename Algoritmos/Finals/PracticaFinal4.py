class Ciudad:
    def __init__(self, N, p, tM, tm):
        self.Nombre = N
        self.Promedio = p
        self.TempMax = tM
        self.TempMin = tm


    
    def set_nombre(self, Nombre):
        self.Nombre = Nombre

    def set_promedio(self, promedio):
        self.Promedio = promedio

    def set_TempMax(self, TempMax):
        self.TempMax = TempMax

    def set_TempMin(self, TempMin):
        self.TempMin = TempMin
    

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
    print("4. Listar Paises")

    opcion = (int)(input("Que desea hacer hoy: "))
    if opcion == 1:
        nueva_ciudad = Ciudad(input("Nombre de la ciudad: "), int(input("Promedio de temperatura: ")), int(input("Temperatura maxima: ")), int(input("Temperatura Minima: ")))
        array_paises.append(nueva_ciudad)

    if opcion == 2:
        for x in range(len(array_paises)):
            print("Numero: " + str(x) + ". " + str(array_paises[x].Nombre))
        pais = (int)(input("Que ciudad desea Modificar? "))
        for x in range(len(array_paises)):
            if pais == x:
                array_paises[x].set_nombre(input("Nuevo nombre de Ciudad: "))
                array_paises[x].set_promedio((int)(input("Nuevo prmedio de Ciudad: ")))
                array_paises[x].set_TempMax((int)(input("Nueva temperatura maxima de Ciudad: ")))
                array_paises[x].set_TempMin((int)(input("Nueva temperatura minima de Ciudad: ")))
    
    

    if opcion == 3:
        promedio, media, max, NombreMax, min, NombreMin = calcular_datos(array_paises)
        print("La tamperatura promedio es: " + str(promedio) + ", La media es: " + str(media) + ", La temperatura maxima: " + str(max) + ", En la ciudad de: " + str(NombreMax) + ", La tempera minima: " + str(min) + ", En la ciudad de: " + str(NombreMin))

    if opcion == 4:
        for x in array_paises:
            print("Nombe de Ciudad: " + x.Nombre + " El pomedio de Temperatura es de: " + str(x.Promedio) + " La temperatura maxima es de: " + str(x.TempMax) + " La temperatura minima es de: " + str(x.TempMin))