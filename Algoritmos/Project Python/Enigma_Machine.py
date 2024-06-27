

alfabeto = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
            4: 'E', 5: 'F', 6: 'G', 7: 'H',
            8: 'I', 9: 'J', 10: 'K', 11: 'L',
            12: 'M', 13: 'N', 14: 'O', 15: 'P',
            16: 'Q', 17: 'R', 18: 'S', 19: 'T',
            20: 'U', 21: 'V', 22: 'W', 23: 'X',
            24: 'Y', 25: 'Z'}


def posicion_inicial_rotor():
    Times1 = input("Ingrese el inicio del rotor I: ")
    Times2 = input("Ingrese el inicio del rotor IV: ")
    Times3 = input("Ingrese el inicio del rotor V: ")

    for key, valor in alfabeto.items():
        if Times1 == valor:
            Times1 = key 

    for key, valor in alfabeto.items():
        if Times2 == valor:
            Times2 = key

    for key, valor in alfabeto.items():
        if Times3 == valor:
            Times3 = key

    return Times1, Times2, Times3

#Times1, Times2, Times3 = posicion_inicial_rotor()

class Rotor:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def rotation(self, times):
        aux = [""] * 26
        for x in range(len(self.alphabet)):
            aux[x] = self.alphabet[(x + times) % 26]
        self.alphabet = aux         


ROTOR_5 = Rotor([4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9])
#necesito que me devuelva el VALOR en ese INDICE
ROTOR_4 = Rotor([4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1])

ROTOR_1 = Rotor([21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10])
# INDICE donde esta ese VALOR
REFLECTOR = Rotor([24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19])



class enigma:
    def __init__(self, frase):
        self.frase_numerica = frase


    def Rotor_1(self, Rotor, n_rotate, returning, count_rotate, indice):
        Rotor.rotation(n_rotate)
        #print(Rotor.alphabet)
        tester = 0 #variable para cuando la resta: Rotor.alphabet[y] - count_rotate da nuemros negativos
        for y in range(len(Rotor.alphabet)):
            if returning == False and self.frase_numerica[indice] == y:
                tester = Rotor.alphabet[y] - count_rotate
                if tester < 0:
                    tester = (tester + 26) % 26
                self.frase_numerica[indice] = tester
                break
            elif returning == True and self.frase_numerica[indice] == Rotor.alphabet[y]:
                self.frase_numerica[indice] = (y + count_rotate) % 26 #se le suma la cantidad de veces que roto ya que lo que antes era n ahora es o
                break
        return self.frase_numerica
 

    def Rotor_R(self, Rotor, count_rotate, indice):
        for y in range(len(Rotor.alphabet)):
            if self.frase_numerica[indice] == y:
                self.frase_numerica[indice] = (Rotor.alphabet[y] + count_rotate) % 26
                break
        return self.frase_numerica
        
def maquina_enigma():
    rotations_1 = 1 #Estas variables son las responsables de correr los rotores la cantidad de veces necesarias
    rotations_2 = 0
    rotations_3 = 0
    count_rotate1 = 1 + Times1  #Estas variables se utilizan para saber cuan corido esta el rotor de su posicion inicial
    count_rotate2 = Times2
    count_rotate3 = Times3
    position_rotate1 = 1 #estas variables son las responsables de que el siguiente rotor gire unicamente cuando el anterior realizo la vuelta completa
    position_rotate2 = 0
    position_rotate3 = 0
    frase = (list)(input("Ingrese la frase: ").upper())
    frase_numerica = []
    frase_cifrada = []
    frase_cifrada_completa = []
    returning = False #para saber si esta "viniendo" o "volviendo" en el cifrado, por que dependiendo que esta haiendo depende que variables se le debe ingresar
    aux = enigma(frase_numerica)
    for x in frase: #funcion que pasa la frase a numeros
        if x == ' ':
            frase_numerica.append(1000)
        for key, value in alfabeto.items():            
            if x == str(value):  
                frase_numerica.append(key)
    for x in range(len(frase_numerica)):
        if frase_numerica[x] != 1000: #si el valor es 1000, significa que es un espacio
            aux.Rotor_1(ROTOR_5, rotations_1, returning, count_rotate1, x) #se llama al objeto rotor y la funcion de cifrado de cada rotor
            aux.Rotor_1(ROTOR_4, rotations_2 , returning, count_rotate2, x)
            aux.Rotor_1(ROTOR_1, rotations_3, returning, count_rotate3, x)
            aux.Rotor_R(REFLECTOR, count_rotate3, x)
            returning = True
            aux.Rotor_1(ROTOR_1, 0, returning, count_rotate2, x)
            aux.Rotor_1(ROTOR_4, 0, returning, count_rotate1, x)
            aux.Rotor_1(ROTOR_5, 0, returning, 0, x)
            frase_cifrada.append(aux.frase_numerica[x])
            rotations_2 = 0
            rotations_3 = 0
            rotations_1 = 1
            if position_rotate1 == 25:
                count_rotate1 = -1
                count_rotate2 += 1
                rotations_2 = 1
                position_rotate1 = -1
                position_rotate2 += 1
            if position_rotate2 == 25:
                count_rotate2 = 0
                count_rotate3 += 1
                rotations_3 = 1
                position_rotate2 = 0
            if position_rotate3 == 25:
                count_rotate3 = 0
                position_rotate3 = 0
            returning = False
            count_rotate1 += 1
            position_rotate1 += 1
        else:
            frase_cifrada.append(aux.frase_numerica[x])
        
    for x in frase_cifrada:
        for key, value in alfabeto.items():
            if x == 1000:
                frase_cifrada_completa.append(" ")
                break                        
            if x == key:  
                frase_cifrada_completa.append(value)
    sentance = ''.join(frase_cifrada_completa)
    print(sentance) 


Opcion = (input("Que desea hacer hoy?: 1. Para codificar frase, 2. para decodificar: ")) 

if int(Opcion) == 1:
    print("--------------------------------------INICIO DE ROTORES--------------------------------------")
    Times1, Times2, Times3 = posicion_inicial_rotor()
    ROTOR_5.rotation(Times1)
    ROTOR_4.rotation(Times2)
    ROTOR_1.rotation(Times3)
    print("--------------------------------------FRASE PARA CODIFICAR--------------------------------------")
    maquina_enigma()
elif int(Opcion) == 2:
    print("--------------------------------------INICIO DE ROTORES--------------------------------------")
    Times1, Times2, Times3 = posicion_inicial_rotor()
    ROTOR_5.rotation(Times1)
    ROTOR_4.rotation(Times2)
    ROTOR_1.rotation(Times3)
    print("FRASE PARA DECODIFICAR".center(100, '-'))
    maquina_enigma()




    








    

    