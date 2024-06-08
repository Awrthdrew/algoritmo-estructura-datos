def decimal_to_binario(decimal):
    if decimal == 0:
        return "0"
    else:
        binario = ""
        while decimal > 0:
            resto = decimal % 2
            binario = str(resto) + binario
            decimal = decimal // 2
        return binario
    
def main():
    while True:
        try:
            decimal = int(input("Ingrese un número decimal: "))
            if decimal == 0:
                break
            print(decimal_to_binario(decimal))
        except ValueError:
            print("Por favor, ingresa un número entero.")
            
main()