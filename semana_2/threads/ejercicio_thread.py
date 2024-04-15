import threading
import time
import keyboard

bucle = True
paused = False

def sensor(puerro_sensor, delay):
    global bucle, paused
    count = 0
    while bucle:
        if not paused:
            time.sleep(delay)
            count += delay 
            print(puerro_sensor, 'Activado en el segundo:', count , '|', 'Número de sensores activados:', count/delay) 
            
def palanca():
    global bucle, paused
    while bucle:
        if keyboard.read_key() == "x":
            break
        elif keyboard.read_key() == "p":
            paused = not paused
            print("Sensores pausados. Presionar p para reanudar")
    bucle = False
    

t1 = threading.Thread(target = sensor, args=('SENSOR N°1:', 1))
t2 = threading.Thread(target = sensor, args=('SENSOR N°2:', 2))
t3 = threading.Thread(target = sensor, args=('SENSOR N°3:', 4))
t4 = threading.Thread(target = palanca)


t1.start()  
t2.start()
t3.start()
t4.start()

t1.join()
t2.join() 
t3.join()
t4.join()

print('¡Todos los sensores fueron ejecutados!')