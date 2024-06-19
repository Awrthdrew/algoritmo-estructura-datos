import random

# 1. Leer un número A y mostrar si es par o impar
A= random.randint(1, 777)
resto = A % 2
true= f". PAR ({A})"  
false= f". IMPAR ({A})"

if resto ==  0:
    print(true)
else:
    print(false)
    

print("________________________")


"""1.0.1 Leer la edad de dos personas e imprimir True si la primera persona es más grande que la
segunda (Para la edad utilizar apenas el año)"""
edad_cori = random.randint(1, 19)
edad_milena = random.randint(1, 16)

print(edad_cori < edad_milena)


print("________________________")

"""2. Leer la edad de dos personas e imprimir True si la primera persona es más grande que la
segunda (Para la edad utilizar apenas el año)"""

edad_uribe = random.randint(1, 20)
edad_puerro = random.randint(1, 18)

print(f"Uribe: ({edad_uribe})" )
print(f"Puerro: ({edad_puerro})" )


"""if edad_uribe > edad_puerro:
    print("True")
else:
    print("False")"""
comparacion = edad_uribe > edad_puerro
print(comparacion)

print("________________________")
    
"""3. Un grupo conformado por 3 personas quieren viajar solos, pero por lo menos uno de ellos
debe tener más de 18 años. Leer las edades de cada uno e imprimir True se pueden viajar o
False si no."""

edad_uribe = random.randint(1, 20)
edad_puerro = random.randint(1, 18)
edad_andrew=  random.randint(1, 21)


print(f"Uribe: ({edad_uribe})" ) 
print(f"Puerro: ({edad_puerro})" )
print(f"Andrew: ({edad_andrew})" )

es_legal = edad_uribe >= 18 or  edad_puerro >= 18 or edad_andrew >= 18 
print(es_legal)

print("________________________")

"""4. El grupo anterior viajó y quieren mirar una película para mayores de edad, imprimir True se
todos pueden mirar la película o False si no."""

edad_uribe = 20 
edad_puerro = 18
edad_andrew=  21

print(f"Uribe: ({edad_uribe})" )
print(f"Puerro: ({edad_puerro})" )
print(f"Andrew: ({edad_andrew})" )

are_you_legal = edad_uribe >= 18 and  edad_puerro >= 18 and edad_andrew >= 18 
print(are_you_legal)


print("________________________")


"""5. Leer dos enteros y mostrar True, si los números tienen paridades diferentes, y False, si las
paridades son iguales"""

n1= random.randint(1, 50)
n2=  random.randint(1, 50)

print(f"Número 1: ({n1})")
print(f"Número 2: ({n2})")

print(n1 % 2 == n2 % 2)


print("________________________")


"""6. Escriba un programa para calcular la reducción en la vida útil de un fumador. Pregunte la
cantidad de cigarrillos fumados por día y cuántos años que fuma. Considere que un fumador
pierde 10 minutos de vida con cada cigarrillo. Calcular cuántos días de vida perderá un
fumador, mostrar el total en días."""

cigarrillos_x_dia= int(input("CANTIDAD CIGARRILLOS: "))
anos_fumando = int(input("AÑOS FUMANDO: "))
# Fumando por X años se multiplica por AÑO (365)  como unidad.  A esto se le agrega el producto de cuanto minutos se perdieron por la cantidad de cigarrillos fumado x año. Para después dividir la cantidad de minutos en un día.
vida_perdida= ((anos_fumando*365) * cigarrillos_x_dia) * 10 / 1440
print(f"Días de vida perdidas: {vida_perdida}")


print("________________________")


"""7. Mostrar por pantalla el siguiente texto empleando comillas simples, dobles y triples:
O'Reilly Media, antes llamada O'Reilly & Associates, es una empresa editorial estadounidense
fundada y dirigida por Tim O'Reilly que está principalmente enfocada a libros de tecnología
e informática."""

texto = '''O'Reilly Media, antes llamada O'Reilly & Associates, es una empresa editorial estadounidense
fundada y dirigida por Tim O'Reilly que está principalmente enfocada a libros de tecnología
e informática.'''

print(texto)


print("________________________")


"""8. Mostrar por pantalla el texto anterior empleando 2 variables y concatenando"""
text1= """O'Reilly Media, antes llamada O'Reilly & Associates, es una empresa editorial estadounidense
fundada y dirigida por Tim O'Reilly"""
text2= """que está principalmente enfocada a libros de tecnología
e informática.'''"""

print(text1 + text2)


print("________________________")


"""9. Utilizar la función print y imprimir su primero nombre, su edad, el nombre de la disciplina y el
año actual.
Siguiendo el formato: {nombre} - {edad} - {nombre de la disciplina} - {ano}.
Observación: Utilizar el parámetro sep en la función print.
Ejempro: José – 2004 – Algoritmo – 19"""

print("Carolina, ", "2004", "Biomecánica", "19", sep="-") #sep funciona como separador entre strings que son espaciado por una coma.


print("________________________")


"""10. Utilizar la función de interpolación format para hacer lo mismo que la cuestión anterior."""

nombre = "Caroline"
ano = 2004
disciplina = "Diseño en Ilustración"
edad = 19

# \n (Es la sangría del texto para poder bajar de línea)
mensaje = f"Nombre: {nombre}\nAño: {ano}\nDisciplina: {disciplina}\nEdad: {edad}"
print(mensaje)

