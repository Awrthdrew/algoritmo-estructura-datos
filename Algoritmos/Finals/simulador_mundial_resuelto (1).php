<?php
/*
    Simulador de Mundial Qatar 2022
    ------------------------------
    1) Armar el fixture del mundial como una structura de árbol binaria
    (ver https://www.ole.com.ar/pronostico-mundial-2022)
    2) Cargar los octavos de final (eligiendo los países a gusto)
    3) Realizar una función recursiva que vaya simulando el mundial
       determinando cada ganador de partido al azar.
    
*/
class Partido{
    public $llave;
    public $equipo_1;
    public $equipo_2;
    public $partido_A;
    public $partido_B;
    
    public function __construct($ll, $e1="", $e2=""){
        $this->llave = $ll;
        $this->equipo_1 = $e1;
        $this->equipo_2 = $e2;
        $this->partido_A = null;
        $this->partido_B = null;
    }
}

$final = new Partido("final");
$final->partido_A = new Partido("Semifinal");
$final->partido_A->partido_A = new Partido("cuartos");
$final->partido_A->partido_A->partido_A = new Partido("octavos", "USA", "HOL");
$final->partido_A->partido_A->partido_B = new Partido("octavos", "ARG", "DIN");
$final->partido_A->partido_B = new Partido("cuartos");
$final->partido_A->partido_B->partido_A = new Partido("octavos", "ALE", "BEL");
$final->partido_A->partido_B->partido_B = new Partido("octavos", "BRA", "URU");
$final->partido_B = new Partido("Semifinal");
$final->partido_B->partido_A = new Partido("cuartos");
$final->partido_B->partido_A->partido_A = new Partido("octavos", "ECU", "ING");
$final->partido_B->partido_A->partido_B = new Partido("octavos", "FRA", "MEX");
$final->partido_B->partido_B = new Partido("cuartos");
$final->partido_B->partido_B->partido_A = new Partido("octavos", "ESP", "CRO");
$final->partido_B->partido_B->partido_B = new Partido("octavos", "POR", "CAM");

function simular($p, $s=""){
    $winner = "";
    if(isset($p->partido_A) and isset($p->partido_B)){
        $p->equipo_1 = simular($p->partido_A, $s."    ");
        $p->equipo_2 = simular($p->partido_B, $s."    ");
    }
    //"sortear" al ganador
    $g = rand(1,2);
    if($g == 1){
        $winner = $p->equipo_1;
    }else $winner = $p->equipo_2;
    //mostrar datos del partido
    echo($s.$p->llave.": ".$p->equipo_1." vs ".$p->equipo_2." => ".$winner."\n");
    return $winner;
}

echo(simular($final)."\n");

?>
