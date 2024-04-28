inline = [
    ['.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', 'O', '.', '.', 'X'],
    ['.', '.', 'O', '.', '.', '.', '.'],
    ['.', 'O', '.', '.', 'X', '.', '.'],
    ['O', '.', 'O', '.', 'X', 'X', 'X']
]


def mostrar():
    print('- 4 IN LINE -')
    print('1 2 3 4 5 6 7')
    for fila in range(len(inline)):
        for columna in range(len(inline[0])):  # Accede al largo de la primera fila para columnas
            print(inline[fila][columna], end = ' ')
        print()  # Salto de línea después de cada fila

def status():
    r = {"LLENO" : True, "GANADOR": "No todavía", "TIPO": "?"}

#--------------------------------------------------------------------

# ¿HAY CASILLERO VACÍO?
    for fila in range(len(inline)):
        for columna in range(len(inline[fila])):
            if inline[fila][columna] == '.':
                r["LLENO"] = False
                break

#BUSCAR INLINE HORIZONTALMENTE
    for fila in range(6):
        for columna in range(4):
            if(inline[fila][columna] == 'X' and
            inline[fila][columna+1] == 'X' and
            inline[fila][columna+2] == 'X' and
            inline[fila][columna+3] == 'X'):
                r["GANADOR"] = "X"
                r["TIPO"] = "LH"
                return r
                
            if(inline[fila][columna] == 'O' and
            inline[fila][columna+1] == 'O' and
            inline[fila][columna+2] == 'O' and
            inline[fila][columna+3] == 'O'):
                r["GANADOR"] = "O"
                r["TIPO"] = "LH"
                return r

#BUSCAR INLINE VERTICALMENTE
    for columna in range(7):
        for fila in range(3):
            if(inline[fila][columna] == 'X' and
            inline[fila+1][columna] == 'X' and
            inline[fila+2][columna] == 'X' and
            inline[fila+3][columna] == 'X'):
                r["GANADOR"] = "X"
                r["TIPO"] = "LV"
                return r
                 
            if(inline[fila][columna] == 'O' and
            inline[fila+1][columna] == 'O' and
            inline[fila+2][columna] == 'O' and
            inline[fila+3][columna] == 'O'):
                r["GANADOR"] = "O"
                r["TIPO"] = "LV"
                return r
                
                
#BUSCAR INLINE DIAGONALMENTE \
    for columna in range(4):
        for fila in range(3):
            if(inline[fila][columna] == 'X' and
            inline[fila+1][columna+1] == 'X' and
            inline[fila+2][columna+2] == 'X' and
            inline[fila+3][columna+3] == 'X'):
                r["GANADOR"] = "X"
                r["TIPO"] = "D\\"
                return r
                
            if(inline[fila][columna] == 'O' and
            inline[fila+1][columna+1] == 'O' and
            inline[fila+2][columna+2] == 'O' and
            inline[fila+3][columna+3] == 'O'):
                r["GANADOR"] = "O"
                r["TIPO"] = "D\\"
                return r
                
#BUSCAR INLINE DIAGONALMENTE /
    for columna in (3,4,5,6):
        for fila in range(4):
            if(inline[fila][columna] == 'X' and
            inline[fila+1][columna-1] == 'X' and
            inline[fila+2][columna-2] == 'X' and
            inline[fila+3][columna-3] == 'X'):
                r["GANADOR"] = "X"
                r["TIPO"] = "D\\"
                return r
                
            if(inline[fila][columna] == 'O' and
            inline[fila+1][columna-1] == 'O' and
            inline[fila+2][columna-2] == 'O' and
            inline[fila+3][columna-3] == 'O'):
                r["GANADOR"] = "O"
                r["TIPO"] = "D//"
                return r
    

mostrar()
print(status())
