#Variables
caja1 = 111 # int
caja2 = 1,2 # float
caja3 = True # bool
caja4 = "Hola" # str

#Funciones
#nombreDeLaFuncion(argumento1, argumento2, ..., argumentoN)
print("Hola como estas")
print(caja1 + caja1)

#Funcion suma
#def nFuncion(nArgumento1, nArgumento1, ..., nArgumentoN)
def suma(num1, num2): 
    return num1 + num2 #lo que queremos que devuelba la funcion
print(suma(5, 3)) #se define que valores van a tener los argumentos

#Funcion media
def mediaDe2Numeros(num1, num2):
    media = num1 + num2
    media = media/2 #se alamacena el valor obtenido en la ultima variable
    return media
#las variables dentro de las funciones son variables locales
print(mediaDe2Numeros(5, 2))

#Funcion insulta
def insulta(nombre):
    print(nombre, "es una persona de dudosa inteligencia")

insulta("Ezequiel")

#Listas
fibonacci = [0,1,1,2,3,5,8] #nLista[datosDeLaLista]
print(fibonacci[0]) #llamar al dato nª 0 de la lista
print(fibonacci[4]) #llamar al dato nª 4 de la lista

cosas = [0, 1.5, True, "Joestan"]
print(cosas[0], cosas[1], cosas[2], cosas[3])
print(cosas)
#Devolver tamaño de una lista len()
print(len(cosas))

#Metodos
print("Antes", fibonacci)
#.append() -> añadir un elemento al final de una lista
fibonacci.append(21) 
print("Despes del append", fibonacci)
fibonacci.insert(7, 13) # .insert(posLista, elemento)
# pone el elemento en la poscision de la lista indicada
print("Despues del insert", fibonacci)
dir(fibonacci)

#IF-ELSE
#if valorBoolean
#   bloque de codigo
insultado = True #valor boolean
if insultado:
    print("Venid a mi, pero con la cara destapada")
else:
    print("¡Que tenga un buen dia!")

#Operadores relacionales: >, <, >=, <=, !=, ==
nota = 8
if nota >= 6:
    print("Aprobado")
else:
    print("Suspendido")
    
#Operadores logicos: not, and, or
aprobado = True
ocupado = False

if aprobado and not ocupado:
    print("Toca viciar")
else:
    print("F")

#Bucles
#WHILE -> como un if solo que se repite hasta que la condicion deja de cumplirse
contador = 0
while contador < 10: 
    print(contador)
    contador = contador + 1
#el contador sigue sumandose hasta que llega a 10 e imprime cada numero

#FOR
#for nombreVariable in objetoIterable(puede ser una lista)
#   Bloque de codigo
for elemento in [1,2,3,4,5]:
    print(elemento)
    # en cada accion se ejecuta un numero diferente, siguiendo
    # el orden de la lista hasta terminar con la lista

lista = ["Juan", "Miguel", "Alva", "Jose", "Augusto"]
nombre = "Alva"
for elemento in lista:
    if elemento == nombre:
        print(elemento, "esta en la lista")
