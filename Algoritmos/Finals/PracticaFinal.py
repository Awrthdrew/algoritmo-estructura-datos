# import random

# class Mechas:
    
#     def __init__(self, d, p):
#         self.diametro = d
#         self.precio = p

#     def get_radio(self):
#         return self.diametro / 2
    





# x = 1
# y = 0
# array_mechas = []
# while x <= 13:
#     y += 1
#     Mecha = Mechas(x, round(random.uniform(1,20), 2))
#     array_mechas.append(Mecha)
#     x += 0.25


# print("--"* 50 + "Antes" + "--" * 50)
# for x in array_mechas:
#     print(x.diametro)

# def insertion_sort(array_mechas):
#     for step in range(1, len(array_mechas)):
#         key = array_mechas[step]
#         j = step - 1
              
#         #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
#         #hasta encontrar un valor menor a este
#         while j >= 0 and key.precio < array_mechas[j].precio:
#             array_mechas[j + 1] = array_mechas[j]
#             j = j - 1
#             # print(array_comida[j + 1].nombre)
#             # print(array_comida[j].nombre)
        
#         # Ubicar el valor rescatado justo por delante del valor menor a este
#         array_mechas[j + 1] = key
# insertion_sort(array_mechas)
# print("--"* 50 + "despues" + "--" * 50)
# for x in array_mechas:
#     print(x.precio)

# suma_distancia = 0
# test = 0
# def calculo_distanica(array_mechas, suma_distancia, test):
#     y = 0
#     x = 0
#     while x < len(array_mechas) - 1:
#         y = 0
#         y = (array_mechas[x].get_radio()) + 1 + (array_mechas[x + 1].get_radio())
#         print("La distancia entre la mecha: " + str(x) + " y la mecha: " + str(x + 1) + " es de: " + str(y))
#         suma_distancia += array_mechas[x].diametro + 1
#         if x == 0:
#             test += array_mechas[x].diametro / 2
#         elif x == len(array_mechas) - 1:
#             test += array_mechas[x + 1].diametro / 2
#         test += y
#         x += 1
#     suma_distancia -= 1

#     print("La distancia total del contenedor sea de: " + str(suma_distancia))
#     print("La distancia total del contenedor sea de: " + str(test))


# def precio(array_mechas):
#     precio_max = 0
#     precio_min = 1000
#     promedio = 0
#     for x in array_mechas:
#         if precio_max < x.precio:
#             precio_max = x.precio
    
#     for x in array_mechas:
#         if precio_min > x.precio:
#             precio_min = x.precio
#     for x in array_mechas:
#         promedio += x.precio
#     promedio /= len(array_mechas)

#     print("El precio minimo es de: " + str(precio_min))
#     print("El precio maximo es de: " + str(precio_max))
#     print("El precio promedio es de: " + str(round(promedio, 2)))

# calculo_distanica(array_mechas, suma_distancia, test)
# precio(array_mechas)



# def insertion_sort_tamano(array_mechas):
#     for step in range(1, len(array_mechas)):
#         key = array_mechas[step]
#         j = step - 1
              
#         #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
#         #hasta encontrar un valor menor a este
#         while j >= 0 and key.diametro < array_mechas[j].diametro:
#             array_mechas[j + 1] = array_mechas[j]
#             j = j - 1
#             # print(array_comida[j + 1].nombre)
#             # print(array_comida[j].nombre)
        
#         # Ubicar el valor rescatado justo por delante del valor menor a este
#         array_mechas[j + 1] = key

# insertion_sort_tamano(array_mechas)

# def calculo_distanica_centro(array_mechas, suma_distancia, test):
#     y = 0
#     x = 0
#     while x < len(array_mechas) - 1:
#         if x == 0:
#             y += (array_mechas[x].get_radio() * 0.1) + 1
#             print("La desyancia entre el centro de la mecha: " + str(x) + " Es de " + str(y)) 
#         else:
#             y += (array_mechas[x].get_radio() * 0.1) + 1
#             print("La desyancia entre el centro de la mecha: " + str(x) + " Es de " + str(y))
#             suma_distancia += array_mechas[x].diametro + 1
#         if x == 0:
#             test += array_mechas[x].diametro / 2
#         elif x == len(array_mechas) - 1:
#             test += array_mechas[x + 1].diametro / 2
#         test += y
#         x += 1
#     suma_distancia -= 1

#     print("La distancia total del contenedor sea de: " + str(suma_distancia))
#     print("La distancia total del contenedor sea de: " + str(test))


# calculo_distanica_centro(array_mechas, suma_distancia, test)

# class Node:
#     def __init__(self, x):
#         self.objeto = x
#         self.next_node = None

#     def __str__(self):
#         return self.objeto
    

#---------------------------------------------------Abraham--------------------------------------------------------------



class Node:
    Esposa = None
    hijos = None
    Madre = ""
    def __init__(self, Nombre):
        self.Nombre = Nombre
        self.Esposa = []
        self.hijos = []
    



raiz = Node("Abraham")
raiz.Esposa.append(Node("Agar"))
raiz.Esposa[0].hijos.append(Node("Ismael"))

raiz.Esposa.append(Node("Sara"))
raiz.Esposa[1].hijos.append(Node("Isaac"))
raiz.Esposa[1].hijos[0].Esposa.append(Node("Rebeca"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos.append(Node("Esaú"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos.append(Node("Jacob"))

raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa.append(Node("Lea"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[0].hijos.append(Node("Rubén"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[0].hijos.append(Node("Simeón"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[0].hijos.append(Node("Leví"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[0].hijos.append(Node("Juda"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[0].hijos.append(Node("Isacar"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[0].hijos.append(Node("Zabulón"))

raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa.append(Node("Zilpha"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[1].hijos.append(Node("Gad"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[1].hijos.append(Node("Aser"))

raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa.append(Node("Raquel"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[2].hijos.append(Node("Jose"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[2].hijos.append(Node("Benjamín"))

raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa.append(Node("Bilha"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[3].hijos.append(Node("Dan"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[3].hijos.append(Node("Neftalí"))

raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[2].hijos[0].Esposa.append(Node("Asenat"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[2].hijos[0].Esposa[0].hijos.append(Node("Manasés"))
raiz.Esposa[1].hijos[0].Esposa[0].hijos[1].Esposa[2].hijos[0].Esposa[0].hijos.append(Node("Efraín"))

array_prueba = []
sangria = ""


array_nombres = []

def mostrar_arbol(raiz, sangria):
    if raiz is None:
        return
    print(sangria + raiz.Nombre)
    array_nombres.append(raiz)
    for hijo in raiz.Esposa:
        mostrar_arbol(hijo, sangria + "")
    for hijo in raiz.hijos:
        mostrar_arbol(hijo, sangria + " ")
        
print("--" * 25 + "ÁRBOL GENEALÓGICO" + "--" * 25)
mostrar_arbol(raiz, "")
  
def ordenar_burbuja(array_nombres):
    for x in range(len(array_nombres) - 1):
        for y in range(len(array_nombres) - x - 1):
            if array_nombres[y].Nombre > array_nombres[y + 1].Nombre:
                aux = array_nombres[y]
                array_nombres[y] = array_nombres[y + 1]
                array_nombres[y + 1] = aux


ordenar_burbuja(array_nombres)
print("--" * 25 + "Ordenado" + "--" * 25)
letra = ""
for x in array_nombres:
    if x.Nombre[0] != letra:
        letra = x.Nombre[0]
        print("\n" + letra + ": ", end="")
    print(x.Nombre, end=", ")

    

