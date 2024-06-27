

# /*
# Un FQDN (sigla en inglés de fully qualified domain name) es un nombre de dominio
# completo que incluye el nombre de la computadora y el nombre de dominio asociado
# a ese equipo.

# Los dominios en internet están organizados en una estructura jerárquica donde a
# cada nodo del árbol se le llama zona.

# Desarrollar una función recursiva que recorra el árbol de ejemplo abajo construido
# y muestre un listado de dominios que contiene. El resultado buscado es un listado
# de la siguiente manera:

# ar.com.lanacion.www
# ar.org.hospitalitaliano.www
# ar.edu.uap.portalalumno
# ar.edu.uap.login
# ar.edu.uap.cc.base-datos
# ar.edu.uap.cc.webserver
# ar.edu.uap.cc.proxy
# ar.mil

# Enviar solución antes de las 16:25hs por email a nicolas.giqueaux@uap.edu.ar
# */


class Zone:
    def __init__(self, z="ar"):
        self.zone = z
        self.sub_zones = [] # Lista para almacenar las subzonas de la zona actual
    
    def add_zone(self, z):
        
        self.sub_zones.append(z) # Agrega una subzona a la lista de subzonas de la zona actual

root_ar = Zone() # Crea una instancia de la clase Zone llamada root_ar que representa la raíz del árbol de dominios

root_ar.add_zone(Zone("com")) # Agrega una subzona con nombre "com" a root_ar

# Agrega subzonas adicionales a root_ar siguiendo la estructura del árbol
root_ar.sub_zones[0].add_zone(Zone("lanacion"))
root_ar.sub_zones[0].sub_zones[0].add_zone(Zone("www"))

root_ar.add_zone(Zone("org"))

root_ar.sub_zones[1].add_zone(Zone("hospitalitaliano"))
root_ar.sub_zones[1].sub_zones[0].add_zone(Zone("www"))

root_ar.add_zone(Zone("edu"))
root_ar.sub_zones[2].add_zone(Zone("uap"))
root_ar.sub_zones[2].sub_zones[0].add_zone(Zone("portalalumno"))

root_ar.sub_zones[2].sub_zones[0].add_zone(Zone("login"))

root_ar.sub_zones[2].sub_zones[0].add_zone(Zone("cc"))
root_ar.sub_zones[2].sub_zones[0].sub_zones[2].add_zone(Zone("base-datos"))

root_ar.sub_zones[2].sub_zones[0].sub_zones[2].add_zone(Zone("webserver"))

root_ar.sub_zones[2].sub_zones[0].sub_zones[2].add_zone(Zone("proxy"))

root_ar.add_zone(Zone("mil"))


#print(root_ar.zone)


def practica(r, sangria = ""):
    sangria += r.zone  
    if len(r.sub_zones) > 0:
        for x in r.sub_zones:
            practica(x, sangria + ".")
    else:
        print(sangria)


practica(root_ar)

def list_all_domains(z, d=""):
    if z is not None:  # Verifica si el objeto Zone pasado como argumento existe
        d += z.zone    # Concatena el nombre de la zona a la cadena d
        if len(z.sub_zones) > 0:  # Verifica si el objeto Zone tiene subzonas
            for zz in z.sub_zones: # Recorre todas las subzonas
                list_all_domains(zz, d + ".") # Llamada recursiva a list_all_domains para cada subzona
        else:
            print(d)   # Imprime la cadena d si el objeto Zone no tiene subzonas (hoja del árbol)

list_all_domains(root_ar)   # Llamada a la función list_all_domains pasando la instancia root_ar

# #print()
