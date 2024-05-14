array = [ 2, 8, 13, 19, 21, 26, 30, 37, 39, 40 ]

"""1. Dada una array de números enteros A[1...n] tal que, para todo i, 1 <= i <= n, tenemos  
|A[i]-A[i+1]| < 1. Con A[1]=x  y  A[n]=y, tal que x < y.  Diseñe un algoritmo de búsqueda eficiente para encontrar  j tal que A[j] = z  para un valor dado z, x<=z<=y.   
Cuál es el número máximo de comparaciones a z que realiza su algoritmo?"""

"""def binary_search(arr, x):
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
    return -1"""

"""2. Reciba como entrada un conjunto S de n números reales y un número real x. Diseñe un 
algoritmo para determinar si existen dos elementos en S, cuya soma es x.   
 * Suponga que S está ordenado,  El algoritmo debe rodar en un tiempo O (n)."""



# CORREGIRLO DESPUÉS
"""def ady_sum(num: int):
    for i in range(len(array)) :
        if num == i + (i + 1):
            print(i, " + ", i + 1," Hace la suma de: ", num)
        else:
            print("No se cumple la adyacencia!")
        break"""

"""3. Reciba como entrada un conjunto S de n números reales y un número real x.  
Diseñe un algoritmo para determinar si existen dos elementos en S, cuya soma es x.  
    Suponga que S está ordenado,  El algoritmo debe rodar en un tiempo máximo de O (n log n) """

def ady_sum(array, num):
    low = 0
    high = len(array) - 1
    
    while low < high:
        sum = array[low] + array[high]
        if sum == num:
            print("Los números que suman ", num, " son: ", array[low], " y ", array[high])
            break
        elif sum < num:
            low += 1
        else:
            high -= 1

ady_sum(array, 21)
