import threading
import time
import keyboard

bucle = True
pause = False

def sensor(texto, delay):
    count = 0
    global bucle
    global pause
    while bucle:
        if not pause:
            time.sleep(delay)
            count+=delay
            impresion= str(texto)+"   INDICE    "+str(count/delay)+"\n"
            print(impresion)

def interruptor():
    global bucle
    global pause
    while bucle:
        if keyboard.read_key() == "b":
            break
        elif keyboard.read_key() == "p":
            pause= not pause
            print("Sistema pausado/reanudado.")
    bucle=False
    
            

t1 = threading.Thread(target=sensor, args=('sensor1', 1))
t2 = threading.Thread(target=sensor, args=('sensor2', 2))
t3 = threading.Thread(target=sensor, args=('sensor3', 4))
t4 = threading.Thread(target=interruptor)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("ejecucion finalizada.")