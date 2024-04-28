import string

def cifrado_cesar(frase, desplazamiento):
    alfabeto = string.ascii_lowercase
    resultado = ""
    for caracter in frase:
        if caracter.lower() in alfabeto:
            indice = alfabeto.index(caracter.lower())
            indice_desplazado = (indice + desplazamiento) % len(alfabeto)
            caracter_cifrado = alfabeto[indice_desplazado]
            if caracter.isupper():
                caracter_cifrado = caracter_cifrado.upper()
            resultado += caracter_cifrado
        else:
            resultado += caracter
    return resultado

def descifrado_cesar(frase_cifrada, desplazamiento):
    return cifrado_cesar(frase_cifrada, -desplazamiento)

def encontrar_desplazamiento(frase_cifrada):
    palabras_diccionario = [
        "inspiradora", "famoso", "frase", "algoritmo", "python"
    ]  # Agrega más palabras del diccionario según tus necesidades
    for desplazamiento in range(1, len(string.ascii_lowercase)):
        descifrado = descifrado_cesar(frase_cifrada, desplazamiento)
        palabras_encontradas = [
            palabra for palabra in palabras_diccionario if palabra in descifrado
        ]
        if len(palabras_encontradas) == len(palabras_diccionario):
            return desplazamiento, descifrado
    return None, None

# Ejemplo de uso
frase_original = "La creatividad es la inteligencia divirtiéndose."
desplazamiento = 7

# Cifrado César
frase_cifrada = cifrado_cesar(frase_original, desplazamiento)
print("Frase cifrada:", frase_cifrada)

# Descifrado inverso
frase_descifrada = descifrado_cesar(frase_cifrada, desplazamiento)
print("Frase descifrada:", frase_descifrada)

# Encontrar el desplazamiento utilizado en el cifrado
desplazamiento_encontrado, frase_descifrada = encontrar_desplazamiento(frase_cifrada)
if desplazamiento_encontrado is not None:
    print("Desplazamiento encontrado:", desplazamiento_encontrado)
    print("Frase descifrada:", frase_descifrada)
else:
    print("No se pudo encontrar el desplazamiento utilizado en el cifrado.")
