class Pais:
    provincias = []#list para contener objetos de clase Provincia
    nombre = ""
    def __init__(self, p):
        self.provincias = p
        self.nombre = "Argentina"

    #Devuelve todos: varones + mujeres
    def get_total_poblacion(self):
        total = 0
        for p in self.provincias:
            total = total + p.get_total_poblacion_provincia()
        return total

    #Devuelte el objeto Provincia por el cod recibido
    def get_provincia(self, cod_provincia):
        p = None
        for x in self.provincias:
            if(x.get_cod() == cod_provincia):
                p = x
                break
        return p

    #PARA HACER :) ************************************************************
    def get_totales_poblacion(self):
        total = 0
        hombres = 0
        mujeres = 0
        for x in self.provincias:

            total = total + x.get_total_poblacion_provincia()
            hombres = hombres + x.get_total_varones()
            mujeres = mujeres + x.get_total_mujeres()

        print("La pobracion total de Argentina es: " + str(total) + "\n" + "El total de hombres es de: " + str(hombres) + "\n" + "El total de mujeres es de: " + str(mujeres))

    def get_viviendas(self): # Se ordenan los valores usando el metodo "Insertion Sort"
        array_total = []
        provincias = []
        for x in self.provincias:
            total = 0
            provincias.append(x.get_nombre())
            nombre_vivienda, cantidad_vivienda = x.get_viviendas()
            for y in cantidad_vivienda:
                total = total + y
            array_total.append(x.get_total_poblacion_provincia() / total)

        for step in range(1, len(array_total)):
            key = array_total[step]
            key_nom = provincias[step]
            j = step - 1

            while j >= 0 and key > array_total[j]:
                array_total[j + 1] = array_total[j]
                provincias[j + 1] = provincias[j]
                j = j - 1

            array_total[j + 1] = key
            provincias[j + 1] = key_nom
        
        for z in range(len(array_total)):
            print("La provincia de: " + str(provincias[z]) + " Tiene un promedio de: " + str(round(array_total[z], 4)) + " Personas por vivienda")


            
   #-----------------------------------------------------------------------------
   

    def mostrar_porcentaje_analfabetismo_por_sexo(self):
        hombres = 0
        mujeres = 0
        mujeres_ana = 0
        hombres_ana = 0
        for x in self.provincias:
            hombres = hombres + x.get_total_varones()
            mujeres = mujeres + x.get_total_mujeres()
            hombres_ana = hombres_ana + x.get_analfabetismo_varones()
            mujeres_ana = mujeres_ana + x.get_analfabetismo_mujeres()

        print("El porcentaje de analfabetos del sexo femenino es de: " + str(round(mujeres_ana / mujeres, 4) * 100) + "%") #Por alguna razon el raund aveces no funcina
        print("El porcentaje de analfabetos del sexo masculino es de: " + str(round(hombres_ana / hombres, 4) * 100) + "%" + "\n")


    def mostrar_porcentaje_analfabetismo_por_provincia(self):
        array_porcentaje_analfabetos = []
        array_nombre_provincias = []
        for x in self.provincias:
            total_analfabetos = x.get_analfabetismo_mujeres() + x.get_analfabetismo_varones()
            porcentaje_analfabetos = total_analfabetos / x.get_total_poblacion_provincia()
            array_nombre_provincias.append(x.get_nombre())
            array_porcentaje_analfabetos.append(porcentaje_analfabetos)

        for step in range(1, len(array_porcentaje_analfabetos)):
            key = array_porcentaje_analfabetos[step]
            key_nom = array_nombre_provincias[step]
            j = step - 1

            while j >= 0 and key > array_porcentaje_analfabetos[j]:
                array_porcentaje_analfabetos[j + 1] = array_porcentaje_analfabetos[j]
                array_nombre_provincias[j + 1] = array_nombre_provincias[j]
                j = j - 1

            array_porcentaje_analfabetos[j + 1] = key
            array_nombre_provincias[j + 1] = key_nom
        for y in range(len(array_porcentaje_analfabetos)):
            print("Nombre de la provincia: " + str(array_nombre_provincias[y]) + "," + " Porcentaje de analfabetos: " + str(round(array_porcentaje_analfabetos[y] * 100, 4)) + "%" )

            
    def mostrar_porcentaje_vivendas_sin_retrete_por_provincia(self):
        array_nombre_provincias = []
        array_porcentaje_retrete = []
        for x in self.provincias:

            # porcentaje_retrete = x.get_sin_retrete() / x.get_total_poblacion_provincia()
            array_nombre_provincias.append(x.get_nombre())
            array_porcentaje_retrete.append(x.get_sin_retrete() / x.get_total_viviendas())

        for step in range(1, len(array_porcentaje_retrete)):
            key = array_porcentaje_retrete[step]
            key_nom = array_nombre_provincias[step]
            j = step - 1

            while j >= 0 and key > array_porcentaje_retrete[j]:
                array_porcentaje_retrete[j + 1] = array_porcentaje_retrete[j]
                array_nombre_provincias[j + 1] = array_nombre_provincias[j]
                j = j - 1

            array_porcentaje_retrete[j + 1] = key
            array_nombre_provincias[j + 1] = key_nom
        for y in range(len(array_porcentaje_retrete)):
            print("Nombre de la provincia: " + str(array_nombre_provincias[y]) + "," + " Porcentaje de casas sin retrete: " + str(round(array_porcentaje_retrete[y] * 100, 4)) + "%" )


    def mostrar_porcentaje_vivienda_precaria_por_provincia(self):
        array_total_provincia = []
        array_nombre_provincias = []
        for x in self.provincias:
            total_provincia = 0

            array_nombre_vivienda, array_numero_precario = x.get_viviendas_sin_cd()

            for z in range(len(array_numero_precario)):
                total_provincia = total_provincia + array_numero_precario[z]
            array_nombre_provincias.append(x.get_nombre())
            array_total_provincia.append(((x.get_total_poblacion_provincia() / x.get_total_viviendas()) * total_provincia) / x.get_total_poblacion_provincia())

        for step in range(1, len(array_total_provincia)):
            key = array_total_provincia[step]
            key_nom = array_nombre_provincias[step]
            j = step - 1

            while j >= 0 and key > array_total_provincia[j]:
                array_total_provincia[j + 1] = array_total_provincia[j]
                array_nombre_provincias[j + 1] = array_nombre_provincias[j]
                j = j - 1

            array_total_provincia[j + 1] = key
            array_nombre_provincias[j + 1] = key_nom
        for y in range(len(array_total_provincia)):
            print("Nombre de la provincia: " + str(array_nombre_provincias[y]) + "," + " Porcentaje de gente en casas precarias: " + str(round(array_total_provincia[y] * 100, 4)) + "%" )


    """
        Se quiere saber si hay una correlacion entre las variables: analfabetismos vs
        viviendas precarias y sin retrete. Por ello hacer:
        1) Ordenar la lista de provincias segun el % de analfabetismos de forma
        ascendente. Esto nos da una pendiente positiva.
        2) Calcular la pendiente de la regresion lineal para las variables 
        "viviendas precarias" y para "sin retetre" y compare:
        ¿Como es el signo de la pendiente de estas dos variables comparado con
        el signo de la pendientes del % de alfabetismo?
        ¿Que se puede concluir?
    """
    def mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete(self):
