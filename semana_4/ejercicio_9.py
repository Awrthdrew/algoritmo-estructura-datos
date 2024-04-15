def decodificar():
    stringui = input("Escribe el texto que deseas descifrar: ")

    for i in range(5):
        traducir = stringui.replace(vocales[1][i], vocales[0][i]) #Al ser listas bidimensionales, la iteración trabaja conforme al índex de la lista, y después el range
                                                                  #realiza las iteraciones conforme al número que se necesita para decodificar.
        stringui = traducir 
    print(stringui)

def codificar():
    stringui = input('Texto a codificar: ')
    
    for i in range(5):
        traducir = stringui.replace(vocales[0][i],vocales[1][i]) #
        stringui = traducir
    print(stringui)

vocales = [['a', 'e', 'i', 'o', 'u'], ['4','9','2','7','1']]
buclardo = True

while buclardo:
    op = input('ELEGIME UNA OPCIÓN MI REY:\n 1.CODIFICAR \n 2.DECODIFICAR \n 3.FINITO \n Elegir: ')
    if op == '1':
        codificar()
    elif op == '2':
        decodificar()
    elif op == '3':
        quit()



"""Dos amigos están a jugar y propusieron escribir una carta donde todas las vocales están
cambiadas por números, uno escribe la carta y el otro tiene que traducir para español. Las
vocales aeiou estarán cambiadas por 49271. En la solución el usuario informa el texto a
traducir y su programa deberá tener una función que recibe una string como parámetro
obligatorio, esta string será la carta, y retorna otra string que será la carta en su idioma
original. La traduciõn debe ser impressa en pantalla"""


"""Considerando la cuestión anterior, los amigos ahora cambiaron la codificación, haga las
alteraciones necesarias para que la función reciba ahora dos parámetros uno obligatorio y
string, el otro también una string pero que por defecto será 49271. La solución deberá buscar
para cada número del texto su letra correspondiente utilizando la posición de la letra, o sea
aeiou corresponde a los caracteres de la string código C0C1C2C3C4, por defecto tenemos a=4, e=9,
i=2, o=7, u= 1. La tradición debe ser mostrada en pantalla y el usuario elegir si quiere informar
o no una nueva codificación."""

