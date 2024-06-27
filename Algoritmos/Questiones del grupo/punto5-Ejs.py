class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        self.parent = None

def es_nodo_interno(nodo):
    return nodo.left is not None or nodo.right is not None

def grado(nodo):
    count = 0
    if nodo.left is not None:
        count += 1
    if nodo.right is not None:
        count += 1
    return count

def nivel(nodo):
    level = 0
    current = nodo
    while current.parent is not None:
        level += 1
        current = current.parent
    return level + 1

def altura_nodo(nodo):
    if nodo is None:
        return -1
    left_height = altura_nodo(nodo.left)
    right_height = altura_nodo(nodo.right)
    return max(left_height, right_height) + 1

def altura_arbol(raiz):
    return altura_nodo(raiz)

def profundidad(nodo):
    depth = 0
    current = nodo
    while current.parent is not None:
        depth += 1
        current = current.parent
    return depth

def rama(inicio, final):
    path = []
    current = inicio
    while current != final:
        path.append(current.valor)
        current = current.parent
    path.append(final.valor)
    return ' -> '.join(path)

# Crear el árbol según el ejemplo dado
raiz = Node("a")
raiz.left = Node("b")
raiz.left.parent = raiz
raiz.left.right = Node("d")
raiz.left.right.parent = raiz.left
raiz.left.right.left = Node("g")
raiz.left.right.left.parent = raiz.left.right
raiz.left.right.right = Node("h")
raiz.left.right.right.parent = raiz.left.right
raiz.left.right.right.left = Node("j")
raiz.left.right.right.left.parent = raiz.left.right.right

raiz.right = Node("c")
raiz.right.parent = raiz
raiz.right.left = Node("e")
raiz.right.left.parent = raiz.right
raiz.right.left.left = Node("i")
raiz.right.left.left.parent = raiz.right.left
raiz.right.left.left.left = Node("k")
raiz.right.left.left.left.parent = raiz.right.left.left
raiz.right.right = Node("f")
raiz.right.right.parent = raiz.right

print("Nodo interno:", es_nodo_interno(raiz))  # True
print("Grado:", grado(raiz))  # 2
print("Nivel:", nivel(raiz))  # 1
print("Altura del nodo 'h':", altura_nodo(raiz.left.right.right))  # 2
print("Altura del árbol:", altura_arbol(raiz))  # 3
print("Profundidad del nodo 'k':", profundidad(raiz.right.left.left.left))  # 4
print("Rama desde 'j' a 'k':", rama(raiz.left.right.right.left, raiz.right.left.left.left))  # j -> h -> d -> b -> c -> e -> i -> k


