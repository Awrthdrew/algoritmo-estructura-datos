#Algoritmo para saber cuántos leds se necesitan para cada número ingresado.

class Leds:
    num_leds = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6  
    }
    
    def __init__(self, numero):
        self.numero = numero
        self.leds = 0
        
    def contar_leds(self):
        leds = 0
        for n in self.numero:
            leds += self.num_leds[n]
        return f'\nEl número {self.numero} tiene {leds} leds.'
    
for i in range(9):
    numero = input('\nIngrese el número: ')
    leds = Leds(numero)
    print(leds.contar_leds())
    break
print('\nFin del programa.')

