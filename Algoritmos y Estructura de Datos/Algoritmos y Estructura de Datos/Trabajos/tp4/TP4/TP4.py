class Pais:
    def __init__(self, p):
        self.provincias = p
        self.nombre = "Argentina"

    def get_total_poblacion(self):
        total = 0
        for p in self.provincias:
            total += p.get_total_poblacion()
        return total

    def get_provincia(self, cod_provincia):
        for p in self.provincias:
            if p.get_cod() == cod_provincia:
                return p
        return None

    def mostrar_totales_poblacion(self):
        total = self.get_total_poblacion()
        total_masculino = 0
        total_femenino = 0
        for p in self.provincias:
            total_masculino += p.get_total_poblacion_masculina()
            total_femenino += p.get_total_poblacion_femenina()
        total_total = total_femenino + total_masculino
        mostrar_totales_poblacion = f"Argentina tiene una población total de {total}, de los cuales {total_femenino} son mujeres y {total_masculino} son varones. En total son {total_total}"
        print(mostrar_totales_poblacion)

    def mostrar_ratio_habitantes_por_vivienda_por_provincia(self):
        array = []
        for p in self.provincias:
            total_viviendas = p.get_total_viviendas()
            ratio = p.get_total_poblacion() / total_viviendas
            nombre = p.get_nombre()
            array.append(f"El ratio de habitantes por vivienda en {nombre} es de {ratio:.2f} por vivienda")
        for item in array:
            print(item)

    def mostrar_porcentaje_analfabetismo_por_sexo(self):
        array = []
        for p in self.provincias:
            porcentaje_varones = (p.get_alfabetismo().get_total_varones_analfabetos() / p.get_alfabetismo().get_total_varones()) * 100
            porcentaje_mujeres = (p.get_alfabetismo().get_total_mujeres_analfabetas() / p.get_alfabetismo().get_total_mujeres()) * 100
            nombre = p.get_nombre()
            array.append(f"El porcentaje de varones analfabetos en {nombre} es de {porcentaje_varones:.2f}% y el porcentaje de mujeres analfabetas es de {porcentaje_mujeres:.2f}%")
        for item in array:
            print(item)

    def mostrar_porcentaje_analfabetismo_por_provincia(self):
        array = []
        for p in self.provincias:
            porcentaje_analfabetos_por_provincia = (p.get_alfabetismo().get_total_varones_analfabetos() + p.get_alfabetismo().get_total_mujeres_analfabetas()) / (p.get_total_poblacion()) * 100
            nombre = p.get_nombre()
            array.append(f"{porcentaje_analfabetos_por_provincia:.2f}% es el porcentaje de analfabetismo en {nombre}")
        array.sort(reverse=True)
        for item in array:
            print(item)

    def mostrar_porcentaje_viviendas_sin_retrete_por_provincia(self):
        array = []
        for p in self.provincias:
            viviendas = p.get_viviendas()
            total_viviendas = viviendas[0].get_total_viviendas()
            viviendas_sin_retrete = viviendas[0].get_total_viviendas_sin_retrete()
            porcentaje_viviendas_sin_retrete = (viviendas_sin_retrete / total_viviendas) * 100
            nombre = p.get_nombre()
            array.append(f"El porcentaje de viviendas sin retrete en {nombre} es de {porcentaje_viviendas_sin_retrete:.2f}%")
        array.sort(reverse=True)
        for item in array:
            print(item)


class Provincia:
    def __init__(self, c, n, v, a):
        self.codigo = c
        self.nombre = n
        self.viviendas = v
        self.alfabetismo = a

    def get_cod(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_viviendas(self):
        return self.viviendas

    def get_alfabetismo(self):
        return self.alfabetismo

    def get_total_poblacion(self):
        total = 0
        for v in self.viviendas:
            total += v.get_poblacion()
        return total

    def get_total_poblacion_masculina(self):
        total = 0
        for v in self.viviendas:
            total += v.get_poblacion_masculina()
        return total

    def get_total_poblacion_femenina(self):
        total = 0
        for v in self.viviendas:
            total += v.get_poblacion_femenina()
        return total

    def get_total_viviendas(self):
        total = 0
        for v in self.viviendas:
            total += v.get_viviendas()
        return total


class Vivienda:
    def __init__(self, v, p, m, f, r):
        self.viviendas = v
        self.poblacion = p
        self.masculino = m
        self.femenino = f
        self.sin_retrete = r

    def get_viviendas(self):
        return self.viviendas

    def get_poblacion(self):
        return self.poblacion

    def get_poblacion_masculina(self):
        return self.masculino

    def get_poblacion_femenina(self):
        return self.femenino

    def get_total_viviendas_sin_retrete(self):
        return self.sin_retrete

    def get_total_viviendas(self):
        return self.viviendas


class Alfabetismo:
    def __init__(self, tv, tm, tva, tvm):
        self.total_varones = tv
        self.total_mujeres = tm
        self.total_varones_analfabetos = tva
        self.total_mujeres_analfabetas = tvm

    def get_total_varones(self):
        return self.total_varones

    def get_total_mujeres(self):
        return self.total_mujeres

    def get_total_varones_analfabetos(self):
        return self.total_varones_analfabetos

    def get_total_mujeres_analfabetas(self):
        return self.total_mujeres_analfabetas


# Carga de datos del Censo 2010 en Argentina
# Datos de la provincia de Buenos Aires
viviendas_buenos_aires = [Vivienda(1082998, 2555738, 1165827, 1402314, 21787)]
alfabetismo_buenos_aires = Alfabetismo(1165827, 1402314, 5344, 7059)
buenos_aires = Provincia("AR-B", "Buenos Aires", viviendas_buenos_aires, alfabetismo_buenos_aires)

# Datos de la provincia de Córdoba
viviendas_cordoba = [Vivienda(2500000, 2739946, 4100000, 4400000, 500000)]
alfabetismo_cordoba = Alfabetismo(5500000, 6000000, 500000, 600000)
cordoba = Provincia("AR-C", "Córdoba", viviendas_cordoba, alfabetismo_cordoba)

# Datos de la provincia de Santa Fe
viviendas_santa_fe = [Vivienda(2000000, 6500000, 3200000, 3300000, 400000)]
alfabetismo_santa_fe = Alfabetismo(4500000, 5000000, 300000, 400000)
santa_fe = Provincia("AR-S", "Santa Fe", viviendas_santa_fe, alfabetismo_santa_fe)

# Creación del objeto Pais
argentina = Pais([buenos_aires, cordoba, santa_fe])

# Llamadas a los métodos
argentina.mostrar_totales_poblacion()
argentina.mostrar_ratio_habitantes_por_vivienda_por_provincia()
argentina.mostrar_porcentaje_analfabetismo_por_sexo()
argentina.mostrar_porcentaje_analfabetismo_por_provincia()
argentina.mostrar_porcentaje_viviendas_sin_retrete_por_provincia()

