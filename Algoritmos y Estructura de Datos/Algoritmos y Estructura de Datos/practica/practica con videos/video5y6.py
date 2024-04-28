# Programacion Orientada a Objetos (POO)
# las clases y tienen atributos y metodos. 
# y en base a esto se crean los objetos, dandole valores a sus atributos
# esto se llama instanciar, y se hace con un constructor __init__(atributos)

# Pilares de la POO:
# Abstraccion: se eligen los atributos y métodos que tendrá una clase.
# Encapsulacion: controlar el acceso a atributos y métodos.

    ##pass # dentro de la clase sirve para no hacer nada

# Crear objeto: Personaje
# Clase: class nombreDeLaClase:
class Personaje:
# atributos
    ##nombre = "Default"
    ##fuerza = 0
    ##inteligencia= 0
    ##defensa = 0
    ##vida = 0
# Metodos:
    # darle valores a los atributos con un metodo constructor que reciba sus valores
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    # self.: arbumento que hace referencia a si mismo
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        # se pueden crear atributos en base a otros
        ##self.aguante = fuerza*vida # en este caso = 10*100
        # sepuedencrear atributos queno dependan de otros
        ##self.turno = False # indica si es su turno o no (boolean)
# haciendo esto no es necesario declararlos al principio de la clase
    
    # metodo que muestre el valor de sus atributos
    def atributos(self):# solo necesita el self para tener acceso a los atributos
        print(self.nombre, ":", sep="")
        print("> Fuerza:", self.fuerza)
        print("> Inteligencia:", self.inteligencia)
        print("> Defensa:", self.defensa)
        print("> Vida:", self.vida)

    # modificar algunos atributos
    def subir_nivel(self, fuerza, inteligencia, defensa):
        # se suma el valor actual con su incremento
        self.fuerza = self.fuerza + fuerza 
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    # metodo que devuelva un valor boolean que indique si el personaje esta vivo o no
    def esta_vivo(self):
        # se comprueba si la vida es mayor que cero o no con True o False
        return self.vida > 0
    
    # metodo matar al personaje y qe lo diga
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # acceder y/o modificar atributos
    # get_: develve el atribto (accede)
    def get_fuerza(self):
        return self.fuerza
    
    # set_: recibe uno nuevo para cambiarlo por el actual (modifica)
    def set_fuerza(self, fuerza):
        # si el valor es negativo, no se moifica e imprime un msj
        if fuerza < 0:
            print("Error, has introucido un valor negativo")
        # pero si el valor es positivo, si lo cambia y no muestra ningun msj
        else:
            self.fuerza = fuerza

# variable = nombreDeLaClase(argumentos) o () para uno vacio
mi_personaje = Personaje("Ezequiel", 10, 1, 5, 100)
# modificar los atributos
##mi_personaje.nombre = "Ezequiel"
##mi_personaje.fuerza = 10

# muestra la fuerza del personaje
print(mi_personaje.get_fuerza())

# modifica la fuerza del personaje
mi_personaje.set_fuerza(-5)
mi_personaje.atributos()

# quita la vida al personaje y lo muestra
mi_personaje.morir()
mi_personaje.atributos()

# se imprime si el personaje esta vivo o no (True o False)
print(mi_personaje.esta_vivo()) # si la vida = numero negativo, el resultado tambien es False

# se imprimen los atributos sin modificar
mi_personaje.atributos()

# se asigna la cantidad que se quiere sumar a a los atributos originales
mi_personaje.subir_nivel(1, 2, 0)
# se imprimen los nuevos atribtos asignados
mi_personaje.atributos()


# consultar cada uno de los atributos
##print("El nombre del jugador es", mi_personaje.nombre)
##print("La fuerza del jugador es", mi_personaje.fuerza)
##print("El aguante del jugador es", mi_personaje.aguante)

# Herencia
class Guerrero(Personaje): # class nombreSubClase(nombreClasePadre):
    # sobreescribir el metodo __init__ heredado de personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # hay dos formas de inicializar los atributos heredados:
        ##Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) # permite inicializar los atributos usando solo super()
        self.espada = espada
        
    # metodo que seleccione un arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acha, daño 8. (2) Arco, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de armas incorrecto.")

# se crea un gerrero asignandole valores a los atributos heredados
guts = Guerrero("Guts", 20, 10, 10, 100, 5)
guts.cambiar_arma()
guts.atributos()
print(guts.espada)