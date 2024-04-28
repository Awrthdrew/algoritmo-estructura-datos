<?php
/*
    Final AyED
    ----------
    07/12/2022    
    
    Dado el siguiente árbol binario, defina una función recursiva
    que retorne el valor máximo, el mínimo y el promedio.
    Considerar en la función que la cantidad de nodos del árbol es dinámica,
    es decir que puedo agregar un nodo más y poder recalcular.
    (no hay que agregar un nodo más, solo diseñar la recursivad para que
    sirva para un árbol con x cantidad de nodos)
    
    Enviar solución antes de las 19:30hs por email a nicolas.giqueaux@uap.edu.ar
*/

class Node{
    public $value;
    public $left;//Node object
    public $right;//Node Object
    
    public function __construct($v){
        $this->value = $v;
        $this->left = null;
        $this->right = null;
    }
}

$root = new Node(20);
$root->left = new Node(3);
$root->left->left = new Node(10);
$root->left->right = new Node(5);
$root->left->right->left = new Node(4);
$root->left->right->right = new Node(33);
$root->right = new Node(13);
$root->right->right = new Node(7);
$root->right->right->left = new Node(23);
$root->right->right->right = new Node(1);

function calcular($n /*se puede agregar todos los parámetros que se necesite*/){
    //TODO: completar la función recursiva
}

echo("El valor máximo es: \n");
echo("El valor mínimo es: \n");
echo("El valor promedio es: \n");
echo("\n");

?>
