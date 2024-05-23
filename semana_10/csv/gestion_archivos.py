import csv
import json

matriz = []

# AGREGAR R PARA QUE \ NO AFECTE A LOS CARACTERERS QUE ESTÉN AL LADO ⬇️ 
# ESTÁ EL ARCHIVO .csv QUE SE VA A LEER EN SU RUTA ABSOLUTA
with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\semana_10\csv\curso.csv', "r", encoding='utf8', newline="\n") as file: 
    line = None
    while line != '':
        # 1) PASARLO A MATRIZ
        line = file.readline().strip()
        print(line)
        if line != '':
            matriz_array = line.split("|")
            matriz.append(matriz_array)
#print(matriz)
            
#2) PROCESAR LISTA PARA AUMENTAR EL BONO DE LOS ALUMNOS EN UN 13%
def aumento_bono():
    for alumno in matriz:
        print(alumno [1] + ' | BONO ACTUAL: ' + alumno[3])
        alumno[3] = str(round(float(alumno[3]) * 1.13, 2))
        print(alumno [1] + ' | 13% ACTUALIZADO: ' + alumno[3])
        print()
        
aumento_bono()

#3) GUARDAR LA MATRIZ EN UN NUEVO ARCHIVO .CSV
r"""with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\semana_10\csv\bonos_actualizados.csv', 'w') as file:
    for alumno in matriz:
        file.write("|".join(map(str, alumno)) + "\n")"""

#4) CREAR DOS LISTAS PARA ALMACENAR ALUMNOS QUE GANAN < $10000 Y LOS QUE GANAN MÁS
bono_menor_10000 = []
resto_alumnos = []

for alumno in matriz:
    if float(alumno[3]) < 10000:
        bono_menor_10000.append(alumno)
    else:
        resto_alumnos.append(alumno)
        
# MÉTODO PARA GUARDAR ARCHIVOS CON LOS ALUMNOS QUE GANAN MENOS DE $10000 Y LOS QUE GANAN MÁS
with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\semana_10\csv\alumnosBonoMenor_10000.csv', 'w', encoding='utf8' ) as file:
    for alumno in bono_menor_10000:
        file.write("|".join(map(str, alumno)) + "\n")

with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\semana_10\csv\restoAlumnos.csv', 'w', encoding='utf8') as file:
    for alumno in resto_alumnos:
        file.write("|".join(map(str, alumno)) + "\n")



# IMPORTAR JSON CON OPEN Y .LOAD
provincias = []
with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\semana_10\localidades.json', 'r', encoding='utf8', newline="\n") as dict_localidades:
    data = json.load(dict_localidades)

    for local in data['localidades']:
        print(local['nombre'] + ' | ' + local['provincia']['nombre'])
        if local['provincia']['nombre'] not in provincias:
            provincias.append(local['provincia']['nombre'])
        else:
            continue
        
with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\semana_10\csv\Provincias.dump.json', 'w', encoding='utf8', newline="\n") as file:
    provincias.sort()
    json.dump(provincias, file, indent = 4, ensure_ascii= False)
    #HAY DOS MANERAS DE USAR JSON.DUMP O FILE.WRITE (.DUMPS) PARA GUARDAR EL ARCHIVO JSON | LA DIFERENCIA VIENE DEL FILE_POINTER Y COMO SE PARAMETRIZA EL ARCHIVO
    #file.write(json.dumps(provincias, indent = 4, ensure_ascii= False))
        