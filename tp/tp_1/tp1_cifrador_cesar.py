import string



abecedario_Upper = list(string.ascii_uppercase)
abecedario_Lower = list(string.ascii_lowercase)

def Codificar():
    frase = input('Escriba frase a codificar: ').upper()
    desplazamiento = int(input('Escriba el numero de desplazamiento: '))

    for i in range(len(abecedario_Upper)):
        pos = i + desplazamiento
        if pos > 25:
            pos = pos - 26
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido
        
    print(frase.upper())

def Decodificar():
    frase = input('Escriba frase codificada: ').upper()
    desplazamiento = int(input('Escriba el numero de desplazamiento: '))

    for i in range(len(abecedario_Upper)):
        pos = i - desplazamiento
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido

    print(frase.upper())

def Bomba(frase_cifrada):
    for desplazamiento in range(26):
        descifrada = ''
        for letra in frase_cifrada:
            if letra.split():
                indice = abecedario_Upper.index(letra)
                descifrada += abecedario_Upper[(indice - desplazamiento) % 26]
            else:
                descifrada += letra
        print(f"Desplazamiento N° {desplazamiento}: {descifrada}")
        
"""def op_valida(op): #Función que permite únicamente ingresar valores enteros para que el menú del cifrador avance en la tarea designada.
    try:
        op_int = int(op)
    except ValueError:
        return False
    return 1 <= op_int <= 4"""
        

while True:
    op = input('\n--* CIFRADOR CÉSAR *--\n1. CODIFICAR \n2. DECODIFICAR \n3. BOMBA\n4. SALIR \n---------------------- \nELEGIR OPCIÓN: ')
    
    #Se valida el (int) ingresado
    """if op_valida(op):
        op_int = int(op)"""
        
    #Casos dentro del menú   
    if op == '1':
        Codificar()
    elif op == '2':
        Decodificar()
    elif op == '3':
        frase_cifrada = input('Escriba la frase cifrada: ').upper()
        Bomba(frase_cifrada)
    elif op == '4':
        quit()
    else:
        print('¡OPCIÓN NO VALIDA, INTENTE NUEVAMENTE!')
