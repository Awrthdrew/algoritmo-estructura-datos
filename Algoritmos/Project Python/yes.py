import random
x = 0
s = ".next_node"
l = "raiz"
# while x <= 13:
#     print("Mecha" + str(y) + " = " + "Mechas(" + str(x) + " , " + str(round(random.uniform(1,20), 2)) + ")")
#     x += 0.25
#     y += 1

while x <= 52:
    print(str(l) + " = " + "Node(" + "Mecha" + str(x) + ")")
    x += 1
    l += s