"""li =  [11, 3, 5]

li.append(44)

#li.remove(5) quita

#li.insert(1, 20) agregar elemento

li.pop()

print(li)"""


# Saca el último elemento de la lista y al insertarla en la posición 0, se reacomoda la lista.
"""p = [33, 22, 1]
tmp = p.pop()
print(tmp)
print(p)
p.insert(0, tmp)
print(p)"""

k = [23, 12, 78]

aux = k[0]
k[0] = k[1]
k[1] = aux

print(k)