#-------------------------------------------------------Precarias-----------------------------------------------------------------
        array_total_provincia = []
        nombre_provincias_precarias_retrete = []
        array_porcentaje_retrete = []
        for x in self.provincias:
            total_provincia = 0
            array_nombre_vivienda, array_numero_precario = x.get_viviendas_sin_cd()

            for z in range(len(array_numero_precario)):
                total_provincia = total_provincia + array_numero_precario[z]
            array_total_provincia.append((((x.get_total_poblacion_provincia() / x.get_total_viviendas()) * total_provincia) / x.get_total_poblacion_provincia()) * 100)

#-------------------------------------------------------sin retrete-----------------------------------------------------------------


        for x in self.provincias:
            # porcentaje_retrete = x.get_sin_retrete() / x.get_total_poblacion_provincia()
            nombre_provincias_precarias_retrete.append(x.get_nombre())
            array_porcentaje_retrete.append((x.get_sin_retrete() / x.get_total_viviendas()) * 100)

        sumatoria_xy = 0
        sumatoria_x = 0
        sumatoria_y = 0
        sumatoria_x_sqr = 0
        array_porcentaje_analfabetos = []
        array_nombre_provincias = []

#------------------------------------------------------Ordenacion basado en analfabetismo-------------------------------------------------------------------

        for x in self.provincias:
            total_analfabetos = x.get_analfabetismo_mujeres() + x.get_analfabetismo_varones()
            porcentaje_analfabetos = total_analfabetos / x.get_total_poblacion_provincia()
            array_nombre_provincias.append(x.get_nombre())
            array_porcentaje_analfabetos.append(porcentaje_analfabetos * 100)

        for step in range(1, len(array_porcentaje_analfabetos)):
            key = array_porcentaje_analfabetos[step]
            key_nom = array_nombre_provincias[step]
            key_ana = array_total_provincia[step]
            key_ret = array_porcentaje_retrete[step]
            j = step - 1

            while j >= 0 and key < array_porcentaje_analfabetos[j]:
                array_porcentaje_analfabetos[j + 1] = array_porcentaje_analfabetos[j]
                array_nombre_provincias[j + 1] = array_nombre_provincias[j]
                array_total_provincia[j + 1] = array_total_provincia[j]
                array_porcentaje_retrete[j + 1] = array_porcentaje_retrete[j]
                j = j - 1

            array_porcentaje_analfabetos[j + 1] = key
            array_nombre_provincias[j + 1] = key_nom
            array_total_provincia[j + 1] = key_ana
            array_porcentaje_retrete[j + 1] = key_ret
