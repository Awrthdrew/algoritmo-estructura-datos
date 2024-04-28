#5 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Lista inicial
lista = [20, 11, 16, 9, 12, 14, 17, 19, 13, 15]

# Dos primeras iteraciones de Bubble Sort
bubble_sort(lista)
print("Contenido de la lista después de las dos primeras iteraciones de Bubble Sort:")
print(lista)


#6
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Lista inicial
lista = [20, 11, 16, 9, 12, 14, 17, 19, 13, 15]

# Dos primeras iteraciones de Insertion Sort
insertion_sort(lista)
print("Contenido de la lista después de las dos primeras iteraciones de Insertion Sort:")
print(lista)
