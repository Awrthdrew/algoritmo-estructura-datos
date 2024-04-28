# Array del alfabeto completo.
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Función para generar el alfabeto cifrado
def generaAlfa(alfa, key):
    # Largo del array2

    larg = 26 - key
    # Largo del corte
    array1 = alfa[:key]
    # Nuevo array después del corte
    array2 = alfa[key:key+larg]
    # Pegar array2 y corte, mandar corte al final
    beta = array2 + array1
    
    return beta

# Imprimir menú
print("Seleccionar una opción")
print("     1. Cifrar palabra")
print("     2. Decifrar palabra")
menu = input()

if menu == '1':
    # Ingreso de la palabra deseada a cifrar
    frase = input("Ingresar palabra a cifrar (en letras mayusculas):\n")
    print("Advertencia: solo se pueden cifrar palabras con letras mayúsculas\n")
    letra = list(frase)
    
    # Ingreso de la llave
    key = int(input("Ingresar llave (la llave debe ser un número entre 1 y 24):\n"))
    
    # Inicio de cifrado
    beta = generaAlfa(alfa, key)
    frasenum = None
    r = []
    
    for i in range(len(letra)):
        frasenum = alfa.index(letra[i])
        r.append(frasenum)
    
    # Imprime frase cifrada
    print("Palabra cifrada: ", end="")
    for l in r:
        print(beta[l], end="")
    
    print("\n")
else:
    # Desencriptar: Entrada: Cadena de caracteres codificada. Tengo la clave para desencriptar.
    fraseEncript = input("Ingresar Palabra: ")
    arrayFraseEncript = list(fraseEncript)
    beta = generaAlfa(alfa, key)
    p = []
    
    for i in range(len(arrayFraseEncript)):
        toEncrypt = beta.index(arrayFraseEncript[i])
        p.append(toEncrypt)
    
    for x in p:
        print(alfa[x], end="")
    
    print()
