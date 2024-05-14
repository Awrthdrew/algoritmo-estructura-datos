from arbolParcial import data

"""
1) Reporte del histórico de consumo eléctrico de un país seleccionado:
  * Mostrar un listado de Países (iterando la Dimensión 0)
  * Pedir por teclado que ingrese el ID de país deseado
  * Mostrar el consumo eléctrico del país seleccionado desde 1970. 
     * Armar el título de reporte con data["body"]["metadata"]["indicator_name"] + el nombre del país
     * Listado de año y su consumo
     * Al final mostrar un promedio de consumo total

2) ¿En que año fue el máximo consumo de cada país?
"""

#print("Datos cargados dentro del header: " + str(len(data["header"])))
#print("Datos cargados dentro del body: " + str(len(data["body"])))
#print("Datos cargados dentro del footer: " + str(len(data["footer"])))

#1
paises = {}
ids = {}
electrico = {}

def listar_paises():
    """for dimension in data[""]["dimensions"]:
        for member in dimension["members"]:
            name = member["name"]
            member_id = member["id"]
            print("Pais:", name,"ID:", member_id)"""
            
    paises = set()
    for pais in data["body"]["data"]:
        ID = pais["iso3"]
        nombre = pais["dim_208"]
        paises.add((ID, nombre))
    print("Los países cargados son:")
    for pais, ID in paises:
        print(f"{pais} ID: {ID}")

#2
def pedir_id():
    paises = set()
    electrico = set()
    for pais in data["body"]["data"]:
        nombre = pais["iso3"]
        ID = pais["dim_208"]
        paises.add((nombre, ID))
    print("Los países cargados son:")
    for pais, ID, in paises:
        print(f"{pais} ID: {ID}")

    identificador = int(input("COLOQUE LA ID DEL PAIS DESEADO: "))
    identificadores_disponibles = {i for _, i in paises}
    
    if identificador in identificadores_disponibles:
        indicator_name = data["body"]["metadata"]["indicator_name"]
        print(f"{indicator_name}")
        for datos in data["body"]["data"]:
            if datos["dim_208"] == identificador: 
                nombre = datos["iso3"]
                consumo = datos["value"]
                anio = datos["dim_29117"]
                electrico.add((nombre, consumo, anio))
        electrico_ordenado = sorted(list(electrico), key=lambda tupla:tupla[2], reverse=False)
        for electrico, consumos, año in electrico_ordenado:
            print(f"PAIS {electrico} CONSUMO {consumos} AÑO {año-27168}")
    else:
        print("El ID no corresponde a ningun pais!")

def imprimir_tipos_estructura(estructura, identacion=0):
    if isinstance(estructura, dict):
        for key in estructura:
            print("  " * identacion + str(key) + ": dict")
            imprimir_tipos_estructura(estructura[key], identacion + 1)
    elif isinstance(estructura, list):
        if estructura:
            print("  " * identacion + "list:")
            imprimir_tipos_estructura(estructura[0], identacion + 1)
        else:
            print("  " * identacion + "list: <empty>")
    else:
        print("  " * identacion + str(estructura) + ": " + type(estructura).__name__)

def max_consumo_pais():
    paises = set()
    electrico = set()
    for pais in data["body"]["data"]:
        nombre = pais["iso3"]
        ID = pais["dim_208"]
        paises.add((nombre, ID))
    print("Los países cargados son:")
    for pais, ID, in paises:
        print(f"{pais} ID: {ID}")

    identificador = int(input("COLOQUE LA ID DEL PAIS DESEADO: "))
    identificadores_disponibles = {i for _, i in paises}
    
    if identificador in identificadores_disponibles:
        indicator_name = data["body"]["metadata"]["indicator_name"]
        print(f"{indicator_name}")
        for datos in data["body"]["data"]:
            if datos["dim_208"] == identificador: 
                nombre = datos["iso3"]
                consumo = datos["value"]
                anio = datos["dim_29117"]
                print(consumo , anio-27168)
        
        max_consumo = max(electrico, key=lambda tupla: tupla[1])
        consumo = max_consumo[1]
        anio = max_consumo[2]
        print(f"El mayor consumo fue de: {consumo} en el año {anio-27168}")
    else:
        print("El ID no corresponde a ningun pais!")
    
    
#imprimir_tipos_estructura(data)
#listar_paises()
#pedir_id()
max_consumo_pais()


