import threading
import time
import keyboard  # Asegúrate de instalarlo con pip install keyboard

# Variable de control para detener los hilos
detener_hilos = False

def thread_delay(thread_name, delay):
    global detener_hilos
    count = 0
    while count < 60:
        if not detener_hilos:
            time.sleep(delay)
            count += delay
            print(thread_name, 'Activado en el segundo:', count, ', y el sensor fue usado', count / delay, 'veces')
        else:
            time.sleep(0.1)  # Pequeña pausa para evitar un uso excesivo de la CPU
        

# Función para pausar o reanudar los hilos al presionar la tecla 'p'
def manejar_tecla_p(event):
    global detener_hilos
    if event.event_type == keyboard.KEY_DOWN:
        detener_hilos = not detener_hilos
        print("Hilos pausados" if detener_hilos else "Hilos reanudados")

# Asignar la función de manejo de eventos a la tecla 'p'
keyboard.on_press_key('p', manejar_tecla_p)

# Crear los hilos
t1 = threading.Thread(target=thread_delay, args=('Sensor 1', 1))
t2 = threading.Thread(target=thread_delay, args=('Sensor 2', 2))
t3 = threading.Thread(target=thread_delay, args=('Sensor 3', 4))

# Iniciar los hilos
t1.start()
t2.start()
t3.start()

# Mantener el programa en ejecución
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa detenido.")
    detener_hilos = True
    t1.join()
    t2.join()
    t3.join()
    keyboard.unhook_all()