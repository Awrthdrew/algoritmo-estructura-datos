<?php
class Pais{
    private $provincias;//array para contener objetos de clase Provincia
    private $nombre;
    public function __construct($p){
        $this->provincias = $p;
        $this->nombre = "Argentina";
    }
    /*Devuelve todos: varones más mujeres*/
    public function get_total_poblacion(){
        $total = 0;
        foreach($this->provincias as $p){
            $total = $total + $p->get_total_poblacion();
        }
        return $total;
    }
    /*Devuelte el objeto Provincia según el cod recibido*/
    public function get_provincia($cod_provincia){
        $p = null;
        foreach($this->provincias as $x){
            if($x->get_cod() == $cod_provincia){
                $p = $x;
            }
        }
        return $p;
    }
    //PARA HACER :) ************************************************************
    /*
        Mostrar el total de población
        Mostrar el total de población femenina
        Mostrar el total de población masculina
    */
    public function mostrar_totales_poblacion(){
        $total=0;
        $totalmasculino=0;
        $totalfemenino=0;
        foreach ($this->provincias as $k) {
            $total= $total + $k->get_total_poblacion();
        }
        foreach ($this->provincias as $k) {
            $totalmasculino= $totalmasculino + $k->get_total_poblacion_masculina();
        }
        foreach ($this->provincias as $k) {
            $totalfemenino= $totalfemenino + $k->get_total_poblacion_femenina();
        }
        $total_total= $totalfemenino+$totalmasculino;
        $mostrar_totales_poblacion =  ("Argentina tiene una población total de {$total}, de los cuales {$totalfemenino} son mujeres y {$totalmasculino} son varones. En total son {$total_total}");
        return $mostrar_totales_poblacion;
    }    
   
    /*
        Mostrar el nombre de provincia y su ratio de habitantes por vivienda
        Orderna por ratio descendentemente
    */
    public function mostrar_ratio_habitantes_por_vivienda_por_provincia(){
        $array= array();
        foreach ($this->provincias as $k) {
            $total_viviendas=0;
            $ratio=0;
            $nombre=null;
            foreach ($k->get_viviendas() as $v) {
                $total_viviendas=$total_viviendas+ $v->get_viviendas();
            }
            $ratio= $k->get_total_poblacion()/ $total_viviendas;
            $nombre= $k->get_nombre();
            array_push($array,"El ratio de habitantes por vivienda en {$nombre} es de {$ratio} por vivienda");
        }
        return $array;
    }
   