#---------------------------------------------------------------Sumatoria---------------------------------------------------------------------------
        for x in range(len(array_nombre_provincias)):
            sumatoria_xy = sumatoria_xy + array_porcentaje_analfabetos[x] * array_total_provincia[x]
        
        for x in range(len(array_nombre_provincias)):
            sumatoria_x = sumatoria_x + array_porcentaje_analfabetos[x]

        for x in range(len(array_nombre_provincias)):
            sumatoria_y = sumatoria_y + array_total_provincia[x]

        for x in range(len(array_nombre_provincias)):
            sumatoria_x_sqr = sumatoria_x_sqr + (array_porcentaje_analfabetos[x])**2

        
        pendiente = ((len(array_nombre_provincias) * sumatoria_xy - (sumatoria_x * sumatoria_y)) / (len(array_nombre_provincias) * sumatoria_x_sqr - sumatoria_x **2))


        print("pendiente de la regresion lineal de viviendas precarias y analfabetismo = " + str(pendiente))

        # for y in range(len(array_porcentaje_analfabetos)):
        #     print("Nombre de la provincia: " + str(array_nombre_provincias[y]) + "," + " Porcentaje de analfabetos: " + str(round(array_porcentaje_analfabetos[y], 4)) + "%")
        #     print("Nombre de la provincia: " + str(nombre_provincias_precarias_retrete[y]) + "," + " retrete: " + str(array_porcentaje_retrete[y]) + "%" + " " + str(array_total_provincia[y]))
        # print("\n")

        for x in range(len(array_nombre_provincias)):
            sumatoria_xy = sumatoria_xy + array_porcentaje_analfabetos[x] * array_porcentaje_retrete[x]
        
        for x in range(len(array_nombre_provincias)):
            sumatoria_x = sumatoria_x + array_porcentaje_analfabetos[x]

        for x in range(len(array_nombre_provincias)):
            sumatoria_y = sumatoria_y + array_porcentaje_retrete[x]

        for x in range(len(array_nombre_provincias)):
            sumatoria_x_sqr = sumatoria_x_sqr + (array_porcentaje_analfabetos[x])**2

        
        pendiente2 = ((len(array_nombre_provincias) * sumatoria_xy - (sumatoria_x * sumatoria_y)) / (len(array_nombre_provincias) * sumatoria_x_sqr - sumatoria_x **2))

        print("pendiente de la regresion lineal de retretes por provincia y analfabetismo = " + str(pendiente2))



