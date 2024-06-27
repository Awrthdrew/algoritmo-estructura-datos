import data
datas = data.data

nombre_id = []

for x in range(len(datas["body"]["dimensions"][0]["members"])):
    nombre_id.append(datas["body"]["dimensions"][0]["members"][x]["id"])
    nombre_id.append(datas["body"]["dimensions"][0]["members"][x]["name"])


anio_id = []

for x in range(len(datas["body"]["dimensions"][1]["members"])):
    anio_id.append(datas["body"]["dimensions"][1]["members"][x]["id"])
    anio_id.append(datas["body"]["dimensions"][1]["members"][x]["name"])




for x in range(len(datas["body"]["dimensions"][0]["members"])):
    print("Nombre del pais: " + str(datas["body"]["dimensions"][0]["members"][x]["name"]))
    print("Id del pais: " + str(datas["body"]["dimensions"][0]["members"][x]["id"]))




def prueba(nombre_id, anio_id):
    aux = 0
    consumo_total = 0
    count = 0
    opcion = (int)(input("Elija el id del pais que desea elejir: "))

    for x in range(len(nombre_id)):
        if nombre_id[x] == opcion:
            aux = nombre_id[x]
            print(str(datas["body"]["metadata"]["indicator_name"]) + " " + str(nombre_id[x + 1]))
    for x in range(len(datas["body"]["data"])):

            

        if aux == datas["body"]["data"][x]["dim_208"]:
            consumo_total += float(datas["body"]["data"][x]["value"])
            count += 1
            print("")
            print(datas["body"]["data"][x]["value"])
            for y in range(len(anio_id)):

                if anio_id[y] == datas["body"]["data"][x]["dim_29117"]:
                    print(anio_id[y + 1])


    print("Consumo total del Pais: ")
    print(round(consumo_total / count, 2))
        

prueba(nombre_id, anio_id)
