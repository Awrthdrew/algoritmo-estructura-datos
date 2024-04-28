#Listas
lista = [29, True, 3.1415, "Hola como estas"]
print(lista[3]) #imprime el objeto en la posicion [n]

print(lista[1:3]) 
#imprime los objetos en la posicion entre el 1 y el anterior al 3

lista[2] = "Elemento cambiado"
print(lista)
#cambia el elemento[n] por el elemento igualado
#se puede agregar una lista dentro de otra

lista_nueva = [1, 2, "Hola como estas", 4, 5]
lista_nueva.append("Hola como estas")
print(lista_nueva)
# .append(n): agregar elemento n al final de la lisa

print(lista_nueva.count("Hola como estas"))
# .count(n): devuelve cantidad de veces que se repite el elemento n

print(lista_nueva.index(2))
# .index(n): indica la primera posicion del elemento n

lista_nueva.remove(3)
print(lista_nueva)
# .remove(n): elimina el elemento n

#Tuplas: 
# son como listas pero inmodificables una vez creadas
tupla = ("Buenos dias", True, 3.1416, 912, True)
print(tupla[0]) 
#imprimir elemento n de la tupla
print(tupla.count(True))  
# .count: contar cantidad de veces que aparece el elemento n
print(tupla.index(True))  
# .index(n): indica la primera posicion del elemento n

#Conjuntos:
#los elementos no pueden ser repetidos
print(set([9, 1, 2, 1, 1.5, 8])) #lista
print(set((9, 1, 2, 1, 1.5, 8))) #tupla
print(set("5236.7")) #string: lista de caracteres

conjunto = set([2, 3, 3, 4])
print(conjunto)
#imprime conjunto, mostrando una sola vez los elementos repetidos

conjunto.add(1) #añadir elemento al conjunto
print(conjunto)

conjunto.remove(1) #elimina el elemento del conjunto
print(conjunto)

conjunto_2 = set([5, 3, 5, 6])
conjunto_3 = set([4, 2])
print(conjunto, conjunto_2, conjunto_3) #imprimir los tres conjuntos

print(conjunto.intersection(conjunto_2)) 
# .intersection: elemento que tienen en comun los dos conjuntos
print(conjunto & conjunto_2) # otra forma de hacerlo

print(conjunto_2.issubset(conjunto)) 
#los elementos del conjunto_2 estan dentro del conjunto? False
print(conjunto_3.issubset(conjunto))
#los elementos del conjnto_3 estan dentro del conjunto? True
#comprobar si los elementos de un conjunto estan dentro del otro 
#(True or False)

#Diccionario {clave/key : valor/value}
# - no tierne orden, es heterogeneo y mutable
diccionario = {1: "Uno", 2: "Dos"}
print(diccionario) # ver el contenido del diccionario
print(diccionario[1]) # ver el value
diccionario[3] = "Tres" # agregar value
print(diccionario) 

dict_lista_tuplas = dict([(1, "Uno"), (2, "Dos"), (3, "Tres")])
print(dict_lista_tuplas) #crear un diccionario con una lista de tuplas

dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string) #crear un diccionario con una lista de strings

dict_tipos = {1: "integer", 2.2: "floatt", "texto": "string", (1, 2): "tupla"}
# Se puede usar cualquier tipo de datos como value, 
# pero la key al usarse como idenificador debe usarse como inmutable
print(dict_tipos)

dict_repeticion = {1: "Primero", 1: "Ultimo"}
# La key no debe repetirse
# en caso de hacerlo, tomara el valor del la ultima key 
print(dict_repeticion)

#Metodos de los diccionarios:
print(diccionario.keys()) 
# .keys(): devuelve todas las keys/claves
print(diccionario.values())
# .values(): devuelve todas los values/valores
print(diccionario.items())
# .items(): devuelve todos los pares key/clave-value/valor

claves = diccionario.values()
print(claves)
diccionario[1] = "One"
# cambiar el valor de una key
print(claves)
# mostrar solo los value

#Eliminar clave:
diccionario.pop(2) 
print(diccionario)
# .pop(): llamando una key se elimina la key y el value

#Ejercicios:
# 1. Listas:
personajes = ["Kakyoin", "Joseph", "Jotaro"]
personajes.remove("Kakyoin")
personajes.append("Polnareff")
resultado1 = personajes[1:2]
# resultado1 = "Jotaro"
print(resultado1)

# 2. Tuplas:
respuesta = ("Yes", "Yes","Yes")
resultado2 = (respuesta.count("Yes"), respuesta.index("Yes"))
print(resultado2)
# resultado2 = (.coun = 3), (.index = 0)

# 3. Conjuntos:
temporada_2 = set(["Joseph", "Caesar"])
temporada_3 = set(["Jotaro", "Joseph", "Avdol", "Kakyoin", "Polnareff"])
resultado3 = temporada_2 & temporada_3
print(resultado3)
# resultado3 = "Joseph"

# 4. Diccionarios
protas = {1: "Jonnahan", 2: "Joseph", 3: "Jotaro"}
jojos = {"Jonnahan": "Phantom Blood", "Joseph": "Battle Tendency", "Jotaro": "Stardust Crusaders"}
resultado4 = jojos[protas[3]]
print(resultado4)
# resultado4 = Stardust Crusaders