curso = ["Ana", "Ricardo", "Sofía", "Diego", "Valeria"]

for pos, elemento in curso:
    print("Chequeando el elemento: " + str(pos) + "valor: " + elemento)
    if elemento == "Maria" :
        print("Encontrado en posicion: " + str(pos))
