import math
import random

minuto = 0
fin_de_la_jornada = 60 * 8
cantidad_personas_abandonaron = 0
cantidad_personas_atendidas = 0
promedio_tiempo_cajas = 0

cajas = []



cant_cajas = (int)(input("Cuantas cajas desea tener? "))


for x in range(cant_cajas):
    cajas.append([])

def generador_persona():
    persona = None
    probabilidad_de_entrada = random.randint(1,10)
    if(probabilidad_de_entrada == 1):
        persona = {"grado_de_paciencia" : random.randint(5,15),
                   "tiempo_esperando_cola" : 0,
                   "tiempo_esperando_en_caja" : 0,
                   "tiempo_que_tarda_la_caja" : random.randint(3,10)
                   }
    return persona

z = 0 #variable que cuenta en que caja se metio la ultima persona, se incrementa cada vez metiendo la persona en la caja siguiente hasta que llegue al limite de cajas existentes

cantidad_de_cajas = len(cajas)

while(minuto <= fin_de_la_jornada):
    minuto += 1
    
    #Logica de entrada a la cola
    persona = generador_persona()
    if(persona):
        cajas[z].append(persona)
        #print("Entro una persona a la cola: "  + str(persona))
        z += 1 #se aumenta para meter a la siguiente persona en la siguente caja
        print(z)

    if z == len(cajas):
        z = 0 #Se reinicia una vez que se llega a la ulitma caja para empezar devuelta por la caja 0
    

    for b in range(len(cajas)):
        if len(cajas[b]) > 0:
            print("-"*25 + "Minuto " + str(minuto) + "-"*25)
            for j in range(len(cajas)):
                print("Personas en caja " + str(j) + ": " + str(len(cajas[j])))
            print("-"*60)
            break    #este break esta porque si llega a haber una persona en mas de una caja 

    #Logica de Paciencia
    for x in range(len(cajas)):
        if len(cajas[x]) > 1: #Pregunta si hay una persona en la fila, y si es que lo hay, comienza a sumarle valores a los minutos esperados
            i = 1
            while(i<len(cajas[x])): #Bucle que recorre las personas que son diccionarios
                cajas[x][i] ["tiempo_esperando_cola"] += 1 # se le agrega un minuto al contador de espera de cada persona
                if cajas[x][i] ["tiempo_esperando_cola"] == cajas[x][i] ["grado_de_paciencia"]: #compara si el valor esperandop en cola es igual al grado de paciencia de la persona, si lo es, la elimina de la cola
                    del cajas[x][i] #Elimina esa persona de la cola.
                    cantidad_personas_abandonaron += 1 #se le suma al contador de personas que abandonaron
                i += 1

    #Logica de La Salida de la Cola
    for x in range(len(cajas)):
        if len(cajas[x]) > 0: #Se fija si hay personas en la cola
            cajas[x][0] ["tiempo_esperando_en_caja"] += 1 #Si es que lo hay le suma un valor al contador de minutos esperados en caja
            if cajas[x][0] ["tiempo_esperando_en_caja"] == cajas[x][0] ["tiempo_que_tarda_la_caja"]: #Compara si el valor del tiempo esperado en caja es igual al que deberia tardar en una caja, si lo es, elimina a esa persona de la fila
                cantidad_personas_atendidas += 1 #Se le suma uno al contador de la personas que fueron atendidas
                promedio_tiempo_cajas = promedio_tiempo_cajas + cajas[x][0] ["tiempo_que_tarda_la_caja"] #Se le suma la cantidad de minutos que tardo cada caja para atender para luego dividirlo por la cantidad de personas, aun no podemos hacer esto ya que no sabemos la cantidad de personas que fueron atendidas
                del cajas[x][0]
promedio_tiempo_cajas = promedio_tiempo_cajas / cantidad_personas_atendidas # se saca el promedio de tiempo que tarda cada caja, en este caso es la suma del total de minutos que tardaron en atender por la cantidad de personas que atendieron.


print("Cantidad cajas: " + str(cantidad_de_cajas))
print("Abandonaron: " + str(cantidad_personas_abandonaron))
print("Atendidos: " + str(cantidad_personas_atendidas))
print("Promedio de tiempo de atención: " + str(round(promedio_tiempo_cajas, 2)))   