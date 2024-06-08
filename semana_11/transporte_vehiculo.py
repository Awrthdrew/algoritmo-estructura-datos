"""7) Una empresa de transporte de carga que cuenta con vehículos propios así como vehículos tercerizados organiza su sistema financiero en 
centros de costo, donde cada centro de costo puede tener varios vehículos agregados u otros centros de costo. Un vehículo pertenece a
un centro de costo, y es el único que genera gastos y facturación. Un centro de costo representa a una empresa de terceros o la propia
empresa que gestiona todas las demás. 
a) Haga una representación gráfica de esta estructura organizacional, utilizando listas enlazadas para que pueda calcular los gastos/facturación 
para toda la organización, así como para un único centro de costos.
b) Haga una función recursiva para calcular el facturación de la organización.
"""

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
        self.facturacion = 0
        
    def costo_vehiculos(self, v):
        if v == None:
            return 0
        else:
            return v.gastos + self.costo_vehiculos(v.siguiente_vehiculo)
        
    def calcular_facturacion(self):
        total_facturacion = 0
        
        # Calcular la facturación de todos los vehículos en este centro de costo
        vehiculo_actual = self.vehiculos
        total_facturacion = self.facturacion + self.costo_vehiculos(self.vehiculos)
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
vehiculo_c = VehiculoTercerizado("C3", 150, 800, "Citroen")
vehiculo_d = VehiculoTercerizado("408", 400, 2000, "Peugeot")
vehiculo_e = VehiculoTercerizado("T-CROSS", 200, 1000, "Toyota")

# Crear centros de costo
centro_1 = CentroCosto("Gasparini")
subcentro_1 = CentroCosto("Florida")
centro_2 = CentroCosto("Gross")
subcentro_2 = CentroCosto("Libertador San Martín")

# Asignar vehículos a los centros de costo
centro_1.vehiculos = vehiculo_a
vehiculo_a.siguiente_vehiculo = vehiculo_b
subcentro_1.vehiculos = vehiculo_c
centro_2.vehiculos = vehiculo_d
subcentro_2.vehiculos = vehiculo_e

# Asignar subcentro de costo al centro de costo
centro_1.siguiente_centro_costo = subcentro_1
centro_2.siguiente_centro_costo = subcentro_2

# Crear la empresa y asignar centros de costo
empresa = Empresa("Vanesa Transportes S.A.")
empresa.centros_costo = centro_1
centro_1.siguiente_centro_costo = centro_2

# Calcular la facturación de cada centro de costo
print("Facturación de la empresa Vanesa Transportes S.A.")
print("#------------------------------#")
print(f"Facturación de Gasparini: {centro_1.calcular_facturacion()}")
print(f"Facturación de Florida: {subcentro_1.calcular_facturacion()}")
print(f"Facturación de Gross: {centro_2.calcular_facturacion()}")
print(f"Facturación de Libertador San Martín: {subcentro_2.calcular_facturacion()}")
print("#------------------------------#")

# Calcular la facturación total de la empresa
print(f"Facturación total de la empresa: {empresa.calcular_facturacion_total()}")