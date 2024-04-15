"""
Solucion EjerciciosFuncionesCondicionalesIteracionRecursividad
Algorithmo y Estrutura de Datos
 
"""

########################  Cuestión 7 ##################################

#función que toma un número entero mayor que zero y retorna
#la suma de todos sus dígitos
def sumarDigitos(numero: int)->int:

    total=0
    strNumero = str(numero)
    for i in strNumero:
        total+=int(i)
    
    return total


print("""    Escribir una función que tome un número entero mayor
    que zero y retorna la suma de todos sus dígitos.
    Por ejemplo, el número 370 corresponderá al valor 10 (3+7+0).
    Si el parámetro leído no es un número entero mayor que zero,
    el programa terminará con el mensaje "Número Inválido"
    """)

try:

    A = int(input("Digite el número para sumar los digitos? "))
    if(A<0):
        print("Número Inválido")
    else:
        print(sumarDigitos(A))
        
except Exception as e:
    print(e)
    
    




