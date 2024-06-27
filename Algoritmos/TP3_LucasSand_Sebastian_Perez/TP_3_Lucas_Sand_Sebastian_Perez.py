normal_aphabet = ["a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y","z"]

#Clase de Rotor
class Rotor:
    def __init__(self,alphabet):        #constructor de los rotores
        self.rotor_alphabet = alphabet      #se le define un alfabeto que ya viene desfazado en base a los valores que retorna el original
        self.rotations = 0      #valor de cuanas veces se roto el rotor se inicia en 0

    def rotate(self,times):     #funcion que va a rotar el alfabeto y contar las rotaciones
        aux = [""]*26       #se crea un array de strings vacio
        for o in range(len(self.rotor_alphabet)):
            aux[o] = self.rotor_alphabet[(o+times)%26]      #para cada valor de el array que se quiere correr se le suma el valor de desfazaje y se le hace el resto por 26 para que no se pase del index, se lo añade al array vacio en su posicion indicada
        self.rotor_alphabet = aux       #se igualan los arrays para que el array original ahora sea el array rotado/desfazado
        self.rotations += times    #se le suma 1 a las rotaciones porque el rotor se roto 1 vez

#definicion de rotores
Rotor_1 = Rotor(
                ["e", "k", "m", "f", "l",
                "g", "d", "q", "v", "z",
                "n", "t", "o", "w", "y",
                "h", "x", "u", "s", "p",
                "a", "i", "b", "r", "c","j"] 
                )

                                
Rotor_4 = Rotor(
                ["e", "s", "o", "v", "p",
                "z", "j", "a", "y", "q",
                "u", "i", "r", "h", "x",
                "l", "n", "f", "t", "g",
                "k", "d", "c", "m", "w","b"] 
                )


Rotor_5 = Rotor(
                ['v', 'z', 'b', 'r', 'g',
                 'i', 't', 'y', 'u', 'p',
                 's', 'd', 'n', 'h', 'l',
                 'x', 'a', 'w', 'm', 'j',
                 'q', 'o', 'f', 'e', 'c', 'k']
                )

Reflector_B = Rotor(        # el alphabeto del reflector es diferente, en este caso es cuantos index se van a sumar para llegar hasta la otra letra
                    [24, 16, 18, 4, 12,
                    13, 5, 22, 7, 14,
                    3, 21, 2, 23, 24,
                    19, 14, 10, 13, 6,
                    8, 1, 25, 12, 2, 20]
                    )

# def search_index_by_letter(letter, aphabet):    #basicamente busca el index de una letra del diccionario que le pases
#         for x in range(len(aphabet)):       #compara todas las posiciones del array para ver si encuentra la letra
#             if aphabet[x] == letter.lower():    #copara las letras en minuscula
#                 return x        #si la encuentra lo returnea
#                 break

class Enigma:       #hago una clase enigma en vez de un programa, ya que podria ingresarle diferentes rotores a la hora de crearla y asi poder hacer muchas mas combinaciones, no solo un programa con los rotores I, IV y V
    def __init__(self,rotor_a, rotor_b, rotor_c, reflector):    #se definin los rotores y reflectores que se van a usar
        self.rotor_a = rotor_a
        self.rotor_b = rotor_b
        self.rotor_c = rotor_c
        self.reflector = reflector
    
    def search_index_by_letter(self, letter, aphabet):    #basicamente busca el index de una letra del diccionario que le pases
        for x in range(len(aphabet)):       #compara todas las posiciones del array para ver si encuentra la letra
            if aphabet[x] == letter.lower():    #copara las letras en minuscula
                return x        #si la encuentra lo returnea
                break

    def enigma_functioning(self, phrase):        #funcion que va a ser el cifrado y descifrado de la maquina
        coded_phrase = ""   #defino la frase que voy a retornar
        aux = ""
        aux2 = ""
        aux4 = ""
        aux5 = ""
        aux6 = ""
        aux7 = ""
        for letter in phrase:
            if letter == " ":
                coded_phrase +=" "
            elif letter == "?":
                coded_phrase +="?"
            elif letter == "¿":
                coded_phrase +="¿"
            elif letter == "!":
                coded_phrase +="!"
            elif letter == "¡":
                coded_phrase +="¡"
            elif letter == ".":
                coded_phrase +="."
            elif letter == ",":
                coded_phrase +=","
            else:
                #primer rotor (rotor 5)
                self.rotor_c.rotate(1)   #como en la maquina original lo primero que se hace al cifrar una letra es rotar el primer rotor
                aux = self.rotor_c.rotor_alphabet[self.search_index_by_letter(letter, normal_aphabet)]
                # print("rotaciones del rotor 5: "+ str(self.rotor_c.rotations))
                # print("rotaciones del rotor 4: "+ str(self.rotor_b.rotations))
                # print("rotaciones del rotor 1: "+ str(self.rotor_a.rotations))
                # print("letra a codificar: "+ letter)
                # print(aux)
                #segundo rotor (rotor 4)
                if self.rotor_c.rotations %26 == 0 and self.rotor_c.rotations > 0:        #si el primer rotor ya dio 1 vuelta completa y las rotaciones son mayores a 0 se lo rota (lo de las rotaciones mayores a 0 e sporqie 0%26 == 0 y sino rota cuando empieza el programa)
                    self.rotor_b.rotate(1)
                aux2 = self.rotor_b.rotor_alphabet[(self.search_index_by_letter(aux, normal_aphabet)+ 26-self.rotor_c.rotations%26)%26]    
                #print(aux2)
                #tercer Rotor (rotor 1)
                if self.rotor_b.rotations %26 == 0 and self.rotor_b.rotations > 0:        #misma logica que con el rotor 1 pero con el rotor 4
                    self.rotor_a.rotate(1)
                aux4 = self.rotor_a.rotor_alphabet[(self.search_index_by_letter(aux2, normal_aphabet) + 26-self.rotor_b.rotations%26)%26]  #aca ya empieza el chino basico jsajaj
                #print(aux4)
                #Reflector B
                aux5 = normal_aphabet[(self.search_index_by_letter(aux4, normal_aphabet) + self.reflector.rotor_alphabet[self.search_index_by_letter(aux4,normal_aphabet)])%26]
                #print(aux5)
                #tercer rotor 2da vez
                aux6 = normal_aphabet[(self.search_index_by_letter(aux5, self.rotor_a.rotor_alphabet)+self.rotor_b.rotations)%26]   #el %26 va al final porque si el rotor 4 ya roto 25 veces se va el index out of range, al hacer el resto siempre me va a quedar dentro del index
                #print(aux6)
                #segundo rotor 2da vez
                aux7 = normal_aphabet[(self.search_index_by_letter(aux6, self.rotor_b.rotor_alphabet)+self.rotor_c.rotations)%26]
                #print(aux7)
                #primer rotor ulima vez
                coded_phrase += normal_aphabet[self.search_index_by_letter(aux7, self.rotor_c.rotor_alphabet)]
                #print(coded_phrase)
        print("-"*50)
        print("Frase codificada: ")
        print(coded_phrase)
        return coded_phrase
        print("-"*50)