#---------------------------------------------------------------------------------------------------------------------------------------------------#
class Provincia:
    cod = None
    nombre = None
    alfabetismo = None #para contener un objeto de la clase Alfabetismo
    sanitario = None #para contener un objeto de la clase Sanitario
    viviendas = [] #list para contener todos los tipos de viviendas
    def __init__(self, c, n, a, r, v):
        self.cod = c
        self.nombre = n
        self.alfabetismo = a
        self.sanitario = r
        self.viviendas = v

    #Devuelve todos: varones más mujeres
    def get_total_poblacion_provincia(self):
        return self.alfabetismo.get_total()
    
    def get_total_mujeres(self):
        return self.alfabetismo.get_total_mujeres()
    
    def get_total_varones(self):
        return self.alfabetismo.get_total_varones()
        
    def get_cod(self):
        return self.cod
    
    def get_nombre(self):
        return self.nombre
    
    def get_viviendas(self):
        nombre_vivienda = []
        cantidad_vivienda = []
        for x in self.viviendas:
            nombre_vivienda.append(x.get_nombre_vivienda())
            cantidad_vivienda.append(x.get_cantidad_vivienda())
        return nombre_vivienda, cantidad_vivienda
    
    def get_total_viviendas(self):
        total = 0
        for x in self.viviendas:
            total = total + x.get_cantidad_vivienda()
        return total
    
    def get_viviendas_sin_cd(self):
        nombre_vivienda = []
        cantidad_vivienda = []
        for x in self.viviendas:
            nombre_vivienda.append(x.get_nombre_vivienda_sin_cd())
            cantidad_vivienda.append(x.get_cantidad_vivienda_sin_cd())
        return nombre_vivienda, cantidad_vivienda
    
    def get_analfabetismo_mujeres(self):
        return self.alfabetismo.get_total_analfabetos_mujeres()
    
    def get_analfabetismo_varones(self):
        return self.alfabetismo.get_total_analfabetos_varones()
    
    def get_alfabetismo_mujeres(self):
        return self.alfabetismo.get_total_alfabetos_mujeres()
    
    def get_alfabetismo_varones(self):
        return self.alfabetismo.get_total_alfabetos_varones()
    
    def get_con_retrete(self):
        return self.sanitario.get_con_retrete()
    
    def get_sin_retrete(self):
        return self.sanitario.get_sin_retrete()

                


class PorSexo:
    varones = None
    mujeres = None
    def __init__(self, v, m):
        self.varones = v
        self.mujeres = m
   
    #Devuelve todos: varones más mujeres
    def get_total_sexo(self):
        return self.varones + self.mujeres
    
    def get_total_varones(self):
        return self.varones
    
    def get_total_mujeres(self):
        return self.mujeres


class Alfabetismo:
    alfabetos = None #para contener un objeto de clase PorSexo con datos de la personas alfabetas
    analfabetos = None #para contener un objeto de clase PorSexo con datos de la personas analfabetas    
    def __init__(self, a, no_a):
        self.alfabetos = a
        self.analfabetos = no_a

    #Total de la población: alfabetas + analfabetas
    def get_total(self):
        return self.alfabetos.get_total_sexo() + self.analfabetos.get_total_sexo()
    
    def get_total_varones(self):
        return self.alfabetos.get_total_varones() + self.analfabetos.get_total_varones()
    
    def get_total_mujeres(self):
        return self.alfabetos.get_total_mujeres() + self.analfabetos.get_total_mujeres()
    
    def get_total_analfabetos_varones(self):
        return self.analfabetos.get_total_varones()
    
    def get_total_analfabetos_mujeres(self):
        return self.analfabetos.get_total_mujeres()
    
    def get_total_alfabetos_varones(self):
        return self.alfabetos.get_total_varones()
    
    def get_total_alfabetos_mujeres(self):
        return self.alfabetos.get_total_mujeres()




class Sanitario:
    con_retrete = None
    sin_retrete = None
    def __init__(self, c, s):
        self.con_retrete = c
        self.sin_retrete = s

    def get_con_retrete(self):
        return self.con_retrete
    
    def get_sin_retrete(self):
        return self.sin_retrete



