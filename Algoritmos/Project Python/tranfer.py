array = [25, 18, 21, 8, 17, 19, 12, 4,
            16, 24, 14, 7, 15, 11, 13, 9,
            5, 2, 6, 26, 3, 23, 22, 10, 1, 20]

for x in range(len(array)):
    array[x] = array[x] - 1

print(array)


alfabeto = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
            4: 'E', 5: 'F', 6: 'G', 7: 'H',
            8: 'I', 9: 'J', 10: 'K', 11: 'L',
            12: 'M', 13: 'N', 14: 'O', 15: 'P',
            16: 'Q', 17: 'R', 18: 'S', 19: 'T',
            20: 'U', 21: 'V', 22: 'W', 23: 'X',
            24: 'Y', 25: 'Z'}



"""
def enigma_cipher(Rotor_1, Rotor_4, Rotor_5):
    frase = (list)(input("Introduzca la frase que quiere codificar (En mayuscula): "))
    frase_numerica = []
    for x in frase:
        for key, value in alfabeto.items():
            if x == value:
                frase_numerica.append(key)
    
    index = 0
    for x in frase_numerica:
        for y in range(len(Rotor_1.alphabet)):
            if x == y:
                
                frase_numerica[index] = Rotor_1.alphabet[y]
        index +=1

    index = 0
    for x in frase_numerica:
        for y in range(len(Rotor_4.alphabet)):
            if x == y:
                
                frase_numerica[index] = Rotor_4.alphabet[y]
        index +=1

    index = 0
    for x in frase_numerica:
        for y in range(len(Rotor_5.alphabet)):
            if x == y:
                
                frase_numerica[index] = Rotor_5.alphabet[y]
        index +=1
    print(frase_numerica)
"""




"""

def enigma_cipher(Rotor, frase_numerica):
    index = 0
    for x in frase_numerica:
        for y in range(len(Rotor.alphabet)):
            if x == y:
                
                frase_numerica[index] = Rotor.alphabet[y]
        index +=1
    return frase_numerica



def maquina_enigma():
    frase = (list)(input("Introduzca la frase que quiere codificar (En mayuscula): "))
    frase_numerica = []
    for x in frase:
        for key, value in alfabeto.items():
            if x == value:
                frase_numerica.append(key)
    
    
    frase_numerica = enigma_cipher(ROTOR_1, frase_numerica)
    frase_numerica = enigma_cipher(ROTOR_4, frase_numerica)
    frase_numerica = enigma_cipher(ROTOR_5, frase_numerica)
    #frase_numerica = enigma_cipher(REFLECTOR, frase_numerica)
    return frase_numerica

frase_numerica = maquina_enigma()
print(frase_numerica)
"""



def maquina_enigma():
    rotations_1 = 1
    rotations_2 = 0
    rotations_3 = 0
    frase = (list)(input("Frase que desea codificar mi rey: "))
    frase_numerica = []
    for x in frase:
        if x == ' ':
            frase_numerica.append(1000) #Valor para cuando hay un espacio en la frase, es 1000 por que quize y para asegurarme que sin importar el desfase nunca de 1000 una de las
        for key, value in alfabeto.items():            
            if x == str(value):  
                frase_numerica.append(key)

    print(frase_numerica)

maquina_enigma()