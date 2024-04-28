"""
Generadores eólicos
===================

Datos reales obtenidos de: https://www.smn.gob.ar/descarga-de-datos
Valores promedios mensuales por estación meteorológica desde 1981 a 2010 (29 años)

Averiguar:
----------
3) Lugar y mes más húmedo y el más seco del país
4) Temperatura promedio durante todo el año en Paraná

Los datos están estruturados como segue:
estadisticas = [ Estacion1, Estacion2, Estacion3... EstacionN ]

EstacionN = {
    Estación: Nombre de la Estación   #0
    Temperatura média (°C): Valores, #1
    Temperatura máxima (°C) : Valores, #2
    Temperatura mínima (°C): Valores, #3
    Humedad relativa (%) : Valores, #4
    Velocidad del Viento (km/h) : Valores, #5
    Nubosidad total (octavos) : Valores, #6
    Precipitación (mm) : Valores, #7
    Frecuencia de días con Precipitación superior a 0.1 mm : Valores #8

}

Donde Valores representa todos los meses del año y su respectivo valor de medición
Valores={'Ene':float,...,'Dec':float }


"""
import datos

def mediaValores(valores:dict):
    i=0
    total=0
    for k,v in valores.items():
        if v!=None:
            total+=v
        i+=1
    return total/i

def maxValorMes(medicoes:dict):
    max=0;
    nome=""
    for k,v in medicoes.items():
        if v!=None and v>max:
            max=v
            nome=k
    return [nome,max]

estadisticas = datos.estadisticas

#3) Lugar y mes más húmedo y el más seco del país
#Humedad relativa (%) : Valores, #4  Major % de Humidad
#Precipitación (mm) : Valores, #7    Major % de Precipitación
def preguntaTres():
    estacao: dict
    nome_estacion_major_humidad = ""
    nome_estacion_major_precipitacion=""
    mes_valor_major_humedad = ["",0]
    mes_valor_major_precipitacion= ["",0]

    for estacion in estadisticas:
        nome_estacion_humedad=""
        nome_estacion_precipitacion=""
        mes_valor_humedad=["",0]
        mes_valor_precipitacion=["",0]

        indice_values = 0
        for v in estacion.values():
            #Nombre de la Estación
            if indice_values==0:
                nome_estacion_precipitacion = v
                nome_estacion_humedad = v

            # Humedad relativa (%)  indice_values=4
            if indice_values==4:
                mes_valor_humedad = maxValorMes(v)
                if mes_valor_humedad[1] != None and mes_valor_humedad[1] > mes_valor_major_humedad[1]:
                    mes_valor_major_humedad= mes_valor_humedad
                    nome_estacion_major_humidad = nome_estacion_humedad

            # Precipitación (mm) , indice_values = 7
            if indice_values==7:
                mes_valor_precipitacion = maxValorMes(v)
                if mes_valor_precipitacion[1] != None and mes_valor_precipitacion[1] > mes_valor_major_precipitacion[1]:
                    mes_valor_major_precipitacion = mes_valor_precipitacion
                    nome_estacion_major_precipitacion = nome_estacion_precipitacion

            indice_values+=1

    print("\nRespuesta 3: ")
    print( f'La Estación {nome_estacion_major_humidad} es la más Humeda y ' ,end="")
    print( f'El mes es {mes_valor_major_humedad[0]} con humedad más alta {mes_valor_major_humedad[1]}')

    print( f'La Estación {nome_estacion_major_precipitacion} tiene major Precipitación ',end="")
    print( f'El mes es {mes_valor_major_precipitacion[0]} con Precipitacion mál alta {mes_valor_major_precipitacion[1]}')

#4) Temperatura promedio durante todo el año en Paraná
def preguntaCuatro():
    estacion: dict
    for estacion in estadisticas:
        is_parana=False
        indice_values = 0
        for v in estacion.values():
            #Estación Paraná
            if(indice_values==0 and v=="PARANÁ AERO"):
                is_parana=True
            # Temperatura média mensual (°C) indice_value=1
            if is_parana and indice_values==1:
                temperatura_media = mediaValores(v)
                break
            indice_values+=1

        #despues de encontrar Paraná no necesita continuar la busca
        if is_parana:
            break

    print("\nRespuesta 4: \n    Média Anual de la Temperatura en Parará:  " + str(temperatura_media) )



preguntaTres()
preguntaCuatro()