class Vivienda:
   
    tipo = None
    cantidad = None
    def __init__(self, t, c):
        self.tipo = t
        self.cantidad = c

    def get_nombre_vivienda(self):
        tipo_vivienda = {
        0: "Casa",
        1: "Rancho",
        2: "Casilla",
        3: "Departamento",
        4: "Pieza/s en inquilinato", 
        5: "Pieza/s en hotel o pensión", 
        6: "Local no construido para habitación", 
        7: "Vivienda móbil"
    } 
        
        nombre_vivienda = ""
        for key, value in tipo_vivienda.items():
            if self.tipo == key:
                nombre_vivienda = value
        
        return nombre_vivienda
    
    def get_nombre_vivienda_sin_cd(self):
        tipo_vivienda = {
        1: "Rancho",
        2: "Casilla",
        4: "Pieza/s en inquilinato", 
        5: "Pieza/s en hotel o pensión", 
        6: "Local no construido para habitación", 
        7: "Vivienda móbil"
    } 
        
        nombre_vivienda = ""
        for key, value in tipo_vivienda.items():
            if self.tipo == key:
                nombre_vivienda = value
        
        return nombre_vivienda
    
    def get_cantidad_vivienda(self):
        return self.cantidad
    
    def get_cantidad_vivienda_sin_cd(self):
        if self.tipo != 0 and self.tipo != 3:
            return self.cantidad
        else:
            return 0


#Fuente de datos: https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-135

