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

def search_client_by_name(node, name):
    if node is None:
        return None
    
    if node.name == name:
        return node
    
    # Buscar en el subárbol izquierdo
    left_result = search_client_by_name(node.left, name)
    if left_result is not None:
        return left_result
    
    # Buscar en el subárbol derecho
    right_result = search_client_by_name(node.right, name)
    if right_result is not None:
        return right_result
    
    # Si no se encontró el cliente en ninguno de los subárboles
    return None

# Ejemplo de búsqueda de cliente por nombre
nombre_buscado = input("Ingrese el nombre a buscar: ")
cliente_encontrado = search_client_by_name(raiz, nombre_buscado)
if cliente_encontrado is not None:
    print(f"Cliente encontrado: ID = {cliente_encontrado.id}, Nombre = {cliente_encontrado.name}")
else:
    print("Cliente no encontrado.")
