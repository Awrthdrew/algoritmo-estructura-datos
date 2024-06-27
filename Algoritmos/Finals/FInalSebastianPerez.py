class Client:
    def __init__(self, i, n):
        self.id = i
        self.name = n
        self.left = None
        self.right = None


raiz = Client(1, "Juan")
raiz.left = Client(2, "Maria")
raiz.left.left = Client(9, "Norma")
raiz.left.left.left = Client(8, "Silviana")
raiz.left.right = Client(5, "Karina")
raiz.right = Client(6, "Diego")
raiz.right.left = Client(4, "Ivana")
raiz.right.right = Client(3, "Carlos")
raiz.right.right.right = Client(7, "Ariel")

array_objetos = []

def Inorder(n):

    if n.left:
        Inorder(n.left)

    print(n.name)
    array_objetos.append(n)

    if n.right:
        Inorder(n.right)
        

print("----------------------------------------------Punto 1. Listar los nombres en orden alfabetico descendente---------------------------------------------- ")
Inorder(raiz)


print("---------------------------------------------- Punto 2. Buscaddor de Nombre ---------------------------------------------- ")

r = None

def buscar_nombre(nodo, nombre):
    global r
    if nodo:
        r = buscar_nombre(nodo.left, nombre)
        r = buscar_nombre(nodo.right, nombre)
        if nodo.name == nombre:

            return nodo
    if r:
        return r
            




print(buscar_nombre(raiz, input("Ingrese nombre que desea buscar: ")))




print("---------------------------------------------- Punto 3. Ordenaciopn de Nombres ---------------------------------------------- ")
print("--" * 50 + "Antes" + "--" * 50)
for x in array_objetos:
    print(x.name + " Id: " + str(x.id))


def ordenar_burbuja(array_objetos):
    for i in range(len(array_objetos) - 1):

        for j in range(len(array_objetos)-i-1):
            if array_objetos[j].name > array_objetos[j + 1].name:
                aux = array_objetos[j]
                array_objetos[j] = array_objetos[j+1]
                array_objetos[j+1] = aux


ordenar_burbuja(array_objetos)

print("--" * 50 + "despues" + "--" * 50)
for x in array_objetos:
    print(x.name + " Id: " + str(x.id))