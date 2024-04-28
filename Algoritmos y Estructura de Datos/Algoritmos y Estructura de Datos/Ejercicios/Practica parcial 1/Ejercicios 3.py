
  

# LISTA EJERCICIOS 5



#_____________________________________________________________________________________________


#--------------------------------------------------------
#1 Fibonacci     
# def fibonacci(N:int):
#       termo1 = 0
#       termo2 = 1
#       contador = 3
      
#       print("n0 -> 1", end='')
      
#       while contador <= N:
#             termoAux = termo1 + termo2
#             termo1 = termo2   
#             termo2 = termoAux
#             print(f' -> {termoAux}', end='')
#             contador += 1
      
#       print('')
      
      
# print("/n" + "="*40 + "/n       Secuencia de Fibonacci/n" + "=" *40)
# secuencia = input("Cuantos números quieres mostrar? ")

# fibonacci(int(secuencia))            
            
    




#_____________________________________________________________________________________________


# Escriba una función que recibiendo la longitud de los 3 lados de un triángulo nos devuelva que
# tipo de triángulo es:
#  Escaleno: todos los lados distintos
#  Equilátero: todo los lados iguales
#  Isósceles: solo 2 lados iguales 
#------------------------------------------------------------------------------
# 2

# def triangulo(x,y,z):
    
#     if (x != y) and (x != z) and (y != x) and (y != z):
#         print("Es un escaleno")
        
#     elif (x == y) and (x==z):
#         print("Equilátero")   
        
#     else: print("Isósceles")
        
# triangulo(2,5,2)


#_____________________________________________________________________________________________


# Escriba una función que recibiendo del usuario un número hasta el 1000 lo convierta en
# número romano y muestre el resultado por pantalla.
# Para la solución observe que a los números enteros en la lista N corresponden respectivamente
# los números romanos en la lista R
# N: 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
# R: M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I 

#-----------------------------------------------------------------------
#3

# def convertir_numero_romano(entero):
#       naturales=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#       romanos=['M','CM','D','CD','C','XC','L','Xl','X','IX','V','IV','I']
      
#       romano = ''
#       natural=entero
#       i = 0
      
#       while i<13:
#             num = natural // naturales[i]
#             if num > 0:
#                   romano += romanos[i]*num
#                   natural -= num * naturales[i]
#             i += 1
#       return romano

# print(convertir_numero_romano(973))            
                  
          
#_____________________________________________________________________________________________

# Escribir una función que tome tres calificaciones de un estudiante como parámetro y una letra.
# Si la letra es A, la función debe calcular la media aritmética de las calificaciones del estudiante, si
# es P, debe calcular el promedio ponderado, con pesos 5, 3 y 2 
#---------------------------------------------------------------------
#4

# def estudiante(x,y,z,letra):
#     if letra == "a" or "A":
#         calculo = x+y+z
#         resultado = calculo//3
#         print(f"Su nota media es: {resultado}")
        
#     elif letra == "p" or "P":
#         calculo = (x*5) + (y+3) + (z+2)
#         resultado = calculo // 10
#         print(f"Su nota ponderada es: {resultado}")
        
            
# estudiante(7,8,3,"P")        


#_____________________________________________________________________________________________

# Escribir una función no recursiva que tome un número entero positivo impar N y devuelva el
# factorial doble de ese número. El factorial doble se define como el producto de todos los
# números naturales impares desde 1 hasta algún número natural impar N.
# Por exemplo el doble factorial de 5 es: 5! = 1 * 3 * 5 = 15
#-------------------------------------------------------------------------------------------------

#5
# n = int(input("Introduzca un número: "))  
# if n >= 0:
#     x = 1
#     f = 1
#     while x <= n:
#         f = f * x
#         x += 2
#     print("El factorial de ",n,"es:",f)
# else:
#     print("No se puede calcular")
    
     
       
#_____________________________________________________________________________________________

# Escribir una función que tome un número entero mayor que zero y retorna la suma de todos sus
# dígitos.
# Por ejemplo, el número 370 corresponderá al valor 10 (3+7+0). Si el parámetro leído no es un
# número entero mayor que zero, el programa terminará con el mensaje "Número Inválido       
                    