#f = Enigma(Rotor_1, Rotor_4, Rotor_5, Reflector_B)
#f.enigma_functioning("una frase larga como esta deberia cifrarse correctamente".lower())

def Program():
    program_enimga = Enigma(Rotor_1, Rotor_4, Rotor_5, Reflector_B)
    print("-"*50)
    option = "C"
    while option.upper() == "C" or option.upper() == "D":
        print("-"*50)
        print("¡Bienvenido al programa de Maquina Enigma I!")
        print("Ingrese la letra C para cifrar una frase")
        print("Ingrese la letra D para decifrar una frase")
        print("Ingrese cualquier otra la letra para salir")
        option = input("Ingrese una opcion C/D/Salir: ")
        if option.upper() == "C":
            program_enimga.rotor_a.rotate(26 - program_enimga.rotor_a.rotations%26)
            program_enimga.rotor_a.rotations = 0
            program_enimga.rotor_b.rotate(26 - program_enimga.rotor_b.rotations%26)
            program_enimga.rotor_b.rotations = 0
            program_enimga.rotor_c.rotate(26 - program_enimga.rotor_c.rotations%26)
            program_enimga.rotor_c.rotations = 0
            print("-"*50)
            program_enimga.rotor_a.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor I: ").lower(), normal_aphabet))
            program_enimga.rotor_b.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor IV: ").lower(), normal_aphabet))
            program_enimga.rotor_c.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor V: ").lower(), normal_aphabet))

            x = program_enimga.enigma_functioning(input("Ingrese la frase a cifrar: ").lower())
            print("-"*50)
            if input("si desea desencriptar la frase ingrese 1: ") == "1":
                program_enimga.rotor_a.rotate(26 - program_enimga.rotor_a.rotations%26)
                program_enimga.rotor_a.rotations = 0
                program_enimga.rotor_b.rotate(26 - program_enimga.rotor_b.rotations%26)
                program_enimga.rotor_b.rotations = 0
                program_enimga.rotor_c.rotate(26 - program_enimga.rotor_c.rotations%26)
                program_enimga.rotor_c.rotations = 0
                print("-"*50)
                program_enimga.rotor_a.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor I: ").lower(), normal_aphabet))
                program_enimga.rotor_b.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor IV: ").lower(), normal_aphabet))
                program_enimga.rotor_c.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor V: ").lower(), normal_aphabet))
                
                program_enimga.enigma_functioning(x)
        elif option.upper() == "D":
            program_enimga.rotor_a.rotate(26 - program_enimga.rotor_a.rotations%26)
            program_enimga.rotor_a.rotations = 0
            program_enimga.rotor_b.rotate(26 - program_enimga.rotor_b.rotations%26)
            program_enimga.rotor_b.rotations = 0
            program_enimga.rotor_c.rotate(26 - program_enimga.rotor_c.rotations%26)
            program_enimga.rotor_c.rotations = 0
            print("-"*50)
            program_enimga.rotor_a.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor I: ").lower(), normal_aphabet))
            program_enimga.rotor_b.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor IV: ").lower(), normal_aphabet))
            program_enimga.rotor_c.rotate(program_enimga.search_index_by_letter(input("Ingrese la posición Inicial del Rotor V: ").lower(), normal_aphabet))

            program_enimga.enigma_functioning(input("Ingrese la frase a cifrar: ").lower())
Program()
