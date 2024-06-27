
import random

alfabeto = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
#La persona introducira cuanto se quiere que se mueva el cifrado y el diccionario sabra que letra es por que sera un recorrido de x + 3 si quiere que se corra en 3 por ejemplo
#contador_alfabeto = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'Ñ': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
#orden_letras_repetidas = ('E', 'A', 'O', 'S', 'R', 'N', 'I', 'D', 'L', 'C', 'T', 'U', 'M', 'P', 'B', 'G', 'V', 'Y', 'Q', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W')
Opcion = (input("Que desea hacer hoy?: 1. Para codificar frase, 2. para decodificar, 3. Para desfasar arbitrariamente el alfabeto: ")) 

#la bailarina de auschwitz
def codificador(alfabeto, frase):
    frase_codificada = []
    key_palabra_cod = [] 
    for x in frase:
        if x == ' ':
            key_palabra_cod.append(1000) #Valor para cuando hay un espacio en la frase, es 1000 por que quize y para asegurarme que sin importar el desfase nunca de 1000 una de las
        for key, value in alfabeto.items():            
            if x == str(value):  
                if (int(key) + int(desfase)) > 26:
                    key_palabra_cod.append((int(key) + int(desfase)) - 26)
                else:
                    key_palabra_cod.append(int(key) + int(desfase))
            
    for x in key_palabra_cod:
        for key, value in alfabeto.items():
            if x == 1000:
                frase_codificada.append(" ")
                break
            if x == key:
                frase_codificada.append(value)
    sentance = ''.join(frase_codificada)
    print(sentance)

def decodificador(alfabeto, frase):
    frase_codificada = []
    key_palabra_cod = []
    for x in frase:
        if x == ' ':
            key_palabra_cod.append(1000)
        for key, value in alfabeto.items():
            if x == value:
                if (int(key) - int(desfase)) < 1:
                    key_palabra_cod.append(int(key) - int(desfase) + 26)
                else:
                    key_palabra_cod.append(int(key) - int(desfase))
    for x in key_palabra_cod:
        for key, value in alfabeto.items():
            if x == 1000:
                frase_codificada.append(" ")
                break
            if x == key:
                frase_codificada.append(value)
    sentence = ''.join(frase_codificada)
    print(sentence)


def bombe_machine(alfabeto, frase, sentance, frase_codificada, key_palabra_cod, cantidad_desfases):
    for s in range(cantidad_desfases):
        desfase = random.randint(1,26)
        print("El alfabeto numero: " + str(s + 1) + " se desfaso " + str(desfase) + " veces")
        for x in frase:
            if x == ' ':
                key_palabra_cod.append(1000) #Valor para cuando hay un espacio en la frase, es 1000 por que quize y para asegurarme que sin importar el desfase nunca de 1000 una de las
            for key, value in alfabeto.items():            
                if x == str(value):  
                    if (int(key) + int(desfase)) > 26:
                        key_palabra_cod.append((int(key) + int(desfase)) - 26)
                    else:
                        key_palabra_cod.append(int(key) + int(desfase))
            
        for x in key_palabra_cod:
            for key, value in alfabeto.items():
                if x == 1000:
                    frase_codificada.append(" ")
                    break
                if x == key:
                    frase_codificada.append(value)
        borrador = ''.join(frase_codificada)
        frase_codificada = []
        key_palabra_cod = []
        frase = borrador
    sentance = borrador
    return sentance



if int(Opcion) == 1:
    frase = (list)(input("Introduzca la frase que quiere codificar (En mayuscula): "))
    desfase = (int)(input("en cuanto desea desfasar la frase?: "))
    codificador(alfabeto, frase)
elif int(Opcion) == 2:
    frase = (list)(input("Introduzca la frase que quiere decodificar (En mayuscula): "))
    desfase = (int)(input("en cuanto esta desfasada la frase?: "))
    decodificador(alfabeto, frase)
elif int(Opcion) == 3:
    frase = (list)(input("Introduzca la frase que quiere codificar (En mayuscula): "))
    cantidad_desfases = (int)(input("cuantas alfabetos queres que se desplacen arbitrariamente: "))
    sentance = ''
    frase_codificada = []
    key_palabra_cod = []
    sentance = bombe_machine(alfabeto, frase, sentance, frase_codificada, key_palabra_cod, cantidad_desfases)
    print("La frase queda en: " + sentance)
#me lo re mil complique ya se pero funciona.









"""
elif int(Opcion) == 3:
    frase = (list)(input("Introduzca la frase que quiere decodificar automaticamente (En mayuscula): "))
    desfase = decodificador_automatico(alfabeto, frase, contador_alfabeto, orden_letras_repetidas)
    decodificador_au(alfabeto, frase, desfase)

"""


























#Intento de desifrador automatico, saca el desfase pero falla la ocmparacion, tambien tiene problemas con los tildes y cuando compara con el diccionario dado en el trabajo, como la palabra "a" o "h" aparecen en el diccionario, algunas veces le pega justo a eso y lo cuenta como terminado, cunado en realidad esta mal.

def decodificador_automatico(alfabeto, frase, contador_alfabeto, orden_letras_repetidas):
    frase_codificada = []
    key_palabra_cod = []
    most_repeted_leter = ''
    intento = 0
    intentotwo = 0
    contador_repeticion = 0
    x = 0

    for x in frase:
        for key, value in contador_alfabeto.items():
            if x == key:
                contador_alfabeto[key] = int(value) + 1

    for key, value in contador_alfabeto.items():
        if int(value) > contador_repeticion:
            most_repeted_leter = key
            contador_repeticion = value
    print(most_repeted_leter)

    for key, value in alfabeto.items():
        if most_repeted_leter == value:
            intento = key
    print(intento)

    if x in range(len(orden_letras_repetidas)):
        for z in orden_letras_repetidas:
            for key, value in alfabeto.items():
                if z == value:
                    intentotwo = key


    desfase = abs(intento - intentotwo)
    #print(desfase)
    return desfase


def decodificador_au(alfabeto, frase, desfase):
    frase_codificada = []
    key_palabra_cod = []
    for x in frase:
        if x == ' ':
            key_palabra_cod.append(1000)
        for key, value in alfabeto.items():
            if x == value:
                if (int(key) - int(desfase)) < 1:
                    key_palabra_cod.append(int(key) - int(desfase) + 27)
                else:
                    key_palabra_cod.append(int(key) - int(desfase))
    for x in key_palabra_cod:
        for key, value in alfabeto.items():
            if x == 1000:
                frase_codificada.append(" ")
                break
            if x == key:
                frase_codificada.append(value)
    sentence = ''.join(frase_codificada)
    print(sentence)



