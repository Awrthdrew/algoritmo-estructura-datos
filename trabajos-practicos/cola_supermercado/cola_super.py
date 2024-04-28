"""
* Título: modelo de simulación de cola de supermercado
* Objetivo: calcular, simuladamente, la cantidad de cajeros para no perder más de 3 clientes por jornada
* Enviar solución por email a alexsandra.cassiano@uap.edu.ar y nicolas.giqueaux@uap.edu.ar
* Grupos de no más de 4 miembros
*
* Consideraciones:
*   -> Una cola por caja
*   -> Cantidad de cajas variables. Usar listas de cajas. Comenzar con una sola caja, luego ir aumentando.
*   -> Cada ejecución del algoritmo representa una jornada de trabajo en donde la cantidad de cajas no varía.
*   -> Para cambiar la cantidad de cajas se deberá detener el programa y parametrizar la cantidad de cajas que se desea.
*   -> Jornada dura 8 horas.
*   -> La frecuencia promedio de ingreso de una persona a la caja durante la jornada es una cada 10 minutos.
*   -> El tiempo que tarda cada caja en atender está entre 3 a 10 minutos. Determinar al azar.
*   -> Las personas tiene distintos grados de paciencia de espera en la cola, 
       si se agota abandona la compra: esperan entren 5 a 15 minutos. 
       Determinar al azar cuando entra a la cola.
*   -> Si un cliente ya está en la caja siendo atendido espera a terminar y no abandona.
*   -> Política de cajas "Primero en entrar, primero en salir"
*   -> Cuando una pesona sale de la caja se saca de la lista y se desplazan todos los elementos restantes. 
       Osea, en el índice 0 del array de la cola de la caja representa a la persona que se está atendiendo,
       cuando esta sale, se saca del array y la persona que estaba en el índice 1 para al 0, la que estaba 
       en el indice 2 pasa al 1 y así sucesivamente
*   -> Iterar cada segundo de las 8 horas de la jornada, es decir que se deberá hacer un bucle que tenga 8(horas) * 60(minutos/h) ciclos.

*   Reporte al final del día:    
*   -> Cantidad de cajas
*   -> Cantidad de personas que abondonan la compra
*   -> Cantidad de personas atendidas
*   -> Promedio de tiempo en caja
*
* https://es.wikipedia.org/wiki/Teor%C3%ADa_de_colas"""

import random as r

def cola_super(num_cajas):
    jornada = 8 * 60  
    atencion_min = 3
    atencion_max = 10
    espera_min = 5
    espera_max = 15
    clientes_perdidos = 0

    cajas = [[] for _ in range(num_cajas)]
    caja_vacia = True  

    for minuto in range(jornada):
        if r.random() < 1/10:  
            caja_vacia = False
            caja_index = False
            for i in range(len(cajas)):
                if not cajas[i]:  
                    caja_vacia = True
                    caja_index = i
                    break
            if caja_vacia:  
                tiempo_atencion = r.randint(atencion_min, atencion_max)
                cajas[caja_index].append(tiempo_atencion)
            else:  
                tiempo_espera = r.randint(espera_min, espera_max)
                if tiempo_espera >= jornada - minuto:  
                    clientes_perdidos += 1
                """else:
                    caja_menos_tiempo = min(cajas, key=lambda caja: sum(caja)) 
                    tiempo_atencion = r.randint(atencion_min, atencion_max)
                    caja_menos_tiempo.append(tiempo_atencion)"""
        for caja in cajas:
            if caja:
                caja[0] -= 1
                if caja[0] == 0:  
                    caja.pop(0)
    return clientes_perdidos

num_cajas = 5
clientes_perdidos = cola_super(num_cajas)

if clientes_perdidos == 0:
    print(f"\nGRAN TRABAJO! La cola del supermercado no perdió ningún cliente.")
elif clientes_perdidos == 1:
    print(f"\nPor causa de la demora en la cola del supermercado, se perdió: {clientes_perdidos} cliente.")
else:
    print(f"\nPor causa de la demora en la cola del supermercado, se perdieron: {clientes_perdidos} clientes.")