import Parcial
data = Parcial.data

def buscar_id(a, b):
    valores = 0
    id_pais = 0
    dic = []
    if a == 'data':
        #print(b)
        for x in b:
            for q, w in x.items():
                if q == 'value':
                    valores =  w
                if q == 'dim_208':
                    id_pais = w
            dic.append(
                {'Consumo': valores, 'Id_pais': id_pais}
                )
            #print(str(valores), str(id_pais))
            """
        for e in dic:
            for t, y in e.items():
                #print(t, y)

                    



def recorrer(data):
    id_pais = 0
    nombre_pais = ""
    for key, valor in data.items(): #recorre el array entero

        if key == 'body':

            for a, b in valor.items(): # a toma el valor de los principales, uno siendo data

                if a == 'dimensions': #Se entra al valor de data y sacamos la lista de adentro

                    for x, i in b[0].items():

                        if x == 'members':
                            for t in i:
                                #print(t)
                                for q, w in t.items():
                                    
                                    if q == 'name':
                                        nombre_pais = w
                                    if q == 'id':
                                        id_pais = w
                                #print("El nombre del pais es: " + nombre_pais + ", El id es: " + str(id_pais))
                buscar_id(a,b)

recorrer(data)
"""
def recorrido(data):
    info = []
    anos = []
    valor = []
    pls = 0
    si = 0
    nombre_pais = ''
    id_pais = ''
    id_parent = 0
    ano = 0
    p = 0
    for x in range(len(data["body"]["dimensions"][0]["members"])):
        for i, o in data["body"]["dimensions"][0]["members"][x].items():
            if i == 'name':
                nombre_pais = o
            if i == 'id':
                id_pais = o
        info.append(
            {'Nombre:': nombre_pais, 'pais': id_pais}
        )
        for k in info:
            for l, j in k.items():
                print(l,j)



    for x in range(len(data["body"]["dimensions"][1]["members"])):
        for i, o in data["body"]["dimensions"][1]["members"][x].items():
            if i == 'id':
                id_parent = o
            if i == 'name':
                ano = o
        anos.append(
            {'Id': id_parent, 'Anio': ano}
        )

    for x in range(len(data["body"]["data"])):
        for i, o in data["body"]["data"][x].items():
            if i == 'value':
                pls = o
            if i == 'dim_208':
                si = o
        valor.append(
            {'consumo': o, 'id': si}
        )


recorrido(data)


                   
                        
                           


      

 
                         


#opcion = (int)(input("De que pais desea conocer: "))


