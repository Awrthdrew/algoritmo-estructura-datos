"""7. Imagine un Buffer de impresión con una capacidad máxima para almacenar 20 documentos, 
simule la gestión de la impresora en caso de fallar a través de una fila circular del tipo FIFO 
(First In First Out), asuma que los documentos que superan la capacidad máxima se pierden. 
La selección del usuario será A, I o S, A para agregar documento, I imprimir y S salir del 
programa. En el caso de la operación A Agregar, el usuario debe informar el nombre del 
documento que ingresará a la fila."""

import time as t

buffer_imp = []
cap_max = 5


#Función que agrega los documentos como parámetro sabiendo si la capacidad del buffer está por arriba.
def agregar_docx(docx):
    if len(buffer_imp) < cap_max:
        buffer_imp.append(docx)
        print(f'\n * Agregando {docx} al buffer')
        t.sleep(1)
    else:
        t.sleep(1)
        print('\n* ESTAMOS LLENOS. NO SE PUEDE CARGAR MÁS *')

#Impresión de los documentos. .pop popeando el último documento agregando. El cual limpia el buffer. 
def imp_docx():  
    if buffer_imp:
        docx_imp = buffer_imp.pop(0)
        print(f"\n * Documento preparado para imprimirse '{docx_imp}'...")
        t.sleep(1)
    else:
        t.sleep(1)
        print("\n * EL BUFFER ESTÁ VACÍO")
    
# Interfaz
def menu():
    while True:
        op = input('\n  REGISTRO NACIONAL  | 🇦🇷 \n ------------------------- \n 1.AGREGAR DOCUMENTO \n 2.IMPRIMIR DOCUMENTO \n 3.FINITO \n -------------------------\n Elegir: ')
        if op == '1':
            docx = input('Documento por agregar: ')
            agregar_docx(docx)
        elif op == '2':
            imp_docx()
        elif op == '3':
            print("\n * APAGANDO SISTEMA")
            t.sleep(2)
            quit()

#Ejecución del programa
menu()