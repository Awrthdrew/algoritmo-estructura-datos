"""a = ["uno", "dos"]
print(id(a))

b = a
x = a.copy()

print(id(b))   

a[0] = "tres"
print(b)

print(id(x))

print(x)"""


"""import copy

x = [[1, 2, 3], ['Andrew', 'Joaco', 'Puerro', 'Uribe'], True]
y = x.copy()
z = copy.deepcopy(x)

print(x)

print(y)

print(z)"""

"""g, *h, i = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(g, h, i)"""

"""
if (nombre := input("Introduzca su nombre: ")) == "Juan":
    print("Hola Juan!")
else:
    print("Hola", nombre)
"""


"""def funcion(*args, **kwargs):
    print(f'Argumentos simples: {args} - Argumentos k-v {kwargs}')
    
funcion()

funcion(69)

funcion(marca='Peugeot')

funcion(13, 'algo', modelo='408')"""

