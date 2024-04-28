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
        return mostrar_totales_poblacion

    def mostrar_ratio_habitantes_por_vivienda_por_provincia(self):
        array = []
        for p in self.provincias:
            total_viviendas = p.get_total_viviendas()
            ratio = p.get_total_poblacion() / total_viviendas
            nombre = p.get_nombre()
            array.append(f"El ratio de habitantes por vivienda en {nombre} es de {ratio} por vivienda")
        return array

    def mostrar_porcentaje_analfabetismo_por_sexo(self):
        array = []
        for p in self.provincias:
            porcentaje_varones = (p.get_alfabetismo().get_total_varones_analfabetos() / p.get_alfabetismo().get_total_varones()) * 100
            porcentaje_mujeres = (p.get_alfabetismo().get_total_mujeres_analfabetas() / p.get_alfabetismo().get_total_mujeres()) * 100
            nombre = p.get_nombre()
            array.append(f"El porcentaje de varones analfabetos en {nombre} es de {porcentaje_varones}% y el porcentaje de mujeres analfabetas es de {porcentaje_mujeres}%")
        return array

    def mostrar_porcentaje_analfabetismo_por_provincia(self):
        array = []
        for p in self.provincias:
            porcentaje_analfabetos_por_provincia = (p.get_alfabetismo().get_total_varones_analfabetos() + p.get_alfabetismo().get_total_mujeres_analfabetas()) / (p.get_total_poblacion()) * 100
            nombre = p.get_nombre()
            array.append(f"{porcentaje_analfabetos_por_provincia}% es el porcentaje de analfabetismo en {nombre}")
        array.sort(reverse=True)
        return array

    def mostrar_porcentaje_viviendas_sin_retrete_por_provincia(self):
        array = []
        for p in self.provincias:
            viviendas = p.get_viviendas()
            total_viviendas = viviendas[0].get_total_viviendas()  # Obtenemos el total de viviendas en la primera posición de la lista
            total_viviendas_sin_retrete = viviendas[0].get_total_viviendas_sin_retrete()  # Obtenemos el total de viviendas sin retrete en la primera posición de la lista
            porcentaje_viviendas_sin_retrete_por_provincia = (total_viviendas_sin_retrete / total_viviendas) * 100
            array.append(f"{porcentaje_viviendas_sin_retrete_por_provincia}% de las viviendas en {p.get_nombre()} no tienen retrete")
        array.sort(reverse=True)
        return array

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
    def __init__(self, tmv, tmm, tva, tvm):
        self.total_mujeres_varones = tmv
        self.total_mujeres_mujeres = tmm
        self.total_varones_analfabetos = tva
        self.total_mujeres_analfabetas = tvm

    def get_total_varones(self):
        return self.total_mujeres_varones

    def get_total_mujeres(self):
        return self.total_mujeres_mujeres

    def get_total_varones_analfabetos(self):
        return self.total_varones_analfabetos

    def get_total_mujeres_analfabetas(self):
        return self.total_mujeres_analfabetas


# Carga de datos del Censo 2010 en Argentina
# Datos de la provincia de Buenos Aires
viviendas_buenos_aires = [Vivienda(5000000, 18000000, 8900000, 9100000, 1000000)]
alfabetismo_buenos_aires = Alfabetismo(18500000, 18500000, 2000000, 3000000)
buenos_aires = Provincia("02", "Buenos Aires", viviendas_buenos_aires, alfabetismo_buenos_aires)

# Datos de la provincia de Córdoba
viviendas_cordoba = [Vivienda(2500000, 8000000, 3900000, 4100000, 500000)]
alfabetismo_cordoba = Alfabetismo(8000000, 8000000, 800000, 900000)
cordoba = Provincia("14", "Córdoba", viviendas_cordoba, alfabetismo_cordoba)

# Datos de la provincia de Santa Fe
viviendas_santa_fe = [Vivienda(2200000, 6500000, 3100000, 3400000, 400000)]
alfabetismo_santa_fe = Alfabetismo(6500000, 6500000, 600000, 700000)
santa_fe = Provincia("21", "Santa Fe", viviendas_santa_fe, alfabetismo_santa_fe)

# Creación de la instancia del país y carga de provincias
argentina = Pais([buenos_aires, cordoba, santa_fe])

# Ejemplo de uso: Obtener el total de la población censada en Argentina
total_poblacion = argentina.get_total_poblacion()
mensaje_poblacion = argentina.mostrar_totales_poblacion()
for char in mensaje_poblacion:
    if char == " ":
        print(char, end="")
    else:
        print(char, end=" ")

# Ejemplo de uso: Mostrar el total de población por provincia
totales_poblacion_provincia = argentina.mostrar_totales_poblacion()
for total in totales_poblacion_provincia:
    print(total)

# Ejemplo de uso: Mostrar el ratio de habitantes por vivienda por provincia
ratio_habitantes_vivienda_provincia = argentina.mostrar_ratio_habitantes_por_vivienda_por_provincia()
for ratio in ratio_habitantes_vivienda_provincia:
    print(ratio)

# Ejemplo de uso: Mostrar el porcentaje de analfabetismo por sexo por provincia
porcentaje_analfabetismo_sexo_provincia = argentina.mostrar_porcentaje_analfabetismo_por_sexo()
for porcentaje in porcentaje_analfabetismo_sexo_provincia:
    print(porcentaje)

# Ejemplo de uso: Mostrar el porcentaje de analfabetismo por provincia
porcentaje_analfabetismo_provincia = argentina.mostrar_porcentaje_analfabetismo_por_provincia()
for porcentaje in porcentaje_analfabetismo_provincia:
    print(porcentaje)

# Ejemplo de uso: Mostrar el porcentaje de viviendas sin retrete por provincia
porcentaje_viviendas_sin_retrete_provincia = argentina.mostrar_porcentaje_viviendas_sin_retrete_por_provincia()
for porcentaje in porcentaje_viviendas_sin_retrete_provincia:
    print(porcentaje)