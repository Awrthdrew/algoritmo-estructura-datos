def lineal_search(arr, x):
    steps = 0
    i = 0
    while i < len(arr):
        steps += 1
        if arr[i] == x:
            print("Encontrado en " + str(steps) + " iteraciones")
            return i
        i += 1
    return -1
            

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    steps = 0
 
    while low <= high:
        steps += 1
        mid = (high + low) // 2
 
        # Si x es mayor ignoro la mitad izquierda
        if arr[mid] < x:
            low = mid + 1
 
        # Si x es menor ignoro la mitad derecha
        elif arr[mid] > x:
            high = mid - 1
 
        # Si no es mayor ni menor lo encontré
        else:
            print("Encontrado en " + str(steps) + " iteraciones")
            return mid
 
    #si alcanzamos este punto y no salió por el return anterior es que no existe
    #el elemento que buscamos en el array
    return -1
 
 
# Test array
#arr = [ 2, 40 ]
#arr = [ 2, 3, 4, 10, 40 ]
#arr = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 40 ]
#arr = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40 ]
arr = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 40 ]
x = 40
 
# Function call
result = lineal_search(arr, x)
#result = binary_search(arr, x)
if result != -1:
    print("Encontrado en: " + str(result))
else:
    print("Valor no encontrado!")
