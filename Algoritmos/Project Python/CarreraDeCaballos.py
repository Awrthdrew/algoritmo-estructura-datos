import random
import time

caballos = [0, 0, 0, 0]

def mover_caballos(caballos):
    contador = 0
   
    podio = []
    nombres = ["Enzo", "Teo", "Gabi", "Seba"]
    metrosR = 0
    metros = 50
    

   
    while metrosR <= metros:
        print("-" * 100)

        if contador == (len(caballos)):
            for z in range(len(caballos)):
                
                print(str(z + 1) + "er Puesto caballo: " + str(nombres[int(podio[z]) - 1]))
            break

        for x in range(len(caballos)):
            if caballos[x] > 50:
                if(x + 1) not in podio:
                    podio.append(x + 1)
                    contador += 1

        for i in range(len(caballos)):
            caballos[i] = caballos[i] + random.randint(1,5)
            print(" " * caballos[i] + "o")
        
  
        metrosR += 1
        time.sleep(0.25)
print(mover_caballos(caballos))