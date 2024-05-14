lista = [1, 3, 5 ,2, 7, 89, 23, 43, 69, 77, 25, 10, 93, 11, 26]
lista.sort()

print(lista)
#print(len(lista)) Ver cantidad de elementos en la lista

# 1. Buscar punto medio.
# 2. Ver si el valor medio es el que buscamos.
# 3. El número es < al valor que buscamos. Aumentamos inicio 1 sobre el puntero.
# 4. El numero es > al avlor que buscamos. Disminuimos el final 1 bajo el puntero.
# 5. Si inicio se vuelve >= que final entonces el valor no se encuentra en la lista.

def escarabajo_binario(valor):
    inicio = 0
    final = len(lista) - 1
    
    while inicio <= final:
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero
    
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None
            
def buscar_escarabajo():
    while True:
        valor = int(input('Qué haces mi rey, qué número de la lista andas necesitando?: '))
        pos_busqueda = escarabajo_binario(valor)
        if pos_busqueda is None:
            print(f'Flaco, {valor} no está!!! Intenta con otro número!!!')
        else:
            print(f'Papucho, sí está el {valor} con {pos_busqueda + 1} búsquedas binarias.')
            break

buscar_escarabajo()

# CÓDIGO DE BÚSQUEDA BINARIA QUE NO ESTÁ FUNCIONANDO COMO CORRESPONDE

