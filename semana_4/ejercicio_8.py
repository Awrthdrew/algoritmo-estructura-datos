import time
import random 
import os

c = [0, 0, 0, 0] #Genera los caballos
podio = [] #Lista que se agrega con el caballo / .append
meta = 100
carrera = True #Se asigna el while para que corran hasta que lleguen a la carrera

#________________________________________________________________________________

#Función que posibilita el podio al final de que la carrera se concreta de la cantidad de metros
def pos_podio(pos):
    marcador = False
    for posicion in podio:
        if pos == posicion:
            marcador = True
    return marcador

#________________________________________________________________________________

#Iteración de la carrera hasta que termina. 

while carrera:
    for i in range(len(c)):
        if c[i] < meta:
            c[i] += random.randint(1,7)
            
        elif not pos_podio(i+1):
            podio.append(i+1)
            
        print(f"Caballo {i+1}: {c[i]}mts {"-"*c[i]}|>")

    time.sleep(0.5)
    os.system("cls")

    if len(podio) >= len(c):
        carrera = False 
        
#________________________________________________________________________________

print("\n  --*** PODIO ***--")
for i in range(len(podio)):
    print(f"PUESTO N°{i+1}: CABALLO {podio[i]}")