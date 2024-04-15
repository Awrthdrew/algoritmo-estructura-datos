"""
Solucion EjerciciosFuncionesCondicionalesIteracionRecursividad
Algorithmo y Estrutura de Datos
 
"""

########################  Cuestión 6 ##################################
def fatorialDobleDecrescente(numero:int):
    
    if(numero<0 or numero%2==0):
        print("\nEl numero debe ser entero, positivo y impar")
        return
    
    calculo = numero
    #opcion 1 para el loop
    while (numero-2)>0:
        #esta impression es opcional
        print(numero,end=" ")
        numero = numero-2
        calculo = calculo*numero
        
    #esta impression es opcional
    print(numero,end=" ")

    
    print("\nEl fatorial doble es " + str(calculo))
    
def fatorialDobleCrescente(numero:int):
    
    if(numero<0 or numero%2==0):
        print("\nEl numero debe ser entero, positivo y impar")
        return
    
    calculo = numero

    #opcion 2 para el loop
    numAux=calculo=1
    
    while numero>numAux:
        #esta impression es opcional
        print(numAux,end=" ")
        
        numAux = numAux + 2
        calculo = calculo*numAux
        
    #esta impression es opcional
    print(numAux,end=" ")
    
    print("\nEl fatorial doble es " + str(calculo))
    

print("""
    6.	Escribir una función no recursiva que tome un número entero
    positivo impar N y devuelva el factorial doble de ese número.
    El factorial doble se define como el producto de todos los
    números naturales impares desde 1 hasta algún número natural
    impar N. Por exemplo el doble factorial de 5 es: 5! = 1 * 3 * 5 = 15
    \n""")

numero = int(input("Que numero deseas calcular? "))

#observe que numero se mantiene el mismo,
#por eso puedo utilizar en la llamada de las dos funciones
fatorialDobleCrescente(numero)
fatorialDobleDecrescente(numero)

