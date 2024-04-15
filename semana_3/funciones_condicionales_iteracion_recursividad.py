#Ejercicio ver qué tipo de triángulo es -> Equilátero, Isósceles, Escaleno
"""def tipoTriangulo(lado_a, lado_b, lado_c): 
        if lado_a == lado_b and lado_b == lado_c and lado_c == lado_a:
            print('ES TRIÁNGULO EQUILÁTERO PELELE')   
        elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
            print('ES TRIÁNGULO ESCALENO PELELE')
        #elif lado_a != lado_b or lado_b != lado_c or lado_c != lado_a: Esto permite verificar si al menos una de las dos lados son iguales. 
        else:
            print('ES TRIÁNGULO ISÓSCELES PELELON')
        
        
            
def main():
    bucle = True
    while bucle:
        a = int(input("LADO A (PRESIONA 0 SI DESEAS SALIR O): "))
        if a == 0:
            break
                
        b = int(input("LADO B (PRESIONA 0 SI DESEAS SALIR O): "))
        if b == 0:
            break
        
        c = int(input("LADO C (PRESIONA 0 SI DESEAS SALIR): "))
        if c == 0:
            break
        
        tipoTriangulo(a,b,c) 
main()"""


#Ejercicio función N a 1000. 

"""def numeros():
    n = 1000
    a = int(input("Ingrese un número entre 0 y 1000: "))
    
    if a > n:
        print("Por favor, ingresa un número menor o igual a 1000.")
        

    contador = 0
    print("Imprimiendo números del 0 al", a, "utilizando while:")
    while contador <= a:
        print(contador, end = ', ')
        contador += 1
    print("\n")

    print("Imprimiendo múltiplos de 2 del 0 al", a)
    for i in range(0, a + 1, 2):
        print(i, end=', ')
    
numeros()"""

    
    
    
    
# Ejercicio n° romanos = resultado
"""def romano_numero(numero):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numeros_romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    resultado_romano = ' '
    
    for i in range(len(numeros)):
        while numero >= numeros[i]:
            resultado_romano += numeros_romanos[i]
            numero -= numeros[i]
    
    return resultado_romano

while True:
  try:
    numero = int(input("Ingrese un número entero hasta el 1000: "))
    if numero < 1 or numero > 1000:
      print("El número debe estar en el rango de 1 a 1000.")
    else:
      print("El número romano equivalente es:", romano_numero(numero))
  except ValueError:
    print("Por favor, ingrese un número entero válido.")"""
    
    
    
    
    
#Media aritmética y promedios   
def media_aritmetica_y_promedio(nota1, nota2, nota3, tipo_promedio):
    if tipo_promedio == 'A' or tipo_promedio == 'a':
        return((nota1 + nota2 + nota3)/3)
    elif tipo_promedio == 'P' or tipo_promedio == 'p':
        return((nota1 + nota2 + nota3)/10)
    else:
        raise ValueError('SOLO MEDIA ARITMÉTICA Y PROMEDIO (A ó P)')

notas = [] 
tipo = []   
bucle = True

for i in range(3):
    while bucle:
        num = int(input('Ingrese nota a promediar: '))
        if 0 >= num or num > 10:
            print('No existe tal calificación para promediar')
        else:
            notas.append(num)
            bucle = False      
    

        
print(f'\n EL PROMEDIO FINAL ES: {notas, tipo}')