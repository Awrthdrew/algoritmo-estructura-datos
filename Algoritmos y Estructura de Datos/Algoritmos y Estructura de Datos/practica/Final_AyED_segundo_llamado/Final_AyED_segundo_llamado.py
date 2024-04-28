
    # Final AyED
    # 14/12/2022
    # Entregar el programa resuelto por email antes de las 11:30
    
    # Sistema de cálculo de estadísticas climatológicas
    # -------------------------------------------------
    # Objetivo general: construir un sistema de carga y cálculo de información
    # climática de ciudades del país.
    # El sistema deberá considerar:
    # 1) la información de la ciudad debe estar construida con objetos con los 
    #    siguientes datos: nombre de la ciudad, un promedio anual de temperatura,
    #    temperatura máxima y mínima registrada
    # 2) las ciudades (objeto) será almacenadas y gestionadas en un array
    # 3) cuando arranca el sistema debe haber al menos 3 ciudades instanciadas
    #    dentro del array
    # 4) el sistema debe permitir, en un ciclo infinito, la carga de otra nueva 
    #    ciudad y agregado al array
    # 5) cada vez que se incorpora una nueva ciudad, se debe recalcular y mostrar:
    #     a) el promedio de temperatura del país. (de las temp promedio de cada ciudad)
    #     b) la mediana de temperatura (del promedio anual de ciudad) del país. 
    #        (cantidad de datos pares: entonces se hace un promedio entre los 
    #        datos centrales)
    #     c) ciudad más calurosa (de la temp max.)
    #     d) ciudad más fria (de la temp min.)

class Ciudad:
    def __init__(self, nombre, temp_promedio, temp_max, temp_min):
        self.nombre = nombre
        self.temp_promedio = temp_promedio
        self.temp_max = temp_max
        self.temp_min = temp_min
    
    def getNombre(self):
        return self.nombre
    
    def getTempPromedio(self):
        return self.temp_promedio
    
    def getTempMax(self):
        return self.temp_max
    
    def getTempMin(self):
        return self.temp_min
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTempPromedio(self, temp_promedio):
        self.temp_promedio = temp_promedio
    
    def setTempMax(self, temp_max):
        self.temp_max = temp_max
    
    def setTempMin(self, temp_min):
        self.temp_min = temp_min
