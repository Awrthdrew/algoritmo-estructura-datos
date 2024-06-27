<?php

/*
    Final AyED
    14/12/2022
    
    Entregar el programa resuelto por email antes de las 11:30
    
    Sistema de cálculo de estadísticas climatológicas
    -------------------------------------------------
    Objetivo general: construir un sistema de carga y cálculo de información
    climática de ciudades del país.
    El sistema deberá considerar:
    1) la información de la ciudad debe estar construida con objetos con los 
       siguientes datos: nombre de la ciudad, un promedio anual de temperatura,
       temperatura máxima y mínima registrada
    2) las ciudades (objeto) será almacenadas y gestionadas en un array
    3) cuando arranca el sistema debe haber al menos 3 ciudades instanciadas
       dentro del array
    4) el sistema debe permitir, en un ciclo infinito, la carga de otra nueva 
       ciudad y agregado al array
    5) cada vez que se incorpora una nueva ciudad, se debe recalcular y mostrar:
        a) el promedio de temperatura del país. (de las temp promedio de cada ciudad)
        b) la mediana de temperatura (del promedio anual de ciudad) del país. 
           (cantidad de datos pares: entonces se hace un promedio entre los 
           datos centrales)
        c) ciudad más calurosa (de la temp max.)
        d) ciudad más fria (de la temp min.)
*/

class Ciudad {
    // Atributos
    public $nombre;
    public $tempPromedio;
    public $tempMax;
    public $tempMin;
    
    // Constructor
    public function __construct($nombre, $tempPromedio, $tempMax, $tempMin) {
        $this->nombre = $nombre;
        $this->tempPromedio = $tempPromedio;
        $this->tempMax = $tempMax;
        $this->tempMin = $tempMin;
    }
    
    // Métodos
    public function getNombre() {
        return $this->nombre;
    }
    
    public function getTempPromedio() {
        return $this->tempPromedio;
    }
    
    public function getTempMax() {
        return $this->tempMax;
    }
    
    public function getTempMin() {
        return $this->tempMin;
    }
    
    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }
    
    public function setTempPromedio($tempPromedio) {
        $this->tempPromedio = $tempPromedio;
    }
    
    public function setTempMax($tempMax) {
        $this->tempMax = $tempMax;
    }
    
    public function setTempMin($tempMin) {
        $this->tempMin = $tempMin;
    }
}

