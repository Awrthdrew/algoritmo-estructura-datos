<?php

/*
    Final AyED
    08/02/2023
    
    Algoritmo caculador de distancia entre centros de orificios alineados y de díametro variable
    ---
    
    Se quiere confeccionar un guardador de mechas de acero rápido. Las mechas 
    son de diferentes diámetros, que van de 1mm a 13mm. Se las quiere guardar
    de forma lineal y separadas 1cm una de la otra entre sus perímetros. Las 
    presentaciones comerciales vienen cada 0.25mm.
    
    Realizar un algoritmo que calcule la distancia entre centros de mecha tal que
    cumple la distancia entre ellas. Las mechas se guardan ordenadas por diámetro.
    
    Algoritmo debe servir tambien para guardar X cantidad de caños de diferentes
    diámetros.    
    
    1) Diseñar un generardor de todas las mechas. Precios aleatoreos.
    2) Ordenarlas de menor a mayor según precio y mostrar por pantalla.
    3) Implementar una función que haga el cálculo distancia entre centros y 
       la longitud total del contenedor.
    4) Implementar una función para calcular el precio máx, mín y promedio.
    
*/

class mecha{
    public $diametro;
    public $precio;
    public function __construct($d){
        $this->diametro = $d;
        $this->precio = 0;
    }
}


?>


# raiz = Node(Mecha0)
# raiz.next_node = Node(Mecha1)
# raiz.next_node.next_node = Node(Mecha2)
# raiz.next_node.next_node.next_node = Node(Mecha3)
# raiz.next_node.next_node.next_node.next_node = Node(Mecha4)
# raiz.next_node.next_node.next_node.next_node.next_node = Node(Mecha5)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha6)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha7)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha8)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha9)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha10)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha11)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha12)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha13)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha14)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha15)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha16)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha17)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha18)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha19)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha20)     
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha21)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha22)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha23)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha24)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha25)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha26)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha27)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha28)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha29)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha30)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha31)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha32)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha33)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha34)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha35)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha36)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha37)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha38)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha39)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha40)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha41)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha42)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha43)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha44)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha45)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha46)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha47)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha48)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha49)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha50)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha51)
# raiz.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(Mecha52)

# caja_mechas = [Mecha0, Mecha1, Mecha2, Mecha3, Mecha4, Mecha5, Mecha6, Mecha7, Mecha8, Mecha9, Mecha10, Mecha11, Mecha12, Mecha13, Mecha14, Mecha15, Mecha16, Mecha17, Mecha18, Mecha19, Mecha20, Mecha21, Mecha22, Mecha23, Mecha24, Mecha24, Mecha25, Mecha26, Mecha27, Mecha28, Mecha29, Mecha30, Mecha31, Mecha32, Mecha33, Mecha34, Mecha35, Mecha36, Mecha37, Mecha38, Mecha39, Mecha40, Mecha41, Mecha42, Mecha43, Mecha44, Mecha45, Mecha46, Mecha47, Mecha48, Mecha49, Mecha50, Mecha51, Mecha52]



# Mecha0 = Mechas(0.0 , 8.82)
# Mecha1 = Mechas(0.25 , 11.26)
# Mecha2 = Mechas(0.5 , 1.31)  
# Mecha3 = Mechas(0.75 , 4.54) 
# Mecha4 = Mechas(1.0 , 4.55)
# Mecha5 = Mechas(1.25 , 19.47)
# Mecha6 = Mechas(1.5 , 17.46)
# Mecha7 = Mechas(1.75 , 8.07)
# Mecha8 = Mechas(2.0 , 3.73)
# Mecha9 = Mechas(2.25 , 2.11)
# Mecha10 = Mechas(2.5 , 8.08)
# Mecha11 = Mechas(2.75 , 5.62)
# Mecha12 = Mechas(3.0 , 3.17)
# Mecha13 = Mechas(3.25 , 15.33)
# Mecha14 = Mechas(3.5 , 19.39)
# Mecha15 = Mechas(3.75 , 19.6)
# Mecha16 = Mechas(4.0 , 16.92)
# Mecha17 = Mechas(4.25 , 8.57)
# Mecha18 = Mechas(4.5 , 18.17)
# Mecha19 = Mechas(4.75 , 10.18)
# Mecha20 = Mechas(5.0 , 9.07)
# Mecha21 = Mechas(5.25 , 2.11)
# Mecha22 = Mechas(5.5 , 11.19)
# Mecha23 = Mechas(5.75 , 14.63)
# Mecha24 = Mechas(6.0 , 9.69)
# Mecha25 = Mechas(6.25 , 17.34)
# Mecha26 = Mechas(6.5 , 2.1)
# Mecha27 = Mechas(6.75 , 12.88)
# Mecha28 = Mechas(7.0 , 8.45)
# Mecha29 = Mechas(7.25 , 14.29)
# Mecha30 = Mechas(7.5 , 7.3)
# Mecha31 = Mechas(7.75 , 15.42)
# Mecha32 = Mechas(8.0 , 8.05)
# Mecha33 = Mechas(8.25 , 18.35)
# Mecha34 = Mechas(8.5 , 5.85)
# Mecha35 = Mechas(8.75 , 11.87)
# Mecha36 = Mechas(9.0 , 3.03)
# Mecha37 = Mechas(9.25 , 4.51)
# Mecha38 = Mechas(9.5 , 10.05)
# Mecha39 = Mechas(9.75 , 10.42)
# Mecha40 = Mechas(10.0 , 17.91)
# Mecha41 = Mechas(10.25 , 2.61)
# Mecha42 = Mechas(10.5 , 19.71)
# Mecha43 = Mechas(10.75 , 1.95)
# Mecha44 = Mechas(11.0 , 16.29)
# Mecha45 = Mechas(11.25 , 8.93)
# Mecha46 = Mechas(11.5 , 14.34)
# Mecha47 = Mechas(11.75 , 8.81)
# Mecha48 = Mechas(12.0 , 19.32)
# Mecha49 = Mechas(12.25 , 8.93)
# Mecha50 = Mechas(12.5 , 16.9)
# Mecha51 = Mechas(12.75 , 6.39)
# Mecha52 = Mechas(13.0 , 1.87)
