class Node:
    valor = ""
    subnodes = None
    dato_extra = 0
    
    def __init__(self, valor, d):
        self.valor = valor
        self.subnodes = []
        self.dato_extra = d

raiz1 = Node("Transporte", 10)

raiz1.subnodes.append(Node("Automotor", 4))
raiz1.subnodes.append(Node("Ciclomotor", 3))
raiz1.subnodes.append(Node("Bicicleta", 8))
raiz1.subnodes.append(Node("Cuadrúpedo", 12))

raiz1.subnodes[0].subnodes.append(Node("Terrestre", 4))
raiz1.subnodes[0].subnodes.append(Node("Aéreo", 6))
raiz1.subnodes[0].subnodes.append(Node("Marítimo", 8))

raiz1.subnodes[0].subnodes[0].subnodes.append(Node("Autos", 8))
raiz1.subnodes[0].subnodes[0].subnodes.append(Node("Tren", 9))
raiz1.subnodes[0].subnodes[0].subnodes.append(Node("Colectivos", 3))

raiz1.subnodes[3].subnodes.append(Node("Caballo", 8))
raiz1.subnodes[3].subnodes.append(Node("Camello", 3))
raiz1.subnodes[3].subnodes.append(Node("Mula", 3))

raiz1.subnodes[0].subnodes[0].subnodes[0].subnodes.append(Node("BMW", 2))
raiz1.subnodes[0].subnodes[0].subnodes[0].subnodes.append(Node("Toyota", 6))
raiz1.subnodes[0].subnodes[0].subnodes[0].subnodes.append(Node("Bugatti", 8))

raiz1.subnodes[0].subnodes[1].subnodes.append(Node("Avión", 4))
raiz1.subnodes[0].subnodes[1].subnodes.append(Node("Helicóptero", 1))
raiz1.subnodes[0].subnodes[1].subnodes.append(Node("Zeppelin", 9))
raiz1.subnodes[0].subnodes[1].subnodes.append(Node("Cohete", 3))
raiz1.subnodes[0].subnodes[1].subnodes.append(Node("Águila Gigante", 7))


def bubble_sort(node):
    if len(node.subnodes) > 1:
        for i in range(len(node.subnodes) - 1):
            for j in range(len(node.subnodes) - 1 - i):
                if node.subnodes[j].dato_extra > node.subnodes[j + 1].dato_extra:
                    node.subnodes[j], node.subnodes[j + 1] = node.subnodes[j + 1], node.subnodes[j]

            bubble_sort(node.subnodes[j])


def print_tree(node, depth=0):
    print(" " * depth + node.valor + " - " + str(node.dato_extra))
    for subnode in node.subnodes:
        print_tree(subnode, depth + 1)
    if depth == 2:
        print("--------------------")  # División entre niveles

print("Árbol original:")
print_tree(raiz1)

print("Árbol ordenado(bubble_sort):")
bubble_sort(raiz1)
print_tree(raiz1)
print("*"*100)

def insertion_sort(node):
    for i in range(1, len(node.subnodes)):
        insert_value = node.subnodes[i].dato_extra
        insert_index = i

        while insert_index > 0 and node.subnodes[insert_index - 1].dato_extra > insert_value:
            node.subnodes[insert_value].dato_extra = node.subnodes[insert_index - 1].dato_extra
            insert_index -= 1

            node.subnodes[insert_index].dato_extra = insert_value 



print("Árbol original:")
print_tree(raiz1)

print("Árbol ordenado(insertion_sort):")
insertion_sort(raiz1)
print_tree(raiz1)