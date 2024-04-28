# Estructuras de control de flujo:
# if: ejecuta un bloque de código si una condición es verdadera.
# else: ejecuta un bloque de código cuando la condición en el if es falsa.
# elif: verifica condiciones adicionales después del if y ejecutar un bloque de código correspondiente si se cumple una condición.

# Ejemplo 1:
nota = float(input("Introduzca su nota: "))
if nota < 6:
    print("Desaprobado.")
else:
    print("Aprobado.")
# usando if y else

# Ejemplo 2:
nota1 = float(input("Introduzca su nota: "))
if 0 <= nota1 and nota1 < 5:
    print("Desaprobado.")
elif 5 <= nota1 and nota1 < 7:
    print("Aprobado.")
elif 7 <= nota1 and nota1 < 9:
    print("Notable.")
elif 9 <= nota1 and nota1 <= 10 :
    print("Sobresaliente.")
else:
    print("Nota fuera de rango.")
# usando if y elif

# Bucles:
# while: ejecuta un bloque de codigo hasta que se deje de cumplir la condicion.
# Ejemplos:
contador = 3 
while contador != 0:
    contador = contador - 1
    print("El conteniddo el contador es:", contador)
# se le resta un numero al 3 hasta que llega a 0

# for: itera sobre una coleccion de elementos, ejecutando un mismo bloque de codigo por cada uno
# estrucura: for iterador in [lista elementos]:  
# Ejemplo:
for iterador in [1, 2, 3]:
    print(iterador)

# Con una lista
lista = list((2, 1, 0))
for iterador1 in lista:
    print(iterador1)

# Con una tupla
tupla = tuple((2, 1, 0))
for iterador2 in tupla:
    print(iterador2)

# Con un conjunto
conjunto = set((2, 1, 0))
for iterador3 in conjunto:
    print(iterador3)

# Con un diccionario, ejemplo 1
diccionario = dict(((2, "Dos"), (1, "Uno"), (0, "Cero")))
for iterador4 in diccionario:
    print(iterador4)
#recorre solo las claves. (clave, valores)

# Con un diccionario, ejemplo 2
diccionario = dict(((2, "Dos"), (1, "Uno"), (0, "Cero")))
for iterador5 in diccionario.values():
    print(iterador5)
# para recorrer solo los valores se usa .values()

# Con un diccionario, ejemplo 3
diccionario = dict(((2, "Dos"), (1, "Uno"), (0, "Cero")))
for iterador6 in diccionario.items():
    print(iterador6)
# para recorrer las claves y los valores (los pares) se usa .items()

# range y len
# Ejemplos:
lista = ["Vamos", "a", "acceder", "a", "esta", "lista", "por", "indices"]
for indice in range(len(lista)):
    print("Indice:", indice, "Elemento:", lista[indice])
# len(): obtener el numero de elemenos.
# range(): obtener una secuencia de indices.

# Sentencias en bucles: 
# break: permite detener y salir del bucle aunque la expresion sea True.
for numero in range(5):
    if numero == 3:
        break
    print(numero)
# deja de recorrer al llegar al 3, sino seguiria hasta el anterior al 5

# continue: terminar con la iteracion aun que no haya llegado al final, y seguir con la siguinte.
for numero in range(5):
    if numero == 3:
        continue
    print(numero)
# sigue recorriendo a pesar de llegar al 3.

# Convinar: else con while y for.
# else: se ejecuta cuando el ciclo while y for dejan de ejecutarse.
# pero si existe un break en los ciclos while o for, entonces no se ejecuta.
# Ejemplo: sistema de comprobacion de contraseña
intentos = 3
while intentos > 0:
    if input(">>> Escriba la contraseña:") == "River912":
        print("Contraseña correcta.")
        break
# la contraseña al ser correcta termina el bucle.
    intentos = intentos - 1
    print("Contraseña incorrecta.")
# al poner la contraseña incorrecta disminuyen los intentos restantes.
else:
    print("Se te acabaron el numero de intentos.")
# al terminar el bucle seejecuta el else.
