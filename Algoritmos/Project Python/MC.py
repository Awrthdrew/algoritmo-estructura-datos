
#Ejercico 3 Lista de Ejercicios 4, secuencia de Fibo
"""


Numero = (int)(input("Elija la cantidad de elementos que desea mostrar de la secuencia: "))

def Fibonacci(N: int):
    Contador = 1
    x = 1
    y = 1
    z = 0
    while(Contador <= N):
        z = x + y
        y = x
        x = z
        z = x + y
        print(z)
        Contador = Contador + 1
print(Fibonacci(Numero))

"""


#Ejercicio 2, Triangulos

"""

def Triangulo(V1: int, V2: int, V3: int):
    if V1 != V2  and V1 != V3 and V2 != V3:
        print("El triangulo es Escaleno")

    elif V1 == V2 == V3:
        print("EL triangulo es Equilatero")

    else:
        print("El triangulo es isoceles")

print("Elija los lados del truangulo a continuacion:")

Valor1 = (int)(input("Primer lado del triangulo: "))
Valor2 = (int)(input("Segundo lado del triangulo: "))
Valor3 = (int)(input("Tercer lado del triangulo: "))

print(Triangulo(Valor1, Valor2, Valor3))

"""

#Ejercicio 4, Notas de alumnos

"""

def media_aritmetica(x: int, y: int, z: int):
    promedio = (x + y + z) / 3
    print(promedio)

def promedio_ponderado(x: int, y: int, z: int):
    PP = (x * 5 + y * 3 + z * 2) / 10
    print(PP)

print("Que tipo de promedio desea sacar?")

Opcion = (str)(input("Ingrese A para Media Aritmetica, Ingrese P si desea el Promedio Ponderado: "))

X = (int)(input("Ingrese primer nota: "))
Y = (int)(input("Ingrese Segunda nota: "))
Z = (int)(input("Ingrese tercer nota: "))

if Opcion == "A":
    print(media_aritmetica(X, Y, Z))

else:
    print(promedio_ponderado(X, Y, Z))
    

"""
#Ejercicio 5 Positivo Entero Par

"""

def factorial_doble(x: int):
    z = 1
    y = 1
    while y <= x:
         z = z * y 
         y = y + 2
         
        
    print(z)
         
   
        

Numero = (int)(input("Elija el NUmero que desea Factorear: "))

print(factorial_doble(Numero))

"""

#Ejercicio 6


#Numero = (str)(input("Elija el Numero que desee sumar: "))

"""

def sumar_digitos(Numero):
    suma_total = 0
    for i in Numero:
        print(i)
        suma_total = suma_total + int(i)
    print(str(suma_total))

sumar_digitos((str)(input("Elija el Numero que desee sumar: ")))

"""
"""
#Ejercicios Matrices

matriz = [
    [3, -2, 1, 12],
    [1, 3, 1, -4],
    [2, 2, -4, 6]
]


def sumatoria_filas(matriz):
    for fila in matriz:
        suma = 0
        for elemento in fila:
            suma = suma + elemento
        print(suma)

#sumatoria_filas(matriz) 
"""

"""
def sacar_determinante(matriz):
    determinante = ((matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[1][0] * matriz[2][1] * matriz[0][2])) - ((matriz[0][2] * matriz[1][1] * matriz[2][0]) + (matriz[1][0] * matriz[0][1] * matriz[2][2]) + (matriz[2][1] * matriz[1][2] * matriz[0][0]))
    return determinante
    print(determinante)

def transponer(matriz):
    return list(zip(*matriz))


def dividir_columnas(matriz):
    trans = transponer(matriz)
    columna_x = trans[0]
    columna_y = trans[1]
    columna_z = trans[2]
    columna_r = trans[3]
    det_x = sacar_determinante([columna_r, columna_y, columna_z])
    det_y = sacar_determinante([columna_x, columna_r, columna_z])
    det_z = sacar_determinante([columna_x, columna_y, columna_r])
    valor_x = det_x / sacar_determinante(matriz)
    valor_y = det_y / sacar_determinante(matriz)
    valor_z = det_z / sacar_determinante(matriz)

    print("X = " + str(valor_x) + " Y = " + str(valor_y) + " Z = " + str(valor_z))

print(dividir_columnas(matriz))



fruits = ["apple", "banana", "cherry"]
prices = [1.50, 2.25, 0.99]
for fruit, price in zip(fruits, prices):
    print(fruit, price)


"""
"""
Documentos = []

def agregar_documento(Documentos):
    if len(Documentos) == 2:
        print("El documento a sido perdido por falta de espacio")

    else:
        Documentos.append(input("Itroduzca Nombre de documento que desea Agregar: "))

    for i in Documentos:
        print(Documentos[i])    


def imprimir_elemento(Documentos):
    Documentos.remove(0)

opcion = ""

while( opcion != "S" and opcion != "s"):
    print("-" * 100)
    print("Presione A si desea mandar un documento a imprimir")
    print("I si desea imprimir elemento en la cola")
    print("Y S para salir")
    print("Hay: " + str(len(Documentos)) + "En la cola")
    opcion = input("Que desea hacer hoy: ")

    if opcion == "A":
        print("Agregando documento a la cola...")
        agregar_documento(Documentos)

    if opcion == "I":
        print("Imprimiendo documento")
        imprimir_elemento(Documentos)

"""


