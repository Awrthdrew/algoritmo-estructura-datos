# Funciones integradas
print("Hola", "Buenos dias", sep=" y ", end=". ") 
print("¿Como estas?")
# sep="" separador de los elementos del print()
# end="" lo que va a aparecer al final del print()

# input():
input("Escriba: ") #cuadro de texo, para escribir en la consola
# al darle un String, este aparecera antes
# Ejemplo:
variable = input("Escriba su nombre: ")
print(variable + ", eres una buena persona.")

# type():
type("Palabra") # devuelve el tipo de elemento dentro de los parentesis
# Ejemplos:
print(type(3))
print(type(2.3))
print(type(True))
print(type([]))
print(type(()))
print(type({0}))
print(type({}))

# str, int, float y bool
variable1 = "3"
print(variable1 , type(variable1))
# devuelve a la variable y su tipo original
variable1 = float(variable1)
print(variable1 , type(variable1))
# cambia a la variable de tipo y devuelve el tipo
variable1 = int(variable1)
print(variable1, type(variable1))
# hace lo mismo que lo anerior pero a una variable int
variable1 = bool(variable1)
print(variable1, type(variable1))

# list, tuple, set y dict
lista = list((1, 2, 3))
tupla = tuple((1, 2, 3))
conjunto = set((1, 2, 3))
diccionario = dict((("Uno", 1),("Dos", 2), ("Tres", 3)))
# se poneque tipo de cadena se quiere que sea
print(lista, type(lista))
print(tupla, type(tupla))
print(conjunto, type(conjunto))
print(diccionario, type(diccionario))
# se imprime la cadena y se dice que tipo es
print(list("Deletrea")) 
# convierte un string en una lista
print(dict(Uno=1, Dos=2, Tres=3))
# convierte variables nombradas a un diccionario

#Funciones matematicas
numero = -3
print("El valor absoluto de", numero, "es: ", abs(numero))
# abs(): valor absoluto del numero que pidas
print("Potencia de 2^3 es: ", pow(2, 3))
# pow(): potencia entre dos numeros
print("Redondeo de 10.50 es: ", round(10.50))
print("Redondeo de 10.51 es: ", round(10.51))
# round(): redondea el numero
print("Redondeo de 10.55 con 0 cifras decimales es: ", round(10.55, 0))
print("Redondeo de 10.55 con 1 cifra decimal es: ", round(10.55, 1))
print("Redondeo de 10.55 con 2 cifras decimales es: ", round(10.55, 2))
# se puede hacer con la cantidad de cifras decimales que especifiques

# sum, max y min
# sum(): suma los elementos
print("Suma lista: ", sum(list((1, 2, 3)))) # de una lista
print("Suma tupla: ", sum(tuple((1, 2, 3)))) # de una tupla
print("Suma conjunto: ", sum(set((1, 2, 3)))) # de un conjunto
print("Suma diccionario: ", sum(dict((("Uno", 1),("Dos", 2), ("Tres", 3)))))
# de un diccionario

# max() y min():
print("Maximo:", max(list((1, 2, 3)))) 
# max(): obtener maximo de los elementos
print("Minimo:", min(set((1, 2, 3))))
# min(): obtener minimo de los elementos

# Funciones utiles: len y sorted
# len(): permite saber la cantidad de elementos
lista1 = [2, 1, 3, 5]
diccionario1 = {"Clave_1", "Valor_1", "Clave_2", "Valor_2", "Clave_3"}

print("El tamaño de la lista es:", len(lista1)) # tamaño de la lista
print("El tamaño del diccionario es:", len(diccionario1)) 
# tamaño del diccionario

# sorted(): ordena los elementos de menor a mayor
print("Lista ordenada de menor a mayor:", sorted(lista1)) 
# ordena los elementos de la lista de menor a mayor
print("Lista ordenada de mayor a menor:", sorted(lista1, reverse=True))
# ordena los elementos de la lista de mayor a menor

# Funciones especiales: range,enumerate y zip. Devuelven un objeto.
# range():
print(list(range(2, 5)))
# lista de numeros enteros desde el primero hasta el anterior del segundo

# enumerate():
print(list(enumerate(["Uno", "Dos", "Tres"])))
# enumera, desde el 0 en adelante, los elementos de la lista
print(list(enumerate(["Uno", "Dos", "Tres"], start=1)))
# start=n: se elige el primer numero

#zip():
print(list(zip([1, 2, 3], ["Uno", "Dos", "Tres"])))
# convina dos colecciones en una lista de tuplas.
# si una coleccion tiene mas elementos que la otra, 
# se ajusta a la que menos elementos tiene.