    /*
        Mostrar por sexo el % de analfabetismo
    */
    public function mostrar_porcentaje_analfabetismo_por_sexo(){
        $array= array();
        foreach ($this->provincias as $k) {
       
            $porcentaje_varones=0;
            $porcentaje_mujeres=0;
            $nombre=null;

            $porcentaje_varones= ($k->get_alfabetismo()->get_total_varones_analfabetos() / $k->get_alfabetismo()->get_total_varones())*100;
            $porcentaje_mujeres= ($k->get_alfabetismo()->get_total_mujeres_analfabetos() / $k->get_alfabetismo()->get_total_mujeres())*100;
           
           
            $nombre= $k->get_nombre();
            array_push($array,"El porcentaje de varones analfabetos en {$nombre} es de {$porcentaje_varones} % \n 
            y el porcentaje de mujeres analfabetos es de {$porcentaje_mujeres} % \n");
        }
       
        return $array;

    }
    /*
        Mostrar el nombre de provincia y el % de analfabetos.
        Ordenar la lista descendentemente por el %
    */
    public function mostrar_porcentaje_analfabetismo_por_provincia(){
        $array= array();
        foreach ($this->provincias as $k) {
            $porcentaje_analfabetos_por_provincia= ($k->get_alfabetismo()->get_total_analfabetos() / $k->get_alfabetismo()->get_total()*100);
            $nombre= $k->get_nombre();
            array_push($array,"{$porcentaje_analfabetos_por_provincia} % es el porcentaje de analfabetismo en {$nombre}");
        }
        for($i=0;$i<count($array);$i++){
            $val = $array[$i];
            $j = $i-1;
            while($j>=0 && $array[$j] > $val){
                $array[$j+1] = $array[$j];
                $j--;
            }
            $array[$j+1] = $val;
        }
        return $array;
    }
    /*
        Mostrar el nombre de provincia y el % de viviendas sin retrete
        Ordenar la lista descendentemente por el %
    */
    public function mostrar_porcentaje_vivendas_sin_retrete_por_provincia(){
        $array= array();
        foreach ($this->provincias as $k) {
            $porcentaje_viviendas_sin_retrete_por_provincia= ($k->get_sanitario()->get_sin_retrete() / ($k->get_sanitario()->get_sin_retrete() + $k->get_sanitario()->get_con_retrete())*100);
            $nombre= $k->get_nombre();
            array_push($array,"{$porcentaje_viviendas_sin_retrete_por_provincia}% es el porcentaje de viviendas sin retrete en {$nombre}");
        }
        for($i=0;$i<count($array);$i++){
            $val = $array[$i];
            $j = $i-1;
            while($j>=0 && substr($array[$j],0,8) > substr($val,0,8)){
                $array[$j+1] = $array[$j];
                $j--;
            }
            $array[$j+1] = $val;
        }
        return $array;
    }
    /*
        Mostrar el nombre de provincia y el % de los que no viven en una casa o departamento.
        Ordenar la lista descendentemente por el %
    */
    public function mostrar_porcentaje_vivienda_precaria_por_provincia(){
        $array= array();
        foreach ($this->provincias as $k) {
            $total_viviendas_precarias=0;
            $total_viviendas=0;
            $porcentaje=0;
            foreach ($k->get_viviendas() as $v) {
                if ($v->get_tipo() != 0 and $v->get_tipo() != 3) {
                    $total_viviendas_precarias= $total_viviendas_precarias + $v->get_viviendas();
                }
                $total_viviendas=$total_viviendas+$v->get_viviendas();
            }
            $nombre= $k->get_nombre();
            $porcentaje= ($total_viviendas_precarias/$total_viviendas) * 100;
            array_push($array, "{$porcentaje} $ es el porcentaje de vivienda precaria en {$nombre}" );
        }
        for($i=0;$i<count($array);$i++){
            $val = $array[$i];
            $j = $i-1;
            while($j>=0 && substr($array[$j],0,8) > substr($val,0,8)){
                $array[$j+1] = $array[$j];
                $j--;
            }
            $array[$j+1] = $val;
        }
        return $array;
    }
    /*
        Se quiere saber si hay una correlación entre las variables: analfabetismos vs
        viviendas precarias y sin retrete. Por ello hacer:
        1) Ordenar la lista de provincias según el % de analfabetismos de forma
        ascendente. Esto nos da una pendiente positiva.
        2) Calcular la pendiente de la regresión lineal para las variables
        "viviendas precarias" y para "sin retetre" y compare:
        ¿Cómo es el signo de la pendiente de estas dos variables comparado con
        el signo de la pendientes del % de alfabetismo?
        ¿Qué se puede concluir?
    */
    public function mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete(){
        $array= array();
        $array_provincias= array();
        foreach ($this->provincias as $k) {
            $porcentaje_analfabetos_por_provincia=round(($k->get_alfabetismo()->get_total_analfabetos() / $k->get_alfabetismo()->get_total()*100),2,PHP_ROUND_HALF_UP);
            $nombre= $k->get_nombre();
            array_push($array_provincias, $nombre);
            array_push($array,$porcentaje_analfabetos_por_provincia);
        }
        for($i=0;$i<count($array);$i++){
            $val = $array[$i];
            $val1= $array_provincias[$i];
            $j = $i-1;
            while($j>=0 && $array[$j] > $val){
                $array[$j+1] = $array[$j];
                $array_provincias[$j+1]=$array_provincias[$j];
                $j--;
            }
            $array[$j+1] = $val;
            $array_provincias[$j+1]=$val1;
        }
        //------------------------------------------------
        $array_viviendas_precarias= array();
        $array_viviendas_sin_retrete= array();
        foreach ($array_provincias as $k) {
            foreach ($this->provincias as $v) {
                if ($k == $v->get_nombre()) {

                    $total_viviendas_precarias=0;
                    $total_viviendas=0;
                    $porcentaje_viviendas_precarias=0;
                    $porcentaje_viviendas_sin_retrete_por_provincia=0;
                    foreach ($v->get_viviendas() as $g) {
                        if ($g->get_tipo() != 0 and $g->get_tipo() != 3) {
                            $total_viviendas_precarias= $total_viviendas_precarias + $g->get_viviendas();
                        }
                        $total_viviendas=$total_viviendas+$g->get_viviendas();
                    }
                    $porcentaje_viviendas_precarias= ($total_viviendas_precarias/$total_viviendas) * 100;
                    array_push($array_viviendas_precarias, $porcentaje_viviendas_precarias);
//-----------------------------------------------------------------------------------------------------------
                    $porcentaje_viviendas_sin_retrete_por_provincia= ($v->get_sanitario()->get_sin_retrete() / ($v->get_sanitario()->get_sin_retrete() + $v->get_sanitario()->get_con_retrete())*100);
                    array_push($array_viviendas_sin_retrete, $porcentaje_viviendas_sin_retrete_por_provincia);
                }
            }
        }
        // x * y
        $sum_x_por_y=0;
        foreach ($array_viviendas_sin_retrete as $k) {
           for ($i=0; $i < count($array_viviendas_precarias); $i++) {
            $sum_x_por_y= $sum_x_por_y + ($k * ($i+1)); }
        }
        $sum_x=0;
        for ($i=0; $i <count($array_viviendas_precarias) ; $i++) {
            $sum_x= $sum_x + $i;
        }
        $sum_y=0;
        foreach ($array_viviendas_sin_retrete as $k) {
            $sum_y= $sum_y + $k;
        }
        $sum_x_al_cuadrado=0;
        for ($j=0; $j <count($array_viviendas_precarias) ; $j++) {
            $sum_x_al_cuadrado= $sum_x_al_cuadrado + (pow($j));
        }
        return $sum_x;
    }
}
class Provincia{
    private $cod;
    private $nombre;
    private $alfabetismo;//para contener un objeto de la clase Alfabetismo
    private $sanitario;//para contener un objeto de la clase Sanitario
    private $viviendas;//array para contener todos los tipos de viviendas
    public function __construct($c, $n, $a, $r, $v){
        $this->cod = $c;
        $this->nombre = $n;
        $this->alfabetismo = $a;
        $this->sanitario = $r;
        $this->viviendas = $v;
    }
    /*Devuelve todos: varones más mujeres*/
    public function get_total_poblacion(){return $this->alfabetismo->get_total();}
    public function get_total_poblacion_femenina(){return $this->alfabetismo->get_total_mujeres();}
    public function get_total_poblacion_masculina(){return $this->alfabetismo->get_total_varones();}
    public function get_cod(){return $this->cod;}
    public function get_viviendas(){return $this->viviendas;}
    public function get_nombre(){return $this->nombre;}
    public function get_alfabetismo(){return $this->alfabetismo;}
    public function get_sanitario(){return $this->sanitario;}
}
class PorSexo{
    private $varones;
    private $mujeres;
    public function __construct($v, $m){
        $this->varones = $v;
        $this->mujeres = $m;
    }    
    /*Devuelve todos: varones más mujeres*/
    public function get_total_varones(){return $this->varones;}
    public function get_total_mujeres(){return $this->mujeres;}
    public function get_total(){return $this->varones + $this->mujeres;}
}
class Alfabetismo{
    private $alfabetos;//para contener un objeto de clase PorSexo con datos de la personas alfabetas
    private $analfabetos;//para contener un objeto de clase PorSexo con datos de la personas analfabetas    
    public function __construct($a, $no_a){
        $this->alfabetos = $a;
        $this->analfabetos = $no_a;
    }
    /*Total de la población: alfabetas + analfabetas*/
    public function get_total(){return $this->alfabetos->get_total()+$this->analfabetos->get_total();}
    public function get_total_varones(){return $this->alfabetos->get_total_varones() + $this->analfabetos->get_total_varones();}
    public function get_total_mujeres(){return $this->alfabetos->get_total_mujeres() + $this->analfabetos->get_total_mujeres();}
    public function get_total_varones_analfabetos(){return $this->analfabetos->get_total_varones();}
    public function get_total_mujeres_analfabetos(){return $this->analfabetos->get_total_mujeres();}
    public function get_total_analfabetos(){return $this->analfabetos->get_total();}
}
class Sanitario{
    private $con_retrete;
    private $sin_retrete;
    public function __construct($c, $s){
        $this->con_retrete = $c;
        $this->sin_retrete = $s;
    }
    public function get_con_retrete(){return $this->con_retrete;}
    public function get_sin_retrete(){return $this->sin_retrete;}
}
class Vivienda{
    /* TIPO (según INDEC):
        0: Casa
        1: Rancho
        2: Casilla
        3: Departamento
        4: Pieza/s en inquilinato
        5: Pieza/s en hotel o pensión
        6: Local no construido para habitación
        7: Vivienda móbil
    */
    private $tipo;
    private $cantidad;
    public function __construct($t, $c){
        $this->tipo = $t;
        $this->cantidad = $c;
    }
    public function get_viviendas(){return $this->cantidad;}
    public function get_tipo(){return $this->tipo;}
}
/*
Fuente de datos: https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-135
*/
$arg = new Pais(array(
    new Provincia(0, 'Ciudad Autónoma de Buenos Aires', new Alfabetismo(new PorSexo(1160483, 1395255), new PorSexo(5344, 7059)), new Sanitario(1061211, 21787), array(new Vivienda(0, 252771), new Vivienda(1, 565), new Vivienda(2, 1884), new Vivienda(3, 788791), new Vivienda(4, 19571), new Vivienda(5, 17082), new Vivienda(6, 2237), new Vivienda(7, 97))),
    new Provincia(1, '24 partidos del Gran Buenos Aires', new Alfabetismo(new PorSexo(3917957, 4223950), new PorSexo(55416, 61809)), new Sanitario(2294650, 358638), array(new Vivienda(0, 2212645), new Vivienda(1, 17794), new Vivienda(2, 73827), new Vivienda(3, 329731), new Vivienda(4, 12452), new Vivienda(5, 1405), new Vivienda(6, 5091), new Vivienda(7, 343))),
    new Provincia(2, 'Interior de la provincia de Buenos Aires', new Alfabetismo(new PorSexo(2285525, 2438254), new PorSexo(33289, 28494)), new Sanitario(1625106, 146799), array(new Vivienda(0, 1502191), new Vivienda(1, 12283), new Vivienda(2, 35724), new Vivienda(3, 212714), new Vivienda(4, 4117), new Vivienda(5, 817), new Vivienda(6, 3026), new Vivienda(7, 1033))),
    new Provincia(3, 'Catamarca', new Alfabetismo(new PorSexo(144528, 148625), new PorSexo(3108, 2928)), new Sanitario(75871, 13505), array(new Vivienda(0, 83578), new Vivienda(1, 2134), new Vivienda(2, 400), new Vivienda(3, 2666), new Vivienda(4, 427), new Vivienda(5, 30), new Vivienda(6, 96), new Vivienda(7, 45))),
    new Provincia(4, 'Chaco', new Alfabetismo(new PorSexo(394795, 411225), new PorSexo(22440, 24292)), new Sanitario(916669, 61884), array(new Vivienda(0, 236946), new Vivienda(1, 12558), new Vivienda(2, 5696), new Vivienda(3, 12052), new Vivienda(4, 2048), new Vivienda(5, 165), new Vivienda(6, 424), new Vivienda(7, 244))),
    new Provincia(5, 'Chubut', new Alfabetismo(new PorSexo(205779, 206044), new PorSexo(4049, 4265)), new Sanitario(197102, 51742), array(new Vivienda(0, 122955), new Vivienda(1, 1479), new Vivienda(2, 1917), new Vivienda(3, 19318), new Vivienda(4, 1068), new Vivienda(5, 58), new Vivienda(6, 237), new Vivienda(7, 144))),
    new Provincia(6, 'Córdoba', new Alfabetismo(new PorSexo(1314229, 1425717), new PorSexo(22334, 18451)), new Sanitario(176147, 93986), array(new Vivienda(0, 840488), new Vivienda(1, 5929), new Vivienda(2, 2775), new Vivienda(3, 124044), new Vivienda(4, 2852), new Vivienda(5, 791), new Vivienda(6, 1199), new Vivienda(7, 475))),
    new Provincia(7, 'Corrientes', new Alfabetismo(new PorSexo(372493, 399455), new PorSexo(17969, 16523)), new Sanitario(136043, 11133), array(new Vivienda(0, 210288), new Vivienda(1, 13056), new Vivienda(2, 8147), new Vivienda(3, 14201), new Vivienda(4, 2293), new Vivienda(5, 236), new Vivienda(6, 393), new Vivienda(7, 230))),
    new Provincia(8, 'Entre Ríos', new Alfabetismo(new PorSexo(486281, 519080), new PorSexo(12294, 9610)), new Sanitario(326978, 30272), array(new Vivienda(0, 317956), new Vivienda(1, 3805), new Vivienda(2, 7273), new Vivienda(3, 26680), new Vivienda(4, 644), new Vivienda(5, 176), new Vivienda(6, 495), new Vivienda(7, 221))),
    new Provincia(9, 'Formosa', new Alfabetismo(new PorSexo(200956, 206992), new PorSexo(7821, 9575)), new Sanitario(79122, 51012), array(new Vivienda(0, 109807), new Vivienda(1, 12203), new Vivienda(2, 1514), new Vivienda(3, 4124), new Vivienda(4, 2104), new Vivienda(5, 44), new Vivienda(6, 229), new Vivienda(7, 109))),
    new Provincia(10, 'Jujuy', new Alfabetismo(new PorSexo(261419, 269965), new PorSexo(5404, 11784)), new Sanitario(122201, 32710), array(new Vivienda(0, 134293), new Vivienda(1, 7286), new Vivienda(2, 2595), new Vivienda(3, 7824), new Vivienda(4, 2510), new Vivienda(5, 74), new Vivienda(6, 245), new Vivienda(7, 84))),
    new Provincia(11, 'La Pampa', new Alfabetismo(new PorSexo(128679, 133208), new PorSexo(2805, 2227)), new Sanitario(101706, 3091), array(new Vivienda(0, 95356), new Vivienda(1, 458), new Vivienda(2, 169), new Vivienda(3, 8239), new Vivienda(4, 317), new Vivienda(5, 10), new Vivienda(6, 177), new Vivienda(7, 71))),
    new Provincia(12, 'La Rioja', new Alfabetismo(new PorSexo(131833, 136616), new PorSexo(2843, 2154)), new Sanitario(75564, 10803), array(new Vivienda(0, 77743), new Vivienda(1, 1970), new Vivienda(2, 1643), new Vivienda(3, 4208), new Vivienda(4, 597), new Vivienda(5, 56), new Vivienda(6, 105), new Vivienda(7, 45))),
    new Provincia(13, 'Mendoza', new Alfabetismo(new PorSexo(681053, 730907), new PorSexo(15527, 16003)), new Sanitario(421292, 38258), array(new Vivienda(0, 398510), new Vivienda(1, 7618), new Vivienda(2, 1985), new Vivienda(3, 48846), new Vivienda(4, 1686), new Vivienda(5, 216), new Vivienda(6, 595), new Vivienda(7, 94))),
    new Provincia(14, 'Misiones', new Alfabetismo(new PorSexo(412901, 422882), new PorSexo(17110, 18662)), new Sanitario(201604, 88659), array(new Vivienda(0, 249745), new Vivienda(1, 7866), new Vivienda(2, 11548), new Vivienda(3, 16938), new Vivienda(4, 3376), new Vivienda(5, 77), new Vivienda(6, 560), new Vivienda(7, 153))),
    new Provincia(15, 'Neuquén', new Alfabetismo(new PorSexo(219539, 225070), new PorSexo(5120, 5339)), new Sanitario(145697, 13605), array(new Vivienda(0, 130466), new Vivienda(1, 1924), new Vivienda(2, 3425), new Vivienda(3, 21312), new Vivienda(4, 1743), new Vivienda(5, 83), new Vivienda(6, 228), new Vivienda(7, 121))),
    new Provincia(16, 'Río Negro', new Alfabetismo(new PorSexo(255390, 262917), new PorSexo(6541, 6539)), new Sanitario(171370, 19227), array(new Vivienda(0, 155561), new Vivienda(1, 2149), new Vivienda(2, 4091), new Vivienda(3, 27071), new Vivienda(4, 1230), new Vivienda(5, 72), new Vivienda(6, 331), new Vivienda(7, 92))),
    new Provincia(17, 'Salta', new Alfabetismo(new PorSexo(459258, 478751), new PorSexo(12710, 17657)), new Sanitario(202113, 64962), array(new Vivienda(0, 220293), new Vivienda(1, 14806), new Vivienda(2, 11076), new Vivienda(3, 17161), new Vivienda(4, 2881), new Vivienda(5, 120), new Vivienda(6, 450), new Vivienda(7, 288))),
    new Provincia(18, 'San Juan', new Alfabetismo(new PorSexo(260076, 278149), new PorSexo(6360, 5133)), new Sanitario(142970, 19234), array(new Vivienda(0, 134753), new Vivienda(1, 11219), new Vivienda(2, 1075), new Vivienda(3, 14489), new Vivienda(4, 405), new Vivienda(5, 43), new Vivienda(6, 196), new Vivienda(7, 24))),
    new Provincia(19, 'San Luis', new Alfabetismo(new PorSexo(170030, 177358), new PorSexo(3674, 2838)), new Sanitario(108089, 9677), array(new Vivienda(0, 104692), new Vivienda(1, 1125), new Vivienda(2, 470), new Vivienda(3, 10380), new Vivienda(4, 654), new Vivienda(5, 106), new Vivienda(6, 208), new Vivienda(7, 131))),
    new Provincia(20, 'Santa Cruz', new Alfabetismo(new PorSexo(113297, 106023), new PorSexo(1291, 1213)), new Sanitario(72841, 3392), array(new Vivienda(0, 64118), new Vivienda(1, 524), new Vivienda(2, 852), new Vivienda(3, 9339), new Vivienda(4, 1181), new Vivienda(5, 43), new Vivienda(6, 118), new Vivienda(7, 58))),
    new Provincia(21, 'Santa Fe', new Alfabetismo(new PorSexo(1273525, 1383361), new PorSexo(25003, 23092)), new Sanitario(862253, 86116), array(new Vivienda(0, 793209), new Vivienda(1, 10303), new Vivienda(2, 8279), new Vivienda(3, 132409), new Vivienda(4, 2023), new Vivienda(5, 796), new Vivienda(6, 1119), new Vivienda(7, 231))),
    new Provincia(22, 'Santiago del Estero', new Alfabetismo(new PorSexo(328348, 340598), new PorSexo(14809, 13061)), new Sanitario(122529, 75377), array(new Vivienda(0, 169162), new Vivienda(1, 20833), new Vivienda(2, 1097), new Vivienda(3, 5830), new Vivienda(4, 463), new Vivienda(5, 75), new Vivienda(6, 223), new Vivienda(7, 223))),
    new Provincia(23, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur', new Alfabetismo(new PorSexo(52991, 50430), new PorSexo(347, 358)), new Sanitario(35041, 1648), array(new Vivienda(0, 25108), new Vivienda(1, 102), new Vivienda(2, 3817), new Vivienda(3, 7326), new Vivienda(4, 226), new Vivienda(5, 43), new Vivienda(6, 44), new Vivienda(7, 23))),
    new Provincia(24, 'Tucumán', new Alfabetismo(new PorSexo(557210, 596990), new PorSexo(15859, 13295)), new Sanitario(276897, 58924), array(new Vivienda(0, 287900), new Vivienda(1, 4931), new Vivienda(2, 11031), new Vivienda(3, 30431), new Vivienda(4, 897), new Vivienda(5, 184), new Vivienda(6, 344), new Vivienda(7, 103)))
));
//var_dump($arg);
//echo($arg->get_provincia(0)->get_total_poblacion());
echo($arg->mostrar_totales_poblacion()."\n");
//echo($arg->get_total_poblacion()."\n");
print_r($arg->mostrar_ratio_habitantes_por_vivienda_por_provincia());
echo("\n");
print_r($arg->mostrar_porcentaje_analfabetismo_por_sexo());
echo("\n");
print_r($arg->mostrar_porcentaje_analfabetismo_por_provincia());
echo("\n");
print_r($arg->mostrar_porcentaje_vivendas_sin_retrete_por_provincia());
echo("\n");
print_r($arg->mostrar_porcentaje_vivienda_precaria_por_provincia());
echo("\n");
print_r($arg->mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete());

?>