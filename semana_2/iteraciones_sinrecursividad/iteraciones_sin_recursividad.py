n1 = 0
n2 = 1

quan = int(input("Cuántos números querés leer?:  "))
count = 0

iteracion = 'Iteración N°: '

while count <= quan:
    if count%2==0 or count == 0:
        n1 = n1 + n2
        print(n1)
        # Se puede castear para lograr el resultado acumulando la variable casteando el int en un str (string) #iteracion=str(n1) ABAJO LO MISMO
    else:
        n2 = n1 + n2
        print(n2)
        # iteracion=str(n2)
    count += 1
    

print(iteracion)