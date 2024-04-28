tablero = [
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', 'O', '.', 'O', '.', '.', '.'],
          ['.', '.', 'O', '.', '.', '.', '.'],
          ['.', 'O', '.', 'X', '.', '.', '.'],
          ['O', '.', 'O', 'X', 'X', 'X', 'X']
          ]

"""tablero = [
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', 'X', '.', '.', '.'],
          ['.', '.', 'O', 'X', 'X', 'X', 'O']
          ]
"""
          
def mostrar():
    print("1 2 3 4 5 6 7")
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            print(tablero[fila][columna], end=' ')
        print()
        
def status():
    r = {"lleno": True, "ganador": "?","tipo":"?"}
    #1) chequear si hay algun casillero vacio
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == '.':
                r["lleno"] = False
                break 
    #2) Buscar por algun 4 en linea horizontal
    for fila in range(6):
        for columna in range(4):
            if(tablero[fila][columna] == 'X' and
               tablero[fila][columna+1] == 'X' and
               tablero[fila][columna+2] == 'X' and
               tablero[fila][columna+3] == 'X'):
                r["ganador"] = "X"
                r["tipo"] = "LH"                

            if(tablero[fila][columna] == 'O' and
               tablero[fila][columna+1] == 'O' and
               tablero[fila][columna+2] == 'O' and
               tablero[fila][columna+3] == 'O'):
                r["ganador"] = "O"
                r["tipo"] = "LH"
                
    #3) Buscar por algun 4 en linea de forma vertical
    for columna in range(7):
        for fila in range(3):
            if(tablero[fila][columna] == 'X' and
                tablero [fila+1][columna] == 'X' and
                tablero [fila+2][columna] == 'X' and
                tablero [fila+3][columna] == 'X'):
                r["ganador"] = "X"
                r["tipo"] = "LV"
            if(tablero[fila][columna] == 'O' and
               tablero[fila+1][columna] == 'O' and
               tablero[fila+2][columna] == 'O' and
               tablero[fila+3][columna] == 'O'):
                r["ganador"] = "O"
                r["tipo"] = "LV"
                
     
    #4) Buscar por algun 4 en linea diagonal /
    for columna in (3,4,5,6):
        for fila in range(4):
            if(tablero[fila][columna] == 'X' and
                tablero [fila+1][columna-1] == 'X' and
                tablero [fila+2][columna-2] == 'X' and
                tablero [fila+3][columna-3] == 'X'):
                r["ganador"] = "X"
                r["tipo"] = "D/"
            if(tablero[fila][columna] == 'O' and
               tablero[fila+1][columna-1] == 'O' and
               tablero[fila+2][columna-2] == 'O' and
               tablero[fila+3][columna-3] == 'O'):
                r["ganador"] = "O"
                r["tipo"] = "D/"

                
    #5) Buscar por algun 4 en linea diagonal \
    for columna in range(4):
        for fila in range(3):
            if(tablero[fila][columna] == 'X' and
                tablero [fila+1][columna+1] == 'X' and
                tablero [fila+2][columna+2] == 'X' and
                tablero [fila+3][columna+3] == 'X'):
                r["ganador"] = "X"
                r["tipo"] = "D\\"
            if(tablero[fila][columna] == 'O' and
               tablero[fila+1][columna+1] == 'O' and
               tablero[fila+2][columna+2] == 'O' and
               tablero[fila+3][columna+3] == 'O'):
                r["ganador"] = "O"
                r["tipo"] = "D\\"
     
    
    return r
        
mostrar()
print(status())


