"""
Solucion EjerciciosFuncionesCondicionalesIteracionRecursividad
Algorithmo y Estrutura de Datos
 
"""

########################  Cuestión 5 ##################################

def media(calificacion1: int, calificacion2:int, calificacion3:int, tipoMedia:str):

    #calcula la media aritimetica
    valorMedia=0
    match tipoMedia:
        case "A":
            valorMedia=(calificacion1 + calificacion2 + calificacion3)/3
        #promedio ponderado,con pesos 5, 3 y 2    
        case "P":
            valorMedia=(calificacion1*5 + calificacion2*3 + calificacion3*2)/(5+3+2)
            
        case _:
            print("CALCULO NO DISPONIBLE")
            
    return valorMedia
    
  

     
print("""5. Escribir una función que tome tres calificaciones de un
    estudiante como parámetro y una letra. Si la letra es A, la
    función debe calcular la media aritmética de las calificaciones
    del estudiante, si es P, debe calcular el promedio ponderado,
    con pesos 5, 3 y 2
    \n""")

#leer 3 calificaciones en separado
A = int(input("Cuál es el valor de la calificacion 1? "))
B = int(input("Cuál es el valor de la calificacion 2? "))
C = int(input("Cuál es el valor de la calificacion 3? "))
tipo = str(input("\nCuál es el tipo de média digite A para media aritimetica y \nP para media ponderada? "))

print ( media(A,B,C,tipo) )
