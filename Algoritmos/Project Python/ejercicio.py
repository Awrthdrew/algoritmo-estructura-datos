"""
Ejercicios:
1) crear una clase Persona con los atributos nombre y edad
2) crear una lista y en la lista agregar 5 instancias de Persona diferentes
3) aplicar la ordenación a la lista
"""

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @property
    def get_edad(self):
        return self.edad
    
    
    
p = persona("francisco", 19)
q = persona("bernardo", 18)
z = persona("franchesco", 30)
h = persona("francisco", 32)
i = persona("jessie", 23)

array_personas = [p,q,z,h,i]

for i in range(len(array_personas)):
    print(array_personas[i].get_edad)


def ordenar_burbuja(array_personas):
    for i in range(len(array_personas)):
        print(i)
        for j in range(len(array_personas)-i-1):
            if array_personas[j].get_edad > array_personas[j + 1].get_edad:
                aux = array_personas[j]
                array_personas[j] = array_personas[j+1]
                array_personas[j+1] = aux
    
ordenar_burbuja(array_personas)

print("------------------------------------------------ Despues de Iteracion-----------------------------------------")

for i in range(len(array_personas)):
    print(array_personas[i].get_edad)




"""

class persona_sin:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    

    def get_edad(self):
        return self.edad
    




pl = persona("francisco", 19)
ql = persona("bernardo", 18)
zl = persona("franchesco", 30)
hl = persona("francisco", 32)
il = persona("jessie", 23)

array_personas = [pl,ql,zl,hl,il]

for i in array_personas:
    print(i.get_edad)


def ordenar_burbuja(array_personas):
    for i in range(len(array_personas)-1):
        for j in range(len(array_personas)-i-1):
            if array_personas[j].get_edad > array_personas[j + 1].get_edad:
                aux = array_personas[j]
                array_personas[j] = array_personas[j+1]
                array_personas[j+1] = aux
    
"""