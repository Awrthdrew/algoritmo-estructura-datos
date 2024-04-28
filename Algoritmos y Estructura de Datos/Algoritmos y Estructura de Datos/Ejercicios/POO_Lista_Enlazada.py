print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")

class Letra:
    siguiente_letra = None
    def __init__(self, letra):
        self.letra = letra
    
raiz = Letra("A")

def mostrar_lista(x):
    while x != None:
        print(x.letra)
        x = x.siguiente_letra

def agregar_fin(x):
    global raiz
    i = raiz
    while i.siguiente_letra != None:
        i = i.siguiente_letra
    i.siguiente_letra = Letra(x)

#agregar_fin("B")
#agregar_fin("C")
#agregar_fin("D")

def agregar_comienzo(x):
    global raiz
    nuevo_nodo = Letra(x)
    while j.siguiente_letra == Letra(raiz):
        

agregar_comienzo("Z")
mostrar_lista(raiz)
   
    
"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para sacar un elemento al final de la lista
3) Hacer una función para sacar un elemento al comienzo de la lista
4) Hacer una función para sacar un elemento en la posición x de la lista
   (reenlazar los objetos detrás)
5) Hacer una función para agregar un elemento más en la posición x de la lista   
"""
