from localidades import data
from provincias import data_prov


"""from localidades import data

print("Localidades de Argentina")

print("Cantidad de localidades: " + str(len(data["localidades"])))

for localidad in data["localidades"]:
    
    #Imprimir todas las localidades de Argentina.
    #print("nombre: " + localidad["nombre"])
    #print("provincia: " + localidad["provincia"]["nombre"])
    if localidad["provincia"]["nombre"] == "Entre Ríos":
        print("+--------------------------------------------------------------+")
        print("nombre: " + localidad["nombre"])
        print("provincia: " + localidad["provincia"]["nombre"])
    
for key in data["localidades"][0].keys():
    print(key)"""
    
# Se inserta localidad para encontrar la provincia y que después al seleccionar la provincia te tire su listado.
"""nombre = input("Ingrese el nombre de la Localidad: ")
localidades = {}

for mi_localidad in data["localidades"]:
    if mi_localidad["nombre"] == nombre:
        localidades = mi_localidad

if not localidades:
    print("La localidad no fue encontrada.")
else:
    print(f"{localidades['nombre']} queda en {localidades['provincia']['nombre']}")

provincia = input("Ingrese el nombre de la Provincia: ")

for mi_localidad in data["localidades"]:
    if mi_localidad["provincia"]["nombre"] == provincia:
        print("-"*10)
        print(f"{mi_localidad["nombre"]}, depto: {mi_localidad["provincia"]["nombre"]}")"""
        
        
#Listar todas las provincias con la cantidad de localidades que tiene cada una.
provincias = {}

for localidad in data["localidades"]:
    if localidad["provincia"]["nombre"] not in provincias:
        provincias[localidad["provincia"]["nombre"]] = 1
    else:
        provincias[localidad["provincia"]["nombre"]] += 1

# Recibe una tupla e itera tomando como clave el parametro del índice 1. De manera descendente
sorted_provincias = sorted(provincias.items(), key=lambda tupla: tupla[1], reverse=True)

for provincia, num_localidades in sorted_provincias:
    print(f"Provincia: {provincia} | N° de Localidades: {num_localidades}")
    

#Listar todas las localidades por al sur de la latitud -31.
"""prov_lat = {}
provincia = {}

for localidad in data["localidades"]:
    if localidad["centroide"]["lat"] < -31:
        prov_lat[localidad["nombre"]] = localidad["centroide"]["lat"]
        provincia[localidad["nombre"]] = localidad["provincia"]["nombre"]

for localidad, lat in prov_lat.items():
    print(f"\nProvincia: {provincia[localidad]} | Localidad: {localidad} | Latitud: {lat}")"""
    
#Buscar otro dataset JSON en https://datos.gob.ar a gusto y procesar algo de tu interes


"""Hacer un función recursiva que muestre todo el árbol del JSON con su 
correspondiente indentación segun el nivel de profundidad de las dimensiones de
la matriz del mismo."""

#Función recursiva que muestre todo el árbol del JSON con su correspondiente indentación según el nivel de profundidad de las dimensiones de la matriz del mismo.

#Esta funciona, imprimiendo el tipo de datos que necesito. str(type(estructura[key])))
"""def arbol_json(estructura, identacion:int):
    for key in estructura:
        print("   " * identacion + str(key) + ":" + str(type(estructura[key])))
        
        if isinstance(estructura[key], dict):
            arbol_json(estructura[key], identacion + 1)
            
        if isinstance(estructura[key], list):
            arbol_json(estructura[key][0], identacion + 1)
            
print(f'La estructura del árbol es: \n {arbol_json(data, 5)}')"""
            
#Esta función imprime el contenido de los datos de provincia con su estructura.
"""def arbol_json(estructura, identacion:int):
    for key in estructura:
        print("   " * identacion + str(key) + ":" + str((estructura[key])))
        
        if isinstance(estructura[key], dict):
            arbol_json(estructura[key], identacion + 1)
            
        if isinstance(estructura[key], list):
            arbol_json(estructura[key][0], identacion + 1)
            
    for key in estructura:
        
        #Imprime los nombres de los parámetros y tipo
        if not (isinstance(estructura[key], dict) or isinstance(estructura[key], list)):
            print("   " * identacion + str(key) + " : " + str(estructura[key]))
        elif isinstance(estructura[key], dict):
            print("   " * identacion + key + " : ")
            arbol_json(estructura[key], identacion + 1)
        elif isinstance(estructura[key], list):
            print("   " * identacion + key + " : ")
            for item in estructura[key]:
                print(" ")
                arbol_json(item, identacion + 1)
            
arbol_json(data_prov, 5)"""