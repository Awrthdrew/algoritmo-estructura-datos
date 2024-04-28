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
