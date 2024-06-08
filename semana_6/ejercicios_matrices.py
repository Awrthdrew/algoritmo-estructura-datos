# Manera de expresar una matriz por fila

"""matrizarda = [  [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

for row in matrizarda:
    print(row)"""
    
# Recorre todos los elementos de la matriz de acuerdo a sus elementos. Accede de acuerdo a las posiciones. Es por fila también

"""matrizarda = [  [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

for row in matrizarda:
    for element in row:
        print(element)"""
        
# Recorre por fila, obligando a las listas que tengan un space-between en cada elemento. Después de cada fila, imprime un salto de línea

"""matrizarda = [  [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

for row in matrizarda:
    for element in row:
        print(element, end = " ")
    print()"""
    
"""1.  Crear una función que imprimir en pantalla una matriz F x C, el usuario deberá informar el 
número de líneas F y de columnas C de la matriz, llenar todos los elementos de la matriz con 
el carácter ‘.’"""

"""def matriz(F, C):
    for i in range(F):
        for j in range(C):
            print(".", end = " ")
        print()
matriz(3, 3)"""

#2.  Crear una función que verifica se existe alguna línea llena de caracteres iguales


#3.  Crear una función que verifica se existe alguna columna llena de caracteres iguales 


"""4.  Crear una función que verifica se existe alguna diagonal llena de caracteres iguales, 
considere solamente matrices cuadráticas, y verifique la diagonal principal y secundaria.""" 



"""5.  Crear un Tic-tac-toe juego donde el usuario empieza configurando el tamaño del tablero y el 
símbolo de sus piezas. El juego debe alternar entre los jugadores hasta tener un Ganador O! 
tablero lleno. """

import random

print()
print("  TA-TE-TI")


num_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tateti_tabla = [[1,2,3], 
                [4,5,6], 
                [7,8,9]]

rows = 3   
cols = 3

# Impresión del tablero con las filas y columnas,
def imp_tablero():
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end = "")
        for j in range(cols):
            print("", tateti_tabla[i][j], end = " |")
    print("\n+---+---+---+")

def mod_array(num, turn):
    num -= 1
    if(num == 0):
        tateti_tabla[0][0] = turn
    elif(num == 1):
        tateti_tabla[0][1] = turn
    elif(num == 2):
        tateti_tabla[0][2] = turn
    elif(num == 3):
        tateti_tabla[1][0] = turn
    elif(num == 4):
        tateti_tabla[1][1] = turn
    elif(num == 5):
        tateti_tabla[1][2] = turn
    elif(num == 6):
        tateti_tabla[2][0] = turn
    elif(num == 7):
        tateti_tabla[2][1] = turn
    elif(num == 8):
        tateti_tabla[2][2] = turn

def check_winner(tateti_tabla):
    
    #Horizontal.
    if(tateti_tabla[0][0] == 'X' and tateti_tabla[0][1] == 'X' and tateti_tabla[0][2] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[0][0] == 'O' and tateti_tabla[0][1] == 'O' and tateti_tabla[0][2] == 'O'):
        print("Ganador O!")
        return "O"
    if(tateti_tabla[1][0] == 'X' and tateti_tabla[1][1] == 'X' and tateti_tabla[1][2] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[1][0] == 'O' and tateti_tabla[1][1] == 'O' and tateti_tabla[1][2] == 'O'):
        print("Ganador O!")
        return "O"
    if(tateti_tabla[2][0] == 'X' and tateti_tabla[2][1] == 'X' and tateti_tabla[2][2] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[2][0] == 'O' and tateti_tabla[2][1] == 'O' and tateti_tabla[2][2] == 'O'):
        print("Ganador O!")
        return "O"
    
    #Vertical.
    if(tateti_tabla[0][0] == 'X' and tateti_tabla[1][0] == 'X' and tateti_tabla[2][0] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[0][0] == 'O' and tateti_tabla[1][0] == 'O' and tateti_tabla[2][0] == 'O'):
        print("Ganador O!")
        return "O"
    elif(tateti_tabla[0][1] == 'X' and tateti_tabla[1][1] == 'X' and tateti_tabla[2][1] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[0][1] == 'O' and tateti_tabla[1][1] == 'O' and tateti_tabla[2][1] == 'O'):
        print("Ganador O!")
        return "O"
    elif(tateti_tabla[0][2] == 'X' and tateti_tabla[1][2] == 'X' and tateti_tabla[2][2] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[0][2] == 'O' and tateti_tabla[1][2] == 'O' and tateti_tabla[2][2] == 'O'):
        print("Ganador O!")
        return "O"
    
    #Diagonal.
    elif(tateti_tabla[0][0] == 'X' and tateti_tabla[1][1] == 'X' and tateti_tabla[2][2] == 'X'):
        print("Ganador X!")
        return "X"
    elif(tateti_tabla[0][0] == 'O' and tateti_tabla[1][1] == 'O' and tateti_tabla[2][2] == 'O'):
        print("Ganador O!")  
        return "O"
    elif(tateti_tabla[0][2] == 'X' and tateti_tabla[1][1] == 'X' and tateti_tabla[2][0] == 'X'):
        print("Ganador X!")  
        return "X"
    elif(tateti_tabla[0][2] == 'O' and tateti_tabla[1][1] == 'O' and tateti_tabla[2][0] == 'O'):
        print("Ganador O!") 
        return "O" 
    else:
        return "N"
    
bucle = False
turn_cont = 0

while(bucle == False):
    
    # Turno del jugador X.
    if(turn_cont % 2 == 0):
        imp_tablero()
        while True:
            pos_choice = int(input("\nTURNO DE JUGADOR X (1-9): "))
            if pos_choice >= 1 and pos_choice <= 9 and pos_choice in num_posibles:
                mod_array(pos_choice, 'X')
                num_posibles.remove(pos_choice)
                break
            else:
                print("Jugada no válida, intente nuevamente.")
        turn_cont += 1
    
    # Turno del jugador O.    
    else:
        imp_tablero()
        while True:
            pos_choice = int(input("\nTURNO DE JUGADOR O (1-9): "))
            if pos_choice >= 1 and pos_choice <= 9 and pos_choice in num_posibles:
                mod_array(pos_choice, 'O')
                num_posibles.remove(pos_choice)
                break
            else:
                print("Jugada no válida, intente nuevamente.")
        turn_cont += 1
    
    #Pseudo algoritmo para que juege la compu. (El .choice() hace elección )
    """else:
        while(True):
            pc_pos = random.choice(num_posibles)
            print("\nLa computadora jugó en la posición: ", pc_pos)
        
            # Turno de la compu.
            if(pc_pos in num_posibles):
                mod_array(pc_pos, 'O')
                num_posibles.remove(pc_pos)
                turn_cont += 1
                break"""
        
    # Verificación de ganador.
    winner = check_winner(tateti_tabla)
    if(winner != "N"):
        print("\nFELICITACIONES AL JUGADOR: ", winner)
        break