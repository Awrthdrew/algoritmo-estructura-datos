"""
Solucion Ejercicios Matrices
Algorithmo y Estrutura de Datos
 
"""

def crearMatrizBidimencional(fila:int, columna:int, valor):
    x = [[ valor for _ in range(columna)] for _ in range(fila)]
    return x

    
#Hacer una función que muestre por pantalla el tablero. """)
def printTablero(matriz):
    fila=""
    for i in  range(len(matriz)):
        for j in  range( len( matriz[i]) ):
            fila += str(matriz[i][j]) + "  "
        print( fila )        
        fila=""

        
#Funcion que verifica se hay una linea llena
def hayLineaLlena(matriz):
    totalFilas=len(matriz)
    totalColumnas=len(matriz[0])
    hayFila = False
    elementoAnterior=""
    for i in range(totalFilas):
        hayFila = True
        elementoAnterior=matriz[i][0]
        
        #el simbolo '.' significa vacio
        if elementoAnterior==".": elementoAnterior=""
        
        for j in range(totalColumnas):
            elemento=matriz[i][j]
            hayFila = hayFila and elemento==elementoAnterior
            elementoAnterior=elemento
            
        if(hayFila):
            return hayFila
        
    return hayFila

#Funcion que verifica se hay una columna llena        
def hayColumnaLlena(matriz):
    totalLineas=len(matriz)
    totalColumnas=len(matriz[0])
    hayColumna = False
    elementoAnterior=""
    for i in range(totalColumnas):
        elementoAnterior=matriz[0][i]
        
        #el simbolo '.' significa vacio
        if elementoAnterior==".": elementoAnterior=""
        
        hayColumna=True
        
        for j in range(totalLineas):
            elemento=matriz[j][i]
            hayColumna = hayColumna and elemento==elementoAnterior
            elementoAnterior=elemento
            
        if(hayColumna):
            return hayColumna
        
    return hayColumna

#Funcion que verifica se la diagonal principal está llena, la matriz debe ser cuadrada
def hayDiagonaPrincipalLlena(matriz):
    
    totalLineas=len(matriz)
    totalColumnas=len(matriz[0])
    
    if totalLineas != totalColumnas:
        print("LA MATRIZ DEBE SER CUADRADA")
        return False
    
    hayDiagonal = True    
    elementoAnterior=matriz[0][0]
    for i in range(totalColumnas):
        #propriedade de la diagonal principal i==j
        elemento = matriz[i][i]
        
        #el simbolo '.' significa vacio no deberá considerarse um símbolo
        if elemento=='.': elemento=''
        
        hayDiagonal = hayDiagonal and elemento==elementoAnterior
        elementoAnterior=elemento        
            
        if(not hayDiagonal):
            return hayDiagonal        
        
    return hayDiagonal 

        
tablero = [
          ['B', '.', '.', '.'],
          ['.', 'B', '.', 'O'],
          ['.', 'B', 'B', 'O'],
          ['.', '.', '.', 'B'],          
          ]

print(hayDiagonaPrincipalLlena(tablero))
print(hayColumnaLlena(tablero))
print(hayLineaLlena(tablero))
        
