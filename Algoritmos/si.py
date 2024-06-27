# class pizzas:
#     def __init__(self, t, c, co, p, nombre):
#         self.tiempo = t
#         self.costo = c
#         self.complejidad = co
#         self.porciones = p
#         self.nombre = nombre

#     def sacar_promedio(self):
#         return self.costo / self.porciones

# class Guiso_Lentejas:
#     def __init__(self, t, c, co, p, nombre):
#         self.tiempo = t
#         self.costo = c
#         self.complejidad = co
#         self.porciones = p
#         self.nombre = nombre

#     def sacar_promedio(self):
#         return self.costo / self.porciones

# class Empanadas:
#     def __init__(self, t, c, co, p, nombre):
#         self.tiempo = t
#         self.costo = c
#         self.complejidad = co
#         self.porciones = p
#         self.nombre = nombre
    
#     def sacar_promedio(self):
#         return self.costo / self.porciones

# class Milanesas_con_Pure:
        
#     def __init__(self, t, c, co, p, nombre):
#         self.tiempo = t
#         self.costo = c
#         self.complejidad = co
#         self.porciones = p
#         self.nombre = nombre        
        
#     def sacar_promedio(self):
#         return self.costo / self.porciones


# pizza = pizzas(30, 500, "media", 4, "Pizza")
# Guiso = Guiso_Lentejas(120, 900, "alta", 6, "Guiso")
# empanadas = Empanadas(60, 740, "media", 4, "Empanadas")
# Milas = Milanesas_con_Pure(30, 800, "baja", 4, "Milas")


# array_comida = [Guiso, pizza, empanadas, Milas]


# def insertion_sort(array_comida):
#     for step in range(1, len(array_comida)):
#         key = array_comida[step]
#         j = step - 1
              
#         #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
#         #hasta encontrar un valor menor a este
#         while j >= 0 and key.sacar_promedio() < array_comida[j].sacar_promedio():
#             array_comida[j + 1] = array_comida[j]
#             j = j - 1
#             # print(array_comida[j + 1].nombre)
#             # print(array_comida[j].nombre)
        
#         # Ubicar el valor rescatado justo por delante del valor menor a este
#         array_comida[j + 1] = key
# insertion_sort(array_comida)
# for x in array_comida:
#     print(x.nombre)

        

class Node:
    valor = ""
    subnodes = None
    def __init__(self, valor, numero):
        self.valor = valor
        self.numero = numero
        self.subnodes = []


Mundo = Node("Tierra", 100)

Mundo.subnodes.append(Node("Canada", 10)) 
Mundo.subnodes.append(Node("Argentina", 9)) 
Mundo.subnodes.append(Node("Chile", 6))

Mundo.subnodes[0].subnodes.append(Node("Northern", 8))
Mundo.subnodes[0].subnodes.append(Node("Southern", 10))
Mundo.subnodes[0].subnodes.append(Node("Western", 7))
Mundo.subnodes[0].subnodes.append(Node("Costal", 5))

Mundo.subnodes[0].subnodes[1].subnodes.append(Node("Edmonton", 10))
Mundo.subnodes[0].subnodes[1].subnodes.append(Node("Calgary", 9))
Mundo.subnodes[0].subnodes[1].subnodes.append(Node("Red-Deer", 7))



def recorrer(r, sangria = ""):
    print(sangria + r.valor + "\n")
    sangria += "  "    
    for i in r.subnodes:
        recorrer(i, sangria)
    

def recorrer_nivel_arbol(nodo, nivel_deseado, nivel_actual=0):
    if nivel_actual == nivel_deseado:
        print(nodo.valor)
    elif nivel_actual < nivel_deseado:
        for subnodo in nodo.subnodes:
            recorrer_nivel_arbol(subnodo, nivel_deseado, nivel_actual + 1)

def recorrer_nodo_especifico(nodo, valor_deseado):
    if nodo.valor == valor_deseado:
        print(nodo.valor)
        for x in nodo.subnodes:
            print(x.valor)
            recorrer_nodo_especifico(x, valor_deseado)

        # Realizar el recorrido a partir de este nodo, si es necesario
        # Puedes agregar aquí la lógica adicional para recorrer los subnodos
        
    for subnodo in nodo.subnodes:
        recorrer_nodo_especifico(subnodo, valor_deseado)

recorrer_nodo_especifico(Mundo, "Chile")