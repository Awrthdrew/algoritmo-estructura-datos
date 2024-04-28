class Rotor:
    def __init__(self, wiring):
        self.wiring = wiring
        self.offset = 0
    
    def rotate(self):
        self.offset = (self.offset + 1) % 26
    
    def encrypt_forward(self, letter):
        index = (ord(letter) - ord('A') + self.offset) % 26
        return self.wiring[index]
    
    def encrypt_backward(self, letter):
        index = (ord(letter) - ord('A') - self.offset) % 26
        return chr(index + ord('A'))


class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring
    
    def reflect(self, letter):
        index = ord(letter) - ord('A')
        return self.wiring[index]


class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector
    
    def rotate_rotors(self):
        for rotor in self.rotors:
            rotor.rotate()
    
    def encrypt(self, message):
        encrypted_message = ""
        for letter in message:
            if letter.isalpha():
                encrypted_letter = self.encrypt_letter(letter)
                encrypted_message += encrypted_letter
                self.rotate_rotors()
            else:
                encrypted_message += letter
        return encrypted_message
    
    def encrypt_letter(self, letter):
        for rotor in self.rotors:
            letter = rotor.encrypt_forward(letter)
            
        letter = self.reflector.reflect(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.encrypt_backward(letter)
        return letter


# Configuración de los rotores y reflector
rotor_I_wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_IV_wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor_V_wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
reflector_B_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotor_I = Rotor(rotor_I_wiring)
rotor_IV = Rotor(rotor_IV_wiring)
rotor_V = Rotor(rotor_V_wiring)
reflector_B = Reflector(reflector_B_wiring)

# Configuración de la máquina Enigma
enigma = EnigmaMachine([rotor_I, rotor_IV, rotor_V], reflector_B)

# Selección de cifrado o descifrado
opcion = input("Seleccione una opción:\n1. Cifrar palabra\n2. Descifrar palabra\n")
if opcion == "1":
    mensaje = input("Ingrese la palabra a cifrar: ").upper()
    mensaje_cifrado = enigma.encrypt(mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)
elif opcion == "2":
    mensaje = input("Ingrese la palabra a descifrar: ").upper()
    mensaje_descifrado = enigma.encrypt(mensaje)
    print("Mensaje descifrado:", mensaje_descifrado)
else:
    print("Opción inválida. Por favor, seleccione 1 o 2.")
