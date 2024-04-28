

#__________________________________________________________________________________________________________________________________________        
        

#Definir un array de 5 elementos de pares asociativos “nombre” => edad. Utilizar diccionario en
#la solución
#------------------------------------------------------------------------------------
#1
# Personas = {"Juan":23,"pablo":14, "Lucas":45, "Alberto":12, "Thiago":67}




#__________________________________________________________________________________________________________________________________________        
        


#Recorrerlo mostrando las edades.
#Recorrerlo mostrando el índice y las edades. 

#-----------------------------------------------
#2, 3
# for nombre,edad in Personas.items():
#     print(f"nombre: {nombre}, edad: {edad}")
       
    
    
    
#__________________________________________________________________________________________________________________________________________        
            
    
# Ingresar un nro por teclado y mostrar si es numero primo o no, usar una función recursiva en la
# solución     
#------------------------------------------------------------
#4

# def hay_divisor(primo,n):
#     if(n<=1):
#         return False
#     else:
#         if(primo%n==0):
#             return True
#         else:
#             return hay_divisor(primo,n-1)
        
# primo = int(input("Numero primo: "))        
        
# if(hay_divisor(primo, primo-1)):
#     print("El número no es primo ")
# else: 
#     print("El número es primo ")            
        
        
        
        
        
        
#__________________________________________________________________________________________________________________________________________        
        
        
# Ingresar la fecha de nacimiento y mostrar la edad actual, import datetime para implementar la
# solución. 
#----------------------------------------------------------
#5
        
import datetime

def calculo():

   #nacimiento = int(input("Introduzca su fecha de nacimineto: "))
   
   year = int(input("Introduza su año de nacimiento: "))
   month = int(input("Introduza su mes de nacimiento: "))
   day = int(input("Introduza su día de nacimiento: "))
   
   fecha_nac = datetime.date(year,month,day)      
   
   fecha_actual = datetime.date.today()
   
   edad = (fecha_actual - fecha_nac).days / 365
   
   print("Tu edad es " , int(edad), "año/s")      
        
calculo()        
        
        
        
      
#__________________________________________________________________________________________________________________________________________        
              
        
# Ingresar un numero N por teclado y crear una matriz M( NxN ) con todos los valores 0 y
# mostrar en pantalla. Para representar la matriz use una estructura de datos con lista de lista, 
#------------------------------------------------------------
#6
# n = int(input("Ingrese un número M (N*N)"))
# M = []
# for i in range(n):
#     m =[0]*n
#     M.append(m)
    
    
# print(M)    
       
   
   
   
    
    
#__________________________________________________________________________________________________________________________________________        

# Inicializar la matriz anterior con valores de 0 a N²-1, o sea M(0,0)=0, M(0,1)=1 … M(N-1,N1)=N²-1, por ejemplo con N=4 tenemos:              
matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0] 
]     
     
#-------------------------------------------------------------
#7

# print(matriz)

# size = int(input("Ingrese el tamaño de la matriz: "))

# linea = [0 for i in range(size)]
# print("Linea con N elemento 0: " + str(linea))

# matriz = [ (0 for i in range(size)) for j in range(size)]
# print("Linea con NXn elemento 0: " + str(matriz))
# count = 0

# for linea in range(size):
#     for columna in range(size):
#         matriz[linea][columna] = count
#         count += 1
        
# for linea in range(size):
#     for columna in range(size):
#         print("4d" /  matriz[linea][columna], end='')  
#     print()          
     
        
    
    
