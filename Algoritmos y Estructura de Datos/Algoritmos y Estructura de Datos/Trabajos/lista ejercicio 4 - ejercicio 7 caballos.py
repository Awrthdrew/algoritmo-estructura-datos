import random
import time

class Horse:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def advance(self):
        self.position += random.randint(1, 5)

def print_race(horses):
    print('\n'.join([
        f"{horse.name} está en el metro {horse.position}"
        for horse in horses
    ]))
    print('---')

def run_race():
    horses = [Horse(f'Caballo {i}') for i in range(1, 5)]

    while True:
        for horse in horses:
            horse.advance()

            if horse.position >= 1000:
                print_race(horses)
                return horses

        print_race(horses)
        time.sleep(1)

podium = run_race()
print(f"¡El podio es para {podium[2].name}, {podium[1].name} y {podium[0].name}!")
