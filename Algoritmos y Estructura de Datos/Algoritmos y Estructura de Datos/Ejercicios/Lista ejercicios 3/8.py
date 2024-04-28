lista1 = [2, 3, 4, 5] #usando insert()
lista1.insert(0, 1) #lista.insert(posicion, elemento)
print("Lista 1, usando insert(): ", lista1)

lista2 = [2, 3, 4, 5] #usando [] y +
lista2 = [1] + lista2 #lista = [elemento] + lista
print("Lista 2, usando [] y +: ", lista2)

lista3 = [2, 3, 4, 5] #usando Slicing 
lista3[:0] = [1] #lista[:0] = [elemento que se agrega]
print("Lista 3, usando Slicing: ", lista3)

lista4 = [1, 2, 3, 4] #usando extend()
# extend() solo se puede usar para agregar elementos al final de la lista
lista4.extend([5])
print("Lista 4, usando extend(): ", lista4)