#------------------------------------------------------------------------------------------            
#6

# def numero():
#      x = input("Introduza un número")
#      suma = 0
#      for char in x:
#          digito = int(char)
#          suma = digito + suma
         
#      print(suma)   
        
      
        
# numero()        





#_____________________________________________________________________________________________

# Carrera de caballos: la pista tiene 1000 metros y corren 4 caballos. Cada metro es una iteración.
# En cada iteración y por cada caballo el mismo puede avanzar de 1 a 5 metros (import random
# y use la función randint). Agregar al final de la iteración una demora del programa de 1
# segundo (import time y use la función sleep()) que permita ir viendo por pantalla en que
# metro está cada caballo dentro de la pista. Cuando el último caballo llegue a los 1000 metros,
# mostrar como quedó conformado el podio. 
#------------------------------------------------------------------------------------
#7


# import time
# import os
# import random
# from os import system, name
# from time import sleep

# def clearShell():
#       os.system('cls')



# def clear():
#     clearShell()
      


# def carrera_caballos():
      
  

#    Tornado = 0
#    Trueno = 0
#    Tormenta = 0
#    Rayo = 0      

#    hourses = [0,0,0,0]
#    podios = [0,0,0,0]
#    podio = 0
   
#    for x in range(1000):
      
#        if hourses[0]<1000:
#             hourses[0] += random.randint(1,5)
#             if hourses[0]>=1000:
#                   podios[podio] = 0
#                   podio += 1
                  
#        if hourses[1]<1000:
#             hourses[1] += random.randint(1,5)
#             if hourses[1]>=1000:
#                   podios[podio] = 1
#                   podio += 1           
                  
#        if hourses[2]<1000:
#             hourses[2] += random.randint(1,5)
#             if hourses[2]>=1000:
#                   podios[podio] = 2
#                   podio += 1            
                  
                  
#        if hourses[3]<1000:
#             hourses[3] += random.randint(1,5)
#             if hourses[3]>=1000:
#                   podios[podio] = 3
#                   podio += 1            
                  
                  
                  
                  
#        if((x%10)==0):
#             clear()
#             print(f"Posición Tornado: {hourses[0]}")    
#             print(f"Posición Trueno: {hourses[1]}")
#             print(f"Posición Tormenta: {hourses[2]}")
#             print(f"Posición Rayo: {hourses[3]}")  
#             time.sleep(0)      
      
       
      
#        if(hourses[0] >= 1000 and hourses[1] >= 1000 and hourses[2] >= 1000 and hourses[3] >= 1000) :
#             break
      
      
        
#    print(f'Primer puesto: {podios[0]}')
#    print(f'Segundo puesto: {podios[1]}')
#    print(f'Tercer puesto: {podios[2]}')
#    print(f'Cuarto puesto: {podios[3]}')
#    #sleep(5)
      
# carrera_caballos()




#_____________________________________________________________________________________________

# Imagine un Buffer de impresión con una capacidad máxima para almacenar 20 documentos,
# simule la gestión de la impresora en caso de falla a través de una cola circular del tipo FIFO
# (First In First Out), asuma que los documentos que superan la capacidad máxima se pierden.
# La selección del usuario será A, I o S, A para agregar documento, I imprimir y S salir del
# programa. En el caso de la operación Agregar, el usuario debe informar el nombre del
# documento que ingresará a la cola. 
#-----------------------------------------------------------------------------------------------
#8

documentos = []


def impresora(documentos):
  
  
  contador = 0
  
  while contador <= 25:
    
    
   if len(documentos) >= 20:
     print("Llegaste al tope de 20 elementos")  
     ultimo_elemento = documentos.pop(-1)
     print(documentos)
     
     
    
   opcion = input("Elija una opción: ")
        
   if opcion == "i":
        print(documentos)
        continue
    
   if opcion == "s":
         break
       
      
   else:
        agregar = int(input("¿Cuántos documentos quiere agregar?: "))
        for i in range(agregar):
            elemento = input("Ingrese el nombre del elemento a agregar:".format(i+1))  
            documentos.append(elemento)
    
        #r = impresora(elemento_agre)
     
        #return elemento_agre     
  contador = contador + 1  
  
  
  
