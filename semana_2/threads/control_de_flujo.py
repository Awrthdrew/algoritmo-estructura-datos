# Este ejercicio funciona en sentido de control de flujo

"""x = 0
if x == 0:
    print("Menem lo hizo")
    while x <= 0:
        print("Puerro pasión")
    x = x + 1 
    print(x)
print("uribe chupapija")"""

#________________________________________________________

#Ejercicios con else and elif

"""x = int(input('N°: '))
if x < 0:
    print('es negativo')
elif x == 0:
    print('es cero')
else:
    print('es positivo')"""

#________________________________________________________

#Ejercicios con switch (NO EXISTE SWITCH EN PYTHON. Ahora hay match - elif
"""
x = 14

match x:
    case 0:
        print("cero")
    case 1:
        print("uno")   
    case 14:
        print("no sé") 
        
"""

#________________________________________________________

#Ejercicios con while, else.

"""c = 0
while(c < 20):
    print(c)
    c = c + 1
else:
    print("Pasa por acá cuando el condicional es false")"""
    
#________________________________________________________

#Ejercicios con iteración de bloques. FOR, ELSE.
# Recorre listas y rangos.

#recorrer listas 
"""for c in ['a' , 'b' , 'c']:
    print(c)
else: 
    print("No hay más para iterar")"""
    
#

#for s in 'Los pibes andan cursando Algoritmos y tienen ganas de meterle con toda':
#   print(s)

#for i in range(12):
#   print(i)

# Listado por índice
"""animals = ["puerro", "uribe", "gordo"]
for i, value in enumerate(animals):
    print(i, value)"""
    
#________________________________________________________

#Ejercicios THREADS

import threading
import time

def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '--->' , count)

t1 = threading.Thread(target = thread_delay, args=('t1', 1))
t2 = threading.Thread(target = thread_delay, args=('t2', 0))

t1.start()
t2.start()

t1.join()
t2.join()

print("¡Thread exe is complete!")

