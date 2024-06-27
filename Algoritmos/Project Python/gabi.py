class Node:
    valor = ""
    subnodes = None
    def __init__(self, valor, numero):
        self.valor = valor
        self.numero = numero
        self.subnodes = []
        
#https://es.wikipedia.org/wiki/Taxonom%C3%ADa#/media/Archivo:Taxonomia-y-filogenia.gif
raiz = Node("Transporte", 3)
raiz.subnodes.append(Node("Automotor", 2))
raiz.subnodes.append(Node("Ciclomotor", 1))
raiz.subnodes.append(Node("Bicicleta", 4))
raiz.subnodes.append(Node("Cuadrupedo", 7))

raiz.subnodes[0].subnodes.append(Node("Terrestre", 1))
raiz.subnodes[0].subnodes.append(Node("Aereo", 7))
raiz.subnodes[0].subnodes.append(Node("Matitimo", 9))

raiz.subnodes[0].subnodes[0].subnodes.append(Node("Autos", 7))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Tren", 3))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Colectivos", 5))

raiz.subnodes[3].subnodes.append(Node("Caballo", 6))
raiz.subnodes[3].subnodes.append(Node("Camello", 4))
raiz.subnodes[3].subnodes.append(Node("Mula", 9))


def recorrer(r, sangria = ""):
    print(sangria + r.valor + "\n")
    sangria += "  "  
    for i in r.subnodes:
        recorrer(i, sangria)
    
recorrer(raiz)

# def recorrer_nivel_especifico(r, v, e = 0):
#     if v <1:
#         print("Nivel 0 no eixiste maestro")
#         return
#     nivel_actual = e
#     nivel_actual_nodos = [r]

#     if nivel_actual == v:
#         for nodo in nivel_actual_nodos:
#             print(nodo.valor)
#     for i in r.subnodes:
#         recorrer_nivel_especifico(i, v, e + 1)
    #print(r.subnodes[v].valor)

# array_nodos = []
# def recorrer_todos_niveles(r, e = 0):
#     nivel_actual = e
#     nivel_actual_nodos = [r]

#     for nodo in nivel_actual_nodos:
#         array_nodos.append("Nivel " + str(e))
#         array_nodos.append(nodo.valor)
#     for i in r.subnodes:
#         recorrer_todos_niveles(i, e + 1)
#     #print(r.subnodes[v].valor)

# recorrer_todos_niveles(raiz)


# for x in array_nodos:
#     print(x)