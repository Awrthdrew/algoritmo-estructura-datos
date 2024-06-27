class Persona:
    def __init__(self, persona, edad):
        self.persona = persona
        self.edad = edad
    @property
    def getEdad(self):
        return self.edad
    @property
    def getPersona(self):
        return self.persona
    
    def __str__(self):
        return f"Persona: {self.persona}, Edad: {self.edad}"
    
#print(a.__getPersona__)

a = Persona("Gabi", 19)
b = Persona("Nico", 34)
c = Persona("Adriel", 84)
d = Persona("Seba", 12)
e = Persona("Lucas", 8)

ListaPersonas = [a, b, c, d, e]

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j].getEdad > lista[j+1].getEdad:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def printArrays(a):
    for x in range(len(a)):
        print(a[x])

print("-" * 25)
print("Antes: ")
printArrays(ListaPersonas)
ordenar_burbuja(ListaPersonas)
print("\n")
print("Después: ")
printArrays(ListaPersonas)
print("-" * 25)




"""
def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            #print("---")
            #print("i: " + str(i) + " - j: " + str(j) + " => " + str(lista))
            #print(str().rjust(j*3+16) + "-  -")
            if lista[j].getEdad > lista[j+1].getEdad:
                print("    Intercambiando: " + str(lista[j]) + " : " + str(lista[j+1]))
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                #lista[j], lista[j+1] = lista[j+1], lista[j]

def printArrays(a):
    for x in range(len(a)):
        print(a[x].getPersona + ", " + str(a[x].getEdad))

printArrays(ListaPersonas)
#print("Antes: " + str(lista))
ordenar_burbuja(ListaPersonas)
#ordenar(lista)
print("Despúes: " + str(ListaPersonas))
"""




























