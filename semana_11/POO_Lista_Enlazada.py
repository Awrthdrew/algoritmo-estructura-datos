"""print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")"""

class Letra:
    def __init__(self, letra):
        self.letra = letra
        self.siguiente_letra = None
    
raiz = Letra("A")

raiz.siguiente_letra = Letra("B")

raiz.siguiente_letra.siguiente_letra = Letra("C")

def mostrar_lista(x):
    while x != None:
        print(x.letra) 
        x = x.siguiente_letra
        
#1.0 Agregar elemento al final de la lista
def agregar_elemento_final(letra):
    global raiz
    otra_raiz = raiz
    while otra_raiz.siguiente_letra != None:
        otra_raiz = otra_raiz.siguiente_letra
    otra_raiz.siguiente_letra = Letra(letra)

#1.1 Agregar elemento al principio de la lista    
def agregar_elemento_principio(letra):
    global raiz
    otra_raiz = Letra(letra)
    otra_raiz.siguiente_letra = raiz
    raiz = otra_raiz
    
#2.0 Sacar elemento al final de la lista
def sacar_elemento_final():
    global raiz
    otra_raiz = raiz
    while otra_raiz.siguiente_letra.siguiente_letra != None:
        otra_raiz = otra_raiz.siguiente_letra
    else:
        otra_raiz.siguiente_letra = None
    
#2.1 Sacar elemento al principio de la lista
def sacar_elemento_principio():
    global raiz
    raiz = raiz.siguiente_letra

#3.0 Agregar elemento en la posición x de la lista
def agregar_elemento_posicion(letra, posicion):
    global raiz
    r = raiz
    elemento = Letra(letra)
    
    if posicion == 0:
        elemento.siguiente_letra = raiz
        raiz = elemento
    else:
        for letra in range(posicion-1):
            r = r.siguiente_letra
        elemento.siguiente_letra = r.siguiente_letra
        r.siguiente_letra = elemento

#3.1 Sacar elemento en la posición x de la lista
def sacar_elemento_posicion(posicion):
    global raiz
    aux = raiz
    
    if posicion == 0:
        raiz = raiz.siguiente_letra
    else:
        for _ in range(posicion-1):
            aux = aux.siguiente_letra
        aux.siguiente_letra = aux.siguiente_letra.siguiente_letra

#------------------------------------------------------------
#Pruebas de las funciones de la lista enlazada con POO
#mostrar_lista(raiz)

#print()

#agregar_elemento_final("Joaquinchin")
#agregar_elemento_principio("Tote")
#sacar_elemento_final()
#sacar_elemento_principio()    
#agregar_elemento_posicion("Bayern Leverkusen", 4)
#sacar_elemento_posicion(1)

#mostrar_lista(raiz)

#------------------------------------------------------------

"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para sacar un elemento al final de la lista
3) Hacer una función para sacar un elemento al comienzo de la lista
4) Hacer una función para sacar un elemento en la posición x de la lista (reenlazar los objetos detrás)
5) Hacer una función para agregar un elemento más en la posición x de la lista   
"""

"""
7) Una empresa de transporte de carga que cuenta con vehículos propios así como vehículos tercerizados organiza su sistema financiero en 
centros de costo, donde cada centro de costo puede tener varios vehículos agregados u otros centros de costo. Un vehículo pertenece a
un centro de costo, y es el único que genera gastos y facturación. Un centro de costo representa a una empresa de terceros o la propia
empresa que gestiona todas las demás. 
a) Haga una representación gráfica de esta estructura organizacional, utilizando listas enlazadas para que pueda calcular los gastos/facturación 
para toda la organización, así como para un único centro de costos.
b) Haga una función recursiva para calcular el facturación de la organización.
"""

"""class Vehiculo:
    def __init__(self, nombre, gastos, facturacion):
        self.nombre = nombre
        self.gastos = gastos
        self.facturacion = facturacion
        self.siguiente_vehiculo = None
        
class CentroCosto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente_centro_costo = None
        self.vehiculos = None
        
    def facturacion(self):
        if self.vehiculos is None:
            return 0
        else:
            return self.vehiculos.facturacion + self.siguiente_centro_costo.facturacion()
        
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente_empresa = None
        self.centros_costo = None"""
        
#------------------------------------------------------------
class Vehiculo:
    def __init__(self, nombre, gastos, facturacion):
        self.nombre = nombre
        self.gastos = gastos
        self.facturacion = facturacion
        self.siguiente_vehiculo = None

class CentroCosto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente_centro_costo = None
        self.vehiculos = None
        
    def calcular_facturacion(self):
        total_facturacion = 0
        
        # Calcular la facturación de todos los vehículos en este centro de costo
        vehiculo_actual = self.vehiculos
        while vehiculo_actual:
            total_facturacion += vehiculo_actual.facturacion
            vehiculo_actual = vehiculo_actual.siguiente_vehiculo
        
        # Calcular la facturación de todos los subcentros de costo
        centro_costo_actual = self.siguiente_centro_costo
        while centro_costo_actual:
            total_facturacion += centro_costo_actual.calcular_facturacion()
            centro_costo_actual = centro_costo_actual.siguiente_centro_costo
        
        return total_facturacion

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.centros_costo = None

    def calcular_facturacion_total(self):
        total_facturacion = 0
        centro_costo_actual = self.centros_costo
        while centro_costo_actual:
            total_facturacion += centro_costo_actual.calcular_facturacion()
            centro_costo_actual = centro_costo_actual.siguiente_centro_costo
        return total_facturacion

class VehiculoPropio(Vehiculo):
    def __init__(self, nombre, gastos, facturacion, marca):
        super().__init__(nombre, gastos, facturacion)
        self.marca = marca

class VehiculoTercerizado(Vehiculo):
    def __init__(self, nombre, gastos, facturacion, empresa_tercerizada):
        super().__init__(nombre, gastos, facturacion)
        self.empresa_tercerizada = empresa_tercerizada

# Crear vehículos propios
vehiculo_a = VehiculoPropio("Optimus Prime", 200, 1000, "Autobots")
vehiculo_b = VehiculoPropio("Mach-5", 300, 1500, "Speed Racer")

# Crear vehículos tercerizados
vehiculo_c = VehiculoTercerizado("Bumblebee", 150, 800, "Empresa X")
vehiculo_d = VehiculoTercerizado("Rayo McQueen", 400, 2000, "Empresa Y")

# Crear centros de costo
centro_1 = CentroCosto("Gasparini")
subcentro_1 = CentroCosto("Florida")
centro_2 = CentroCosto("Gross")

# Asignar vehículos a los centros de costo
centro_1.vehiculos = vehiculo_a
vehiculo_a.siguiente_vehiculo = vehiculo_b
subcentro_1.vehiculos = vehiculo_c
centro_2.vehiculos = vehiculo_d

# Asignar subcentro de costo al centro de costo
centro_1.siguiente_centro_costo = subcentro_1

# Crear la empresa y asignar centros de costo
empresa = Empresa("Vanesa Transportes S.A.")
empresa.centros_costo = centro_1
centro_1.siguiente_centro_costo = centro_2

# Calcular la facturación de cada centro de costo
print("Facturación de la empresa Vanesa Transportes S.A.")
print()
print(f"Facturación de Gasparini: {centro_1.calcular_facturacion()}")
print(f"Facturación de Florida: {subcentro_1.calcular_facturacion()}")
print(f"Facturación de Gross: {centro_2.calcular_facturacion()}")
print()

# Calcular la facturación total de la empresa
print(f"Facturación total de la empresa: {empresa.calcular_facturacion_total()}")




