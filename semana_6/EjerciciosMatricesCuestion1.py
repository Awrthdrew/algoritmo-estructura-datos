"""
Solucion Ejercicios Matrices
Algorithmo y Estrutura de Datos
 
"""

#matriz de '.'
def crearMatrizBidimencional1(fila:int, columna:int):
    x = [[ '.' for _ in range(columna) ] for _ in range(fila)]
    return x

#matriz donde los valores son numero de su linea
def crearMatrizBidimencional2(fila:int, columna:int):
    x=[]
    for i in range(fila):
        x.insert(i, [ i for _ in range(columna) ] )
    return x

#matriz donde los valores son numero de su columna
def crearMatrizBidimencional3(fila:int, columna:int):
    x=[]
    for i in range(fila):
        linea=[]
        for j in range(columna):
            #linea.insert(j,j)
            linea.append(j)
        x.insert(i,linea)
    return x

#matriz donde los valores son incrementados de 1 iniciando en 0
def crearMatrizBidimencional4(fila:int, columna:int):

    x = [[(i*columna)+j for j in range(columna)] for i in range(fila)]
    return x


def printTablero(matriz):
    fila=""
    for i in  range(len(matriz)):
        for j in  range( len( matriz[i]) ):
            fila += str(matriz[i][j]) + "     "
        print( fila )        
        fila=""
    print(" ")
        

matriz = crearMatrizBidimencional1(5,3)
printTablero(matriz)

matriz = crearMatrizBidimencional2(5,3)
printTablero(matriz)

matriz = crearMatrizBidimencional3(5,3)
printTablero(matriz)

matriz = crearMatrizBidimencional4(4,3)
printTablero(matriz)































def hayLineaLlena(matriz):
    totalFilas=len(matriz)
    totalColumnas=len(matriz[0])
    hayFila = False
    elementoAnterior=""
    for i in range(totalFilas):
        elementoAnterior=matriz[i][0]
        
        for j in range(totalColumnas):
            elemento=matriz[i][j]
            hayFila = elemento==elementoAnterior
            elementoAnterior=elemento
            
        if(hayFila):
            return hayFila
        
    return hayFilas   

        
        
