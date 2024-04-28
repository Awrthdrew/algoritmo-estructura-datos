<?php
//Array del alfabeto comelto.
    $alfa = array('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z');

    //creacion de alfabeto cifrado
    $beta = array();
    function generaAlfa ($alfa, $key) {
        
        //key
        $k = $key;
        //largo de array2
        $larg = 26 - $k;
        //largo del corte
        $array1 = array_slice($alfa,0,$k);
        //nuevo array despues del corte
        $array2 = array_slice($alfa,$k,$larg);
        //pegar array2 y corte, mandar corte al final
        $beta = array_merge($array2,$array1);
        
        return $beta;
        
    }
 //imprimir menu
 echo("Seleccionar una opcion \n");
 echo("     1. Cifrar palabra \n");
 echo("     2. Decifrar palabra \n");
 $menu = readline();



if($menu==1){

    
    //ingreso de la palabra deseada a cifrar.

    $frase = readline("ingresar palabra a cifrar:\n");
    echo ("Advertencia: solo se pueden crifrar palabras con letras mayusculas \n");
    echo ("\n");
    $letra = str_split($frase);
    
    //ingreso de la llave
    $key = readline("ingresar llave:(la llave debe ser un numero entre 1 y 24) \n"); // Tiene que ser entre 0-24
    
    
    //incio de cifrado
    $beta = generaAlfa($alfa, $key);
    $frasenum = null;
    $r = array();
    
    //condicional menu inicio
    
    
    for($i=0;$i<count($letra);$i++) {
        
        $frasenum = array_search($letra[$i], $alfa);
        $r[] = $frasenum;      
    }
    
    //imprime frase cifrada
    echo("Palaba cifrada: ");
        foreach($r as $l) {
            
            echo($beta[$l]);
            
        }  
        echo " \n ";
}
else{
    
    
    
    //decrypt:  INPUT: Cadena de caracteres codificada. Tengo la key para desencriptar  ****Sin saber beta, 
    $fraseEncript = readline("Ingresar Palabra: ");  // readLine   frase codificada
    $arrayFraseEncript = str_split($fraseEncript);
    for($i=0;$i<count($arrayFraseEncript);$i++) {
        $toEncrypt = array_search($arrayFraseEncript[$i], $beta);
        $p[] = $toEncrypt;
    }    
    //print_r($p);
        
    foreach($p as $x) {
        
        echo($alfa[$x]);
    } 
}    
    
    
    
    //Probar sacar array de foreach
    //SI no, Leer el array con for, y sacarlo en un array del for y de la function
    //Probar todo en documento separado para no alterar este
    ?>