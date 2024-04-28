# Arbol:
class Client:
	def __init__ (self, i, n):
		self.id = i
		self.name = n
		self.left = None
		self.right = None
raiz = Client(1, "Juan")
raiz.left = Client(2, "Maria")
raiz.left.left = Client(9, "Norma")
raiz.left.left.left = Client(8, "Silvina")
raiz.left.right = Client(5, "Karina")
raiz.right = Client(6, "Diego")
raiz.right.left = Client(4, "Ivana")
raiz.right.right = Client(3, "Carlos")
raiz.right.right.right = Client(7, "Ariel")

# 1) desarrolla una funcion recursiva que recorra el arbol e imprima los nombres en orden alfabetico descendente.
# Nota: no usar metodos de ordenacion ni modificar el arbol.

print("1) Nombres en orden alfabético descendente:")

def imprimir_nombres_descendente(nodo):
    if nodo is None:
        return
    imprimir_nombres_descendente(nodo.left)
    print(nodo.name)
    imprimir_nombres_descendente(nodo.right)

imprimir_nombres_descendente(raiz)
print("")
# 2) Con el mismo arbol BTREE de la base de datos del campo "nombre"
# desarrolla una funcion que reciba por parametro el string que sera el nombre a buscar en el arbol.
# Si existe, que devuelva dicho objeto "Cliente" sino un None.
def search_client_by_name(node, name):
    if node is None:
        return None
    
    if node.name == name:
        return node
    
    left_result = search_client_by_name(node.left, name)
    if left_result is not None:
        return left_result
    
    right_result = search_client_by_name(node.right, name)
    if right_result is not None:
        return right_result   
    return None

nombre_buscado = input("2) Ingrese el nombre a buscar (con la primera letra en mayuscula): ")
cliente_encontrado = search_client_by_name(raiz, nombre_buscado)
if cliente_encontrado is not None:
    print(f"Cliente encontrado: ID = {cliente_encontrado.id}, Nombre = {cliente_encontrado.name}")
else:
    print("Cliente no encontrado.")
print("")

# 3) Utilizando la informacion de la tabla, pasarla a una lista de python y desarrollar una funcion que la ordene por nombre ascendente utilizando el metodo de burbuja.
# mostrar el nombre y su correspondiente id luego de ordenar.
tabla = [
    (1, "Juan"),
    (2, "Maria"),
    (3, "Carlos"),
    (4, "Ivana"),
    (5, "Karina"),
    (6, "Diego"),
    (7, "Ariel"),
    (8, "Silvana"),
    (9, "Norma")
]

def ordenar_por_nombre(lista):
    n = len(lista)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

ordenar_por_nombre(tabla)
print("3) Ordenacion ascendente por nombre: ")

for cliente in tabla:
    print("Nombre:", cliente[1], "- ID:", cliente[0])
