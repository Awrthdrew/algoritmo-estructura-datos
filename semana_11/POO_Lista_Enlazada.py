"""print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")"""

class Letra:
    def __init__(self, letra):
        self.letra = letra
        self.siguiente_letra = None
    
raiz = Letra("A")

raiz.siguiente_letra = Letra("B")

raiz.siguiente_letra.siguiente_letra = Letra("C")

def mostrar_lista(x):
    while x != None:
        print(x.letra) 
        x = x.siguiente_letra
        
"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para sacar un elemento al final de la lista
3) Hacer una función para sacar un elemento al comienzo de la lista
4) Hacer una función para sacar un elemento en la posición x de la lista (reenlazar los objetos detrás)
5) Hacer una función para agregar un elemento más en la posición x de la lista   
"""
        
#1.0 Agregar elemento al final de la lista
def agregar_elemento_final(letra):
    global raiz
    otra_raiz = raiz
    while otra_raiz.siguiente_letra != None:
        otra_raiz = otra_raiz.siguiente_letra
    otra_raiz.siguiente_letra = Letra(letra)

#1.1 Agregar elemento al principio de la lista    
def agregar_elemento_principio(letra):
    global raiz
    otra_raiz = Letra(letra)
    otra_raiz.siguiente_letra = raiz
    raiz = otra_raiz
    
#2.0 Sacar elemento al final de la lista
def sacar_elemento_final():
    global raiz
    otra_raiz = raiz
    while otra_raiz.siguiente_letra.siguiente_letra != None:
        otra_raiz = otra_raiz.siguiente_letra
    else:
        otra_raiz.siguiente_letra = None
    
#2.1 Sacar elemento al principio de la lista
def sacar_elemento_principio():
    global raiz
    raiz = raiz.siguiente_letra

#3.0 Agregar elemento en la posición x de la lista
def agregar_elemento_posicion(letra, posicion):
    global raiz
    r = raiz
    elemento = Letra(letra)
    
    if posicion == 0:
        elemento.siguiente_letra = raiz
        raiz = elemento
    else:
        for letra in range(posicion-1):
            r = r.siguiente_letra
        elemento.siguiente_letra = r.siguiente_letra
        r.siguiente_letra = elemento

#3.1 Sacar elemento en la posición x de la lista
def sacar_elemento_posicion(posicion):
    global raiz
    aux = raiz
    
    if posicion == 0:
        raiz = raiz.siguiente_letra
    else:
        for _ in range(posicion-1):
            aux = aux.siguiente_letra
        aux.siguiente_letra = aux.siguiente_letra.siguiente_letra

#------------------------------------------------------------
#Pruebas de las funciones de la lista enlazada con POO
#mostrar_lista(raiz)

#print()

#agregar_elemento_final("Joaquinchin")
#agregar_elemento_principio("Tote")
#sacar_elemento_final()
#sacar_elemento_principio()    
#agregar_elemento_posicion("Bayern Leverkusen", 4)
#sacar_elemento_posicion(1)

#mostrar_lista(raiz)

#------------------------------------------------------------

