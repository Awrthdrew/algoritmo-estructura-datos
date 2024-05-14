# TRABAJO PRÁCTICO N° 2 | COLA SUPERMERCADO | 2° INGENIERÍA EN SISTEMAS DE LA INFORMACIÓN | 02/05/2024

"""
Integrantes:
BAEZA GRAF, Santiago #36873
BLOCK ERNST, Andrew #36766
ORDOÑEZ, Joaquín #37525
URIBE, Franco #36480
"""

#------------------------------------------------------------------CONSIGNA------------------------------------------------------------------------#

"""
* Título: modelo de simulación de cola de supermercado
* Objetivo: calcular, simuladamente, la cantidad de cajeros para no perder más de 3 clientes por jornada
* Enviar solución por email a alexsandra.cassiano@uap.edu.ar y nicolas.giqueaux@uap.edu.ar
* Grupos de no más de 3 miembros
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
* https://es.wikipedia.org/wiki/Teor%C3%ADa_de_colas
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------#

import random
import sys

def generador_persona():
    """
    Usar esta función por minuto para crear la persona que se suman a la cola de una caja
    Uso: p = generador_persona()
    Retorna: una persona o None si no hay nadie para entrar a la cola en ese minuto
    """
    p = None
    probabilidad_de_entrada = random.randint(1, 10)#probabilidad 1 en 10 de entrar a una sola cola
    if(probabilidad_de_entrada == 1):
        p = {
            "paciencia" : random.randint(5, 15),#cantidad de minutos que tolera en la cola
            "en_cola" : 0,#contador de iteraciones, si llega a grado_de_paciencia se va.
            "en_caja" : 0,#contador de iteraciones cuando ya está en caja, cuando llegue a tiempo_que_tarda_la_caja, se va
            "tardanza_caja" : random.randint(3, 10),#tiempo que le va a tardar la caja en antender a este cliente: de 3 a 10 minutos
            "posicion" : None, #posicion/indice que ocupa dentro de la list/cola de la caja
            "caja_accedida" : None #indica a cual caja de las disponibles accedio
        }
    return p

def Ordenar(caja): #Se ejecuta cada minuto con todas las personas, para verificar si hay alguna posicion delante vacia
    for p in cajas[caja]:   
        pos = cajas[caja].index(p)
        if pos > 0: #si esta en la cola, no siendo atendido en el cajer0
            while cajas[caja][pos-1] is None: 
                cajas[caja][pos-1] = p
                del cajas[caja][pos]
                pos = pos-1

def IngresoCaja(): #Se ejecuta al ingresar una persona, y devuelve la caja mas vacia para que entre en esa
    def porLen(info): #Funcion que servira para hacer el sorted() segun el valor de ['len']
        return info['len']
    
    personas_en_caja = [_ for _ in range(num_cajas)] #list con cantidad de elementos correspondiente a la de cajas
        
    for i in range(num_cajas):
        if len(cajas[i]) == 0: #si la caja esta totalmente vacia, va directo a esa sin analizar las demas
            return i 
        else:
            caja_info = {'indice': i, 'len': len(cajas[i])} #dict con el indice de la caja y la cantidad de personas en ella             
            personas_en_caja[i] = caja_info
            
    personas_en_caja = sorted(personas_en_caja, key=porLen)
    return personas_en_caja[0]['indice'] #devuelve el indice de la caja con la menor cantidad de personas

def Espera(p): #Se ejecuta si la persona no esta siendo atendida en caja, cada minuto
    
    p['en_cola'] += 1 #suma al tiempo que estuvo esperando en la cola a ser atendido por minuto
    
    if p['en_cola'] > p['paciencia']: #si el tiempo de espera supera su paciencia
        #print(f'PERSONA SE FUE ENOJADA POR ESPERAR MUCHO (pos: {p["posicion"]} - caja: {p["caja_accedida"]})')
        global cantidad_personas_abandonaron
        cantidad_personas_abandonaron += 1
        cajas[p['caja_accedida']].remove(p)
        #personas.remove(p) #el remove generaba problemas, al alterar la lista en la que se iteraba el for p in personas
        personas[personas.index(p)] = 'del' #al cambiar p por 'del', no se modifican los indices de los demas elementos por esta iteracion
        return True #si se elimino la persona ejecuta el break para saltar directamente a la siguiente
    
def Atencion(p): #Se ejecuta si la persona esta en el cajero siendo atendida
    
    p['en_caja'] += 1 #suma al tiempo en caja por minuto
    
    if p['en_caja'] > p['tardanza_caja']: #cuando termina la compra en la caja
        #print(f"PERSONA SE FUE CON LA COMPRA (caja: {p['caja_accedida']})")
        global cantidad_personas_atendidas, suma_tiempo_cajas
        cantidad_personas_atendidas += 1
        suma_tiempo_cajas += p['tardanza_caja']
        cajas[p['caja_accedida']].remove(p) #se elimina la persona de la caja
        #personas.remove(p) 
        personas[personas.index(p)] = 'del' 
            

repetir = True

while repetir: #se va a ejecutar mientras num_cajas > 0
    jornada =  60 * 8 #variable que marca el fin de las 8 horas de trabajo
    cantidad_personas_abandonaron = 0
    cantidad_personas_atendidas = 0
    suma_tiempo_cajas = 0
    cantidad_personas_generadas = 0
    personas = [] #lista que permite recorrer todas las personas creadas en las distintas cajas
    
    while True: #asegura que num_cajas reciba como input un valor que se pueda castear a int
        num_cajas = input('Cuantas cajas quiere que haya disponibles? ')
        try:
            int(num_cajas)
            num_cajas = int(num_cajas)
            break
        except ValueError: #si no se puede castear, devuelve un mensaje y repite el input
            print('ESO NO ES UN NUMERO ENTERO!!!')
    cajas = [[] for _ in range(num_cajas)]

    if num_cajas > 0:
        
        #************************************************************************
        #MOTOR PRINCIPAL
        #Bucle que representa lo que sucede en cada minuto de la jornada laboral
        #Cada iteración representa lo que sucede en un minuto de la jornada   
        for minuto in range(jornada): #se ejecuta jornada veces
                
            #print(f'minuto: {minuto}') 
            p = generador_persona()
            
            if(p): #cuando se crea exitosamente una persona
                personas.append(p) 
                cantidad_personas_generadas += 1
                p['caja_accedida'] = IngresoCaja() 
                cajas[p['caja_accedida']].append(p)
                p['posicion'] = cajas[p['caja_accedida']].index(p)
                #print(f"CREADO EN POSICION {p['posicion']} - CAJA {p['caja_accedida']}") 
            
            while personas: #permite que, si se acaba el tiempo, se terminen de atender o ir las personas en cola y caja
                for p in personas:
                    
                    
                    Ordenar(p['caja_accedida'])    
                    
                    p['posicion'] = cajas[p['caja_accedida']].index(p)
                    
                    if p['posicion'] != 0:
                        if Espera(p):
                            continue
                    if p['posicion'] == 0:
                        Atencion(p)
                        continue

                #estas 2 lineas se encargan de remover de personas[] a quienes se fueron atendidos o enojados
                personas_copia = personas.copy() #se crea la copia para no alterar la lista sobre la cual se itera
                personas = [p for p in personas_copia if p != 'del'] #si p no es == 'del', se mantiene en la list personas
                            
                #print(cajas) #permite llevar seguimiento de los cambios por minuto en cada persona y posiciones
                if minuto < jornada-1: #mientras siga corriendo el tiempo de la jornada, el while se ejecuta solo una vez
                    break

        promedio_tiempo_cajas = suma_tiempo_cajas // cantidad_personas_atendidas

        print(F'\n--- EN UN JORNADA DE {int(jornada / 60)} HORA/S ---')
        print("Cantidad cajas: " + str(num_cajas))
        print("Abandonaron: " + str(cantidad_personas_abandonaron))
        print("Atendidos: " + str(cantidad_personas_atendidas))
        print("Promedio de tiempo de atención: " + str(promedio_tiempo_cajas))
        print('Cantidad de personas que ingresaron: ' + str(cantidad_personas_generadas) + '\n')

    else: 
        print('FINALIZO LA EJECUCION DEL PROGRAMA')
        repetir = False
        sys.exit(1)
        
        
