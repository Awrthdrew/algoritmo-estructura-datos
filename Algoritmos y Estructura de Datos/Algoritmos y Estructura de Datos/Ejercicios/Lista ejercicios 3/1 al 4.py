# Creamos la variable 'animales'
animales = "elefante jirafa león tigre oso mono cebra rinoceronte hipopótamo cocodrilo" #ejercicio 1
# Separamos los nombres de los animales en una lista
# lista_animales = animales[0:] #ejercicio 2
# print(lista_animales) #ejercicio 2
lista_animales = animales.split()
# Iteramos sobre la lista de animales y mostramos cada nombre en pantalla
for animal in lista_animales: #ejercicio 3
    print(animal[0] + animal[1:])
