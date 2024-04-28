"""
* Titulo: modelo de simulación de cola de supermercado
* Objetivo: calcular empíricamente la cantidad de cajeros para no perder mas de 3 clientes por jornada
* Enviar solución por email
* Grupos de no más de 3 miembros
*
* Consideraciones:
*   -> una cola por caja
*   -> cantidad de cajas variables. Usar listas de cajas
*   -> jornada dura 8 horas
*   -> La frecuencia promedio de ingreso de una persona a la caja durante la jornada es una cada 10 minutos.
*   -> El tiempo que tarda cada caja en atender está entre 3 a 10 minutos
*   -> Las personas tiene distintos grados de paciencia de espera en la cola, si se agota abandona la compra: esperan entren 10 a 20 minutos
*   -> Si ya está en la caja siendo atendido espera a termniar y no abandona
*   -> Política de cajas "Primero en entrar, primero en salir"
*   -> Cuando una pesona sale de la caja se saca de la lista y se desplazan todos los elementos restantes. 
       Osea, en el índice 0 del array de la cola de la caja representa a la persona que se está atendiendo,
       cuando esta sale, se saca del array y la persona que estaba en el índice 1 para al 0, la que estaba 
       en el indice 2 pasa al 1 y así sucesivamente

*   Reporte al final del dia:    
*   -> Cantidad de cajas
*   -> Cantidad de personas que abondonan la compra
*   -> Cantidad de personas atendidas
*   -> Promedio de tiempo en caja
*
* https://es.wikipedia.org/wiki/Teor%C3%ADa_de_colas
"""


