import random

# Constantes del problema
JORNADA_LABORAL_MINUTOS = 8 * 60
FRECUENCIA_INGRESO_MINUTOS = 10
PACIENCIA_MINUTOS_MIN = 5
PACIENCIA_MINUTOS_MAX = 15
TIEMPO_ATENCION_MIN = 3
TIEMPO_ATENCION_MAX = 10

# Variables del problema
cajas = [[]]  # Una lista de listas, una cola por cada caja
personas_atendidas = 0
personas_abandonaron = 0
tiempo_total_cajas = 0

def generador_persona():
    """Crea una persona para ingresar a la cola en un momento dado, con un grado
    de paciencia y un tiempo de atención determinado al azar."""
    grado_paciencia = random.randint(PACIENCIA_MINUTOS_MIN, PACIENCIA_MINUTOS_MAX)
    tiempo_atencion = random.randint(TIEMPO_ATENCION_MIN, TIEMPO_ATENCION_MAX)
    return {"grado_paciencia": grado_paciencia, "tiempo_esperando": 0,
            "tiempo_atencion": tiempo_atencion}

for minuto_actual in range(JORNADA_LABORAL_MINUTOS):
    # Generamos una persona para ingresar a la cola con una frecuencia promedio
    if minuto_actual % FRECUENCIA_INGRESO_MINUTOS == 0:
        nueva_persona = generador_persona()
        caja_con_menos_personas = min(range(len(cajas)), key=lambda i: len(cajas[i]))
        cajas[caja_con_menos_personas].append(nueva_persona)
    
    # Sacamos a las personas de las cajas que ya fueron atendidas
    for cola in cajas:
        if len(cola) > 0 and cola[0]["tiempo_atencion"] == 0:
            tiempo_total_cajas += cola[0]["tiempo_esperando"]
            cola.pop(0)
            personas_atendidas += 1
            
    # Sacamos a las personas que abandonaron la cola por exceder su paciencia
    for cola in cajas:
        for i, persona in enumerate(cola):
            persona["tiempo_esperando"] += 1
            if persona["tiempo_esperando"] > persona["grado_paciencia"]:
                cola.pop(i)
                personas_abandonaron += 1
    
    # Atendemos a la primera persona de cada cola, reduciendo su tiempo de atención
    for cola in cajas:
        if len(cola) > 0:
            cola[0]["tiempo_atencion"] -= 1

# Imprimimos los resultados finales
print("Cantidad de cajas:", len(cajas))
print("Cantidad de personas que abandonaron la compra:", personas_abandonaron)
print("Cantidad de personas atendidas:", personas_atendidas)
if personas_atendidas > 0:
    print("Promedio de tiempo en caja:", tiempo_total_cajas / personas_atendidas)
else:
    print("Promedio de tiempo en caja: 0")