arg = Pais([
    Provincia(0, 'Ciudad Autónoma de Buenos Aires', Alfabetismo(PorSexo(1160483, 1395255), PorSexo(5344, 7059)), Sanitario(1061211, 21787), [Vivienda(0, 252771), Vivienda(1, 565), Vivienda(2, 1884), Vivienda(3, 788791), Vivienda(4, 19571), Vivienda(5, 17082), Vivienda(6, 2237), Vivienda(7, 97)]),
    Provincia(1, '24 partidos del Gran Buenos Aires', Alfabetismo(PorSexo(3917957, 4223950), PorSexo(55416, 61809)), Sanitario(2294650, 358638), [Vivienda(0, 2212645), Vivienda(1, 17794), Vivienda(2, 73827), Vivienda(3, 329731), Vivienda(4, 12452), Vivienda(5, 1405), Vivienda(6, 5091), Vivienda(7, 343)]),
    Provincia(2, 'Interior de la provincia de Buenos Aires', Alfabetismo(PorSexo(2285525, 2438254), PorSexo(33289, 28494)), Sanitario(1625106, 146799), [Vivienda(0, 1502191), Vivienda(1, 12283), Vivienda(2, 35724), Vivienda(3, 212714), Vivienda(4, 4117), Vivienda(5, 817), Vivienda(6, 3026), Vivienda(7, 1033)]),
    Provincia(3, 'Catamarca', Alfabetismo(PorSexo(144528, 148625), PorSexo(3108, 2928)), Sanitario(75871, 13505), [Vivienda(0, 83578), Vivienda(1, 2134), Vivienda(2, 400), Vivienda(3, 2666), Vivienda(4, 427), Vivienda(5, 30), Vivienda(6, 96), Vivienda(7, 45)]),
    Provincia(4, 'Chaco', Alfabetismo(PorSexo(394795, 411225), PorSexo(22440, 24292)), Sanitario(916669, 61884), [Vivienda(0, 236946), Vivienda(1, 12558), Vivienda(2, 5696), Vivienda(3, 12052), Vivienda(4, 2048), Vivienda(5, 165), Vivienda(6, 424), Vivienda(7, 244)]),
    Provincia(5, 'Chubut', Alfabetismo(PorSexo(205779, 206044), PorSexo(4049, 4265)), Sanitario(197102, 51742), [Vivienda(0, 122955), Vivienda(1, 1479), Vivienda(2, 1917), Vivienda(3, 19318), Vivienda(4, 1068), Vivienda(5, 58), Vivienda(6, 237), Vivienda(7, 144)]),
    Provincia(6, 'Córdoba', Alfabetismo(PorSexo(1314229, 1425717), PorSexo(22334, 18451)), Sanitario(176147, 93986), [Vivienda(0, 840488), Vivienda(1, 5929), Vivienda(2, 2775), Vivienda(3, 124044), Vivienda(4, 2852), Vivienda(5, 791), Vivienda(6, 1199), Vivienda(7, 475)]),
    Provincia(7, 'Corrientes', Alfabetismo(PorSexo(372493, 399455), PorSexo(17969, 16523)), Sanitario(136043, 11133), [Vivienda(0, 210288), Vivienda(1, 13056), Vivienda(2, 8147), Vivienda(3, 14201), Vivienda(4, 2293), Vivienda(5, 236), Vivienda(6, 393), Vivienda(7, 230)]),
    Provincia(8, 'Entre Ríos', Alfabetismo(PorSexo(486281, 519080), PorSexo(12294, 9610)), Sanitario(326978, 30272), [Vivienda(0, 317956), Vivienda(1, 3805), Vivienda(2, 7273), Vivienda(3, 26680), Vivienda(4, 644), Vivienda(5, 176), Vivienda(6, 495), Vivienda(7, 221)]),
    Provincia(9, 'Formosa', Alfabetismo(PorSexo(200956, 206992), PorSexo(7821, 9575)), Sanitario(79122, 51012), [Vivienda(0, 109807), Vivienda(1, 12203), Vivienda(2, 1514), Vivienda(3, 4124), Vivienda(4, 2104), Vivienda(5, 44), Vivienda(6, 229), Vivienda(7, 109)]),
    Provincia(10, 'Jujuy', Alfabetismo(PorSexo(261419, 269965), PorSexo(5404, 11784)), Sanitario(122201, 32710), [Vivienda(0, 134293), Vivienda(1, 7286), Vivienda(2, 2595), Vivienda(3, 7824), Vivienda(4, 2510), Vivienda(5, 74), Vivienda(6, 245), Vivienda(7, 84)]),
    Provincia(11, 'La Pampa', Alfabetismo(PorSexo(128679, 133208), PorSexo(2805, 2227)), Sanitario(101706, 3091), [Vivienda(0, 95356), Vivienda(1, 458), Vivienda(2, 169), Vivienda(3, 8239), Vivienda(4, 317), Vivienda(5, 10), Vivienda(6, 177), Vivienda(7, 71)]),
    Provincia(12, 'La Rioja', Alfabetismo(PorSexo(131833, 136616), PorSexo(2843, 2154)), Sanitario(75564, 10803), [Vivienda(0, 77743), Vivienda(1, 1970), Vivienda(2, 1643), Vivienda(3, 4208), Vivienda(4, 597), Vivienda(5, 56), Vivienda(6, 105), Vivienda(7, 45)]),
    Provincia(13, 'Mendoza', Alfabetismo(PorSexo(681053, 730907), PorSexo(15527, 16003)), Sanitario(421292, 38258), [Vivienda(0, 398510), Vivienda(1, 7618), Vivienda(2, 1985), Vivienda(3, 48846), Vivienda(4, 1686), Vivienda(5, 216), Vivienda(6, 595), Vivienda(7, 94)]),
    Provincia(14, 'Misiones', Alfabetismo(PorSexo(412901, 422882), PorSexo(17110, 18662)), Sanitario(201604, 88659), [Vivienda(0, 249745), Vivienda(1, 7866), Vivienda(2, 11548), Vivienda(3, 16938), Vivienda(4, 3376), Vivienda(5, 77), Vivienda(6, 560), Vivienda(7, 153)]),
    Provincia(15, 'Neuquén', Alfabetismo(PorSexo(219539, 225070), PorSexo(5120, 5339)), Sanitario(145697, 13605), [Vivienda(0, 130466), Vivienda(1, 1924), Vivienda(2, 3425), Vivienda(3, 21312), Vivienda(4, 1743), Vivienda(5, 83), Vivienda(6, 228), Vivienda(7, 121)]),
    Provincia(16, 'Río Negro', Alfabetismo(PorSexo(255390, 262917), PorSexo(6541, 6539)), Sanitario(171370, 19227), [Vivienda(0, 155561), Vivienda(1, 2149), Vivienda(2, 4091), Vivienda(3, 27071), Vivienda(4, 1230), Vivienda(5, 72), Vivienda(6, 331), Vivienda(7, 92)]),
    Provincia(17, 'Salta', Alfabetismo(PorSexo(459258, 478751), PorSexo(12710, 17657)), Sanitario(202113, 64962), [Vivienda(0, 220293), Vivienda(1, 14806), Vivienda(2, 11076), Vivienda(3, 17161), Vivienda(4, 2881), Vivienda(5, 120), Vivienda(6, 450), Vivienda(7, 288)]),
    Provincia(18, 'San Juan', Alfabetismo(PorSexo(260076, 278149), PorSexo(6360, 5133)), Sanitario(142970, 19234), [Vivienda(0, 134753), Vivienda(1, 11219), Vivienda(2, 1075), Vivienda(3, 14489), Vivienda(4, 405), Vivienda(5, 43), Vivienda(6, 196), Vivienda(7, 24)]),
    Provincia(19, 'San Luis', Alfabetismo(PorSexo(170030, 177358), PorSexo(3674, 2838)), Sanitario(108089, 9677), [Vivienda(0, 104692), Vivienda(1, 1125), Vivienda(2, 470), Vivienda(3, 10380), Vivienda(4, 654), Vivienda(5, 106), Vivienda(6, 208), Vivienda(7, 131)]),
    Provincia(20, 'Santa Cruz', Alfabetismo(PorSexo(113297, 106023), PorSexo(1291, 1213)), Sanitario(72841, 3392), [Vivienda(0, 64118), Vivienda(1, 524), Vivienda(2, 852), Vivienda(3, 9339), Vivienda(4, 1181), Vivienda(5, 43), Vivienda(6, 118), Vivienda(7, 58)]),
    Provincia(21, 'Santa Fe', Alfabetismo(PorSexo(1273525, 1383361), PorSexo(25003, 23092)), Sanitario(862253, 86116), [Vivienda(0, 793209), Vivienda(1, 10303), Vivienda(2, 8279), Vivienda(3, 132409), Vivienda(4, 2023), Vivienda(5, 796), Vivienda(6, 1119), Vivienda(7, 231)]),
    Provincia(22, 'Santiago del Estero', Alfabetismo(PorSexo(328348, 340598), PorSexo(14809, 13061)), Sanitario(122529, 75377), [Vivienda(0, 169162), Vivienda(1, 20833), Vivienda(2, 1097), Vivienda(3, 5830), Vivienda(4, 463), Vivienda(5, 75), Vivienda(6, 223), Vivienda(7, 223)]),
    Provincia(23, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur', Alfabetismo(PorSexo(52991, 50430), PorSexo(347, 358)), Sanitario(35041, 1648), [Vivienda(0, 25108), Vivienda(1, 102), Vivienda(2, 3817), Vivienda(3, 7326), Vivienda(4, 226), Vivienda(5, 43), Vivienda(6, 44), Vivienda(7, 23)]),
    Provincia(24, 'Tucumán', Alfabetismo(PorSexo(557210, 596990), PorSexo(15859, 13295)), Sanitario(276897, 58924), [Vivienda(0, 287900), Vivienda(1, 4931), Vivienda(2, 11031), Vivienda(3, 30431), Vivienda(4, 897), Vivienda(5, 184), Vivienda(6, 344), Vivienda(7, 103)])
])
opcion = 100
print("1. Mostrar el total de la poblacion")
print("2. Mostrar ratio de habitantes por provincia")
print("3. Mostrar el porcentaje de analfabetismo por sexo")
print("4. Mostrar la provincia y el porcentaje de analfabetos")
print("5. Mostrar porvincia y el procentaje de viviendas sin retrete")
print("6. Mostrar el nombre de la provincia y el porcentaje de los que viven en una casa precaria")
print("7. Mostrar la correlacion de analfabetismo vs vivienda y retrete")
print("0. Para salir ")
while opcion != 0:
    opcion = (int)(input(("Que desea hacer Hoy:")))
    if opcion == 1:
        print("--" * 50 + "--" * 50)
        print(arg.get_totales_poblacion())
    if opcion == 2:
        print("--" * 50 + "--" * 50)
        print(arg.get_viviendas())  
    if opcion == 3:
        print("--" * 50 + "--" * 50)
        print(arg.mostrar_porcentaje_analfabetismo_por_sexo())
        
    if opcion == 4:
        print("--" * 50 + "--" * 50)
        print(arg.mostrar_porcentaje_analfabetismo_por_provincia())
        
    if opcion == 5:
        print("--" * 50 + "--" * 50)
        print(arg.mostrar_porcentaje_vivendas_sin_retrete_por_provincia())

    if opcion == 6:
        print("--" * 50 + "--" * 50)
        print(arg.mostrar_porcentaje_vivienda_precaria_por_provincia())
    
    if opcion == 7:
        print(arg.mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete())
"""
La correlacion que puedo ver entre el analfabetismo y vivienda y retriete es que cuentas mas viviendas sin retrete se encuentran, y mas viviendfas precarias, el analfabetismo
aumenta, honestamente la ecuacion no estoy al 100% seguro que esta bien pero hice lo que entendi y entendimos con los chicos.
"""