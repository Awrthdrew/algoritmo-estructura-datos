def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
print('Original: ')
print(data)
insertion_sort(data)
print('Ordenado: ')
print(data)

class autos:
    def __init__(self, nombre, patente):
        self.nombre = nombre
        self.patente = patente
class motos:
    def __init__(self, nombre, patente):
        self.nombre = nombre
        self.patente = patente

Toyota = autos("SupraMK4", 334)
Yamaha = motos("Tz250", 455)
Honda = autos("NSX", 122)
KTM = motos("Duke290", 334)
Nissan = autos("SilviaS15", 123)

autosmotos = [Toyota, Yamaha, Honda, KTM, Nissan]


"""

"""



def insertion_sort(autosmotos):

    for step in range(1, len(autosmotos)):
        key = autosmotos[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key.nombre < autosmotos[j].nombre:
            autosmotos[j + 1] = autosmotos[j]
            j = j - 1
            print(autosmotos[j + 1].nombre)
            print(autosmotos[j].nombre)
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        autosmotos[j + 1] = key


insertion_sort(autosmotos)


for x in autosmotos:
    print(str(x.nombre) + " Patente: " + str(x.patente))

