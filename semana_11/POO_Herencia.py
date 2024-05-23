print("Ejemplo básico de Herencia POO en Python")
print("---")

class Animal:

    #método especial que se ejecuando cuando se instancia la clase
    def __init__(self, name):
        #asignar atributo
        self.name = name
#-------------------------------------------------------------------------------        
class Gato(Animal):
    def __init__(self, name):
        super(Gato, self).__init__(name)
    
    def maullar(self):
        return "Dejame entrar a la habenicht houseeee"
#-------------------------------------------------------------------------------        
class Perro(Animal):
    def ladrar(self):
        return "Guauu"
        
g = Gato("Misky")

print(g.name)
print(g.maullar())

p = Perro("Bolt")
print(p.name)
print(p.ladrar())
