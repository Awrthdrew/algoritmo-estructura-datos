import string

formato = open("diccionario.txt", "r", encoding="UTF-8")  
diccionario = [linea.strip() for linea in formato.readlines()]

abecedario_Upper = list(string.ascii_uppercase)
abecedario_Lower = list(string.ascii_lowercase)

def codificar():
    frase = input('Escriba frase a codificar: ').upper()
    desplazamiento = int(input('Escriba el número de desplazamiento: '))

    for i in range(len(abecedario_Upper)):
        pos = i + desplazamiento
        if pos > 25:
            pos = pos - 26
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido
        
    print(frase.upper())

def decodificar():
    frase = input('Escriba frase codificada: ').upper()
    desplazamiento = int(input('Escriba el numero de desplazamiento: '))

    for i in range(len(abecedario_Upper)):
        pos = i - desplazamiento
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido

    print(frase.upper())

def decodificarAux(frase, desplazamiento):

    for i in range(len(abecedario_Upper)):
        pos = i - desplazamiento
        traducido = frase.replace(abecedario_Upper[i], abecedario_Lower[pos])
        frase = traducido
    return frase

def super_decodificado(frase_cifrada):
    frase_cifrada_dividida = frase_cifrada.split(" ")
    frase_decodificada = ''
    for desplazamiento in range(26):
        for palabra in frase_cifrada_dividida:
            palabra_decodificada = decodificarAux(palabra, desplazamiento)
            if palabra_decodificada in diccionario:
                frase_decodificada += " " + palabra_decodificada
                desplazamiento_correcto = desplazamiento
    print(f'{frase_decodificada.upper()} \nDESPLAZAMIENTO CORRECTO N°: {desplazamiento_correcto}')    
    


while True:
    op = input('\n--* CIFRADOR CÉSAR *--\n1. CODIFICAR \n2. DECODIFICAR \n3. SUPER DECODIFICADO\n4. SALIR \n---------------------- \nELEGIR OPCIÓN: ')

    #Casos dentro del menú   
    if op == '1':
        codificar()
    elif op == '2':
        decodificar()
    elif op == '3':
        frase_cifrada = input('Escriba la frase cifrada: ').upper()
        super_decodificado(frase_cifrada)
    elif op == '4':
        quit()
    else:
        print('¡OPCIÓN NO VALIDA, INTENTE NUEVAMENTE!')