print("Ejemplo básico de Programación Orientada a Objetos en Python")
print("---")

class Animal:

    #CONSTRUCTOR
    #método especial que se ejecuando cuando se instancia la clase
    def __init__(self, name):
        #asignar atributo
        self.name = name #atributo público
        self.__age = 0 #atributo privado
        

    @staticmethod
    def autor():
        return "Autores: Curso de AyED - FACEA - UAP"
        
    #atributo de clase: es compartido entre todas las instancias
    locomocion = "Acuática" 
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, x):
        if (x > 0 and x <= 500):
            self.__age = x
            print(perro.__age)
        
#Uso de un método estático, no hace falta instanciar la clase
print(Animal.autor())

#Instancias

perro = Animal("Rocko")
gato = Animal("Michifuz")

print("Nombres:")
perro.name = "Rocko"
perro.age = 55 #property read-only unless setter
print(perro.name)
print(gato.name)

# No se va a poder printear porque trata de acceder a un atributo privado de una clase. Para hacerlo, se debe usar un método de la clase. Osea, dentro del n° 25(29).
#print(perro.__age)

print("Locomoción")
print(perro.locomocion)
print(gato.locomocion)
Animal.locomocion = "Terrestre"
print(perro.locomocion)
print(gato.locomocion)





