# TRABAJO PRÁCTICO N° 1 | CIFRADOR CÉSAR | 2° INGENIERÍA EN SISTEMAS DE LA INFORMACIÓN | 18/04/2024

"""
Integrantes:
BAEZA GRAF, Santiago #36873
BLOCK ERNST, Andrew #36766
ORDOÑEZ, Joaquín #37525
URIBE, Franco #36480
"""

# Se importa una librería para la utilización de listas de los abecedarios.
import string

# Se referencia al documento de texto que está dentro de la carpeta del --*CIFRADOR CÉSAR*--
formato = open("diccionario.txt", "r", encoding="UTF-8")  
diccionario = [linea.strip() for linea in formato.readlines()]

# Listas de abecedarios (MINÚSCULA Y MAYÚSCULA)
abecedario_Upper = list(string.ascii_uppercase)
abecedario_Lower = list(string.ascii_lowercase)

# Función de codificación de una frase en español.
def codificar(frase, desplazamiento): 

    for i in range(len(abecedario_Upper)):
        pos = i + desplazamiento
        if pos > 25:
            pos = pos - 26
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido
    return frase.upper()

# Función que decodifica una frase cifrada con un número de desplazamiento específico.
def decodificar(frase, desplazamiento):

    for i in range(len(abecedario_Upper)):
        pos = i - desplazamiento
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido
    return frase.upper()

# Función que decodifica de manera automática a una frase cifrada sin que se sepa cual es el desplazamiento correcto.
def super_decodificado(frase):
    
    # División la cadena en la lista palabra por palabra, sacando los espacios en blanco. Se almacenan en frase_palabras.
    frase_palabras = frase.split(' ')

    # Variable que almacena temporalmente las palabras desplazdas.
    palabras_Aux = []

    # String vacía que contendrá a la frase completa.
    frase_final = ''

    # Contandor que hace la validación de la palabras decodificadas.
    chequeo = 0

    # Iteración que recorre los 25 desplazamientos posibles.
    for desplazamiento in range(26):

        # Iteración que recorre la palabra cifrada con todos los desplazamientos que le corresponden. Agregando las palabras decodificadas en palabras_Aux
        for palabra in frase_palabras:
            palabra_decodificada = decodificar(palabra, desplazamiento).lower()
            palabras_Aux.append(palabra_decodificada)

        # Al total del recorrido de las palabras decodificadas con su desplazamiento correspondiente. Se las almacena y concatena a la frase_final con un espacio entre medio.
        for i in range(len(palabras_Aux)):
            frase_final += palabras_Aux[i] + ' '

            # Iteración del largo del diccionario.txt
            for j in range(len(diccionario)):
                
                # Si la palabra correspondiente al índice [i] aparecen en el diccionario. Se suma un chequeo (Palabras encontradas en el diccionario)
                if palabras_Aux[i] == diccionario[j]:
                    chequeo += 1
                    
        # Si la cantidad de palabras en el diccionario es mayor a la mitad de la longitud de la frase. Se agregan las palabras decodificadas a frase_final, si no se vacía.    
        if chequeo <= (len(frase_palabras) / 2):
                frase_final = ''
                
        # Frase descifrada con el número de desplazamiento correcto.
        else:
            print(f'{frase_final.upper()} \nDESPLAZAMIENTO CORRECTO N°: {desplazamiento}') 
        chequeo = 0
        palabras_Aux.clear()

# Opciones disponibles para el --*CIFRADOR CÉSAR*--
while True:
    op = input('\n--* CIFRADOR CÉSAR *--\n1. CODIFICAR \n2. DECODIFICAR \n3. SUPER DECODIFICADO\n4. SALIR \n---------------------- \nELEGIR OPCIÓN: ')

    # Opciones disponibles dentro de las funciones del --*CIFRADOR CÉSAR*--
    if op == '1':
        print(codificar(input('Escriba frase a codificar: ').upper(), int(input('Escriba el número de desplazamiento: '))))
    elif op == '2':
        print(decodificar(input('Escriba frase codificada: ').upper(), int(input('Escriba el numero de desplazamiento: '))))
    elif op == '3':
        super_decodificado(input('Escriba la frase cifrada: ').upper())
    elif op == '4': 
        quit()
    # Validez del tipo opción ingresada.
    else:
        print('¡OPCIÓN NO VALIDA, INTENTE NUEVAMENTE!')