impresora(documentos)

















     
#----------------------------------------------------------------------------------
#Ejemplo en clases, MATRICES



# Matriz = [
#      [3,-2,1,12],
#      [1,3,1,-4],
#      [2,2,-4,6]
# ]


# def sumatoria_matriz_fila(Matriz, fila):
#   suma = 0
#   for i in Matriz[fila]:
#      suma += i
#   print(f"La sumatoria es {suma}")
   
#------------------------------------------------------------

   
   
   
# transpuesta = [[fila[i] for fila in Matriz] for i in range(len(Matriz[0]))]   

# def sumatoria_matriz_columna(Matriz, columna): 
#     #transpuesta = [[fila[i] for fila in Matriz] for i in range(len(Matriz[0]))]
#     suma = 0
#     for i in Matriz[columna]:
#      suma += i
#     print(f"La suma es: " + str(suma))    

#sumatoria_matriz_columna(transpuesta,0)




#-----------------------------------------
#CRAMER


# def cramer():

#   matriz = [ [3,-2, 1,12],
#              [1, 3, 1,-4],
#              [2, 2,-4,6]
#   ]


#   #Sacar determinante:
  
#   deter1 = matriz[0][0] * matriz[1][1] * matriz[2][2]
#   deter2 = deter1 + (matriz[0][1] * matriz[1][2] * matriz[2][0])
#   deter3 = deter2 + (matriz[2][1] * matriz[1][0] * matriz[0][2])
  
#   deter4 = deter3 - (matriz[0][2] * matriz[1][1] * matriz[2][0])
#   deter5 = deter4 - (matriz[0][1] * matriz[1][0] * matriz[2][2])
#   deter6 = deter5 - (matriz[0][0] * matriz[1][2] * matriz[2][1])
#   print(f"Determinante: {deter6}")
  
  
  
#   #Primer valor:
#   val1 = matriz[0][3] * matriz[1][1] * matriz[2][2]
#   val2 = val1 + (matriz[0][1] * matriz[1][2] * matriz[2][3])
#   val3 = val2 + (matriz[0][2] * matriz[1][3] * matriz[2][1])
#   #Segunda parte
#   val4 = val3 - (matriz[0][2] * matriz[1][1] * matriz[2][3])
#   val5 = val4 - (matriz[0][1] * matriz[1][3] * matriz[2][2])
#   val6 = val5 - (matriz[0][3] * matriz[1][2] * matriz[2][1])
 
#   res1 = val6 // deter6
#   print(f"Primer valor(x): {res1}")
  
  
  
  
#   #Segunda valor
#   val7 = matriz[0][0] *matriz[1][3] * matriz[2][2]
#   val8 = val7 + (matriz[0][3] * matriz[1][2] *  matriz[2][0])
#   val9 = val8 + (matriz[0][2] * matriz[1][0] * matriz[2][3])
#   #Segunda parte
#   val10 = val9 - (matriz[0][2] * matriz[1][3] * matriz[2][0])
#   val11 = val10 - (matriz[0][3] * matriz[1][0] * matriz[2][2])
#   val12 = val11 - (matriz[0][0] * matriz[1][2] * matriz[2][3])
  
#   res2 = val12 //  deter6
#   print(f"Segundo valor(y): {res2}")
  
  
  
  
#   #Tercer valor
#   val13 = matriz[0][0] *matriz[1][1] * matriz[2][3]
#   val14 = val13 + (matriz[0][1] * matriz[1][3] *  matriz[2][0])
#   val15 = val14 + (matriz[0][3] * matriz[1][0] * matriz[2][1])
#   #Segunda parte
#   val16 = val15 - (matriz[0][3] * matriz[1][1] * matriz[2][0])
#   val17 = val16 - (matriz[0][1] * matriz[1][0] * matriz[2][3])
#   val18 = val17 - (matriz[0][0] * matriz[1][3] * matriz[2][1])
  
#   res3 = val18 //  deter6
#   print(f"Tercer valor(z): {res3}")
  
# cramer()  


      

      
      
     
      




      




        
        