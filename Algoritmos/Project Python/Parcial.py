
"""
Construir:
==========

1) Reporte del histórico de consumo eléctrico de un país seleccionado:
  * Mostrar un listado de Países (iterando la Dimensión 0)
  * Pedir por teclado que ingrese el ID de país deseado
  * Mostrar el consumo eléctrico del país seleccionado desde 1970. 
     * Armar el título de reporte con data["body"]["metadata"]["indicator_name"] + el nombre del país
     * Listado de año y su consumo
     * Al final mostrar un promedio de consumo total

2) ¿En que año fue el máximo consumo de cada país?

"""


data = {
    "header": {
        "name": "uneclac cepalstat api",
        "version": "1.9.13",
        "success": True,
        "machine": "01",
        "context": "public",
        "code": 200,
        "message": "",
        "timestamp": 1683157035
    },
    "body": {
        "metadata": {
            "indicator_id": 1754,
            "indicator_name": "Consumo de energía eléctrica",
            "theme": "Estadísticas e Indicadores Ambientales",
            "area": "Producción y consumo de energía de recursos renovables y no renovables",
            "note": "",
            "unit": "Gigavatios-hora",
            "data_features": "Periodicidad: anual / Cobertura: nacional",
            "definition": "Esta variable presenta información sobre el consumo de energía eléctrica, la que corresponde a energía transmitida por electrones en movimiento. Se incluye la energía eléctrica generada con cualquier fuente energética, sea primaria o secundaria (en centrales hidroeléctricas, termoeléctricas, termonucleares, geotérmicas, eólicas o fotovoltaicas).",
            "calculation_methodology": "Por lo general los datos se obtienen de registros administrativos que llevan las empresas productoras, distribuidoras y/o comercializadoras de electricidad en los países.",
            "comments": "Por lo general, las estadísticas de energía se presentan en el marco de los balances energéticos de los países. Estos balances contabilizan los flujos físicos por los cuales la energía (por tipo de fuente: primaria y secundaria) se produce, se intercambia con el exterior, se transforma y se consume por sectores económicos, es decir, muestra el conjunto de relaciones de equilibrio entre la oferta y la demanda, todo calculado en una unidad común (física o energética), dentro de un territorio (generalmente un país o región) y para un período determinado (en general un año).<br><br>\r\n\r\nPara obtener mayor información sobre definiciones y metodología de obtención de datos, consultar el sitio web de la Organización Latinoamericana de Energía (OLADE): http://www.olade.org/es/productos/SIEN/metodologias\r\n",
            "decimals": 1,
            "last_update": "Sep 28 2022  3:48PM"
        },
        "data": [
            {
                "value": "17875.47",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29138
            },
            {
                "value": "19305.6",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29139
            },
            {
                "value": "21106.84",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29140
            },
            {
                "value": "22505",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29141
            },
            {
                "value": "23445",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29142
            },
            {
                "value": "24736.56",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29143
            },
            {
                "value": "25619.64",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29144
            },
            {
                "value": "27211.79",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29145
            },
            {
                "value": "27887.76",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29146
            },
            {
                "value": "31608",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29147
            },
            {
                "value": "32888.56",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29150
            },
            {
                "value": "31946.42",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29151
            },
            {
                "value": "32655",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29152
            },
            {
                "value": "34760.73",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29153
            },
            {
                "value": "36539.06",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29154
            },
            {
                "value": "36864.11",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29155
            },
            {
                "value": "37412.18",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29156
            },
            {
                "value": "42528.89",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29157
            },
            {
                "value": "43479.48",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29158
            },
            {
                "value": "39949.53",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29159
            },
            {
                "value": "40341.09",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29160
            },
            {
                "value": "42108.97",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29161
            },
            {
                "value": "44855.77",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29162
            },
            {
                "value": "48244.41",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29163
            },
            {
                "value": "51777.01",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29164
            },
            {
                "value": "55186.32",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29165
            },
            {
                "value": "58521.1",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29166
            },
            {
                "value": "63041.3579579393",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29167
            },
            {
                "value": "68077.33",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29168
            },
            {
                "value": "70881.46",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29169
            },
            {
                "value": "75138.312",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29170
            },
            {
                "value": "76245.4780836977",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29171
            },
            {
                "value": "74875.053872093",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29172
            },
            {
                "value": "79857.9530232558",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29173
            },
            {
                "value": "84525.889",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29174
            },
            {
                "value": "89374.011",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29175
            },
            {
                "value": "95472.4819005",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29176
            },
            {
                "value": "99925.769269",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29177
            },
            {
                "value": "105138.552872766",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29178
            },
            {
                "value": "105330.564281076",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29179
            },
            {
                "value": "110573.4853342",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29180
            },
            {
                "value": "115894.765468022",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29181
            },
            {
                "value": "118351.91783804",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29182
            },
            {
                "value": "120922.013",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29183
            },
            {
                "value": "126242.658749517",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29184
            },
            {
                "value": "129616.279069767",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29185
            },
            {
                "value": "131922.235847473",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29186
            },
            {
                "value": "129000.571",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29187
            },
            {
                "value": "128744.804589268",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29188
            },
            {
                "value": "125620.291467245",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29189
            },
            {
                "value": "124495.777712322",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216,
                "dim_29117": 29190
            },
            {
                "value": "767",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29138
            },
            {
                "value": "816",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29139
            },
            {
                "value": "871",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29140
            },
            {
                "value": "896",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29141
            },
            {
                "value": "964",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29142
            },
            {
                "value": "1025",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29143
            },
            {
                "value": "1118",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29144
            },
            {
                "value": "1233",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29145
            },
            {
                "value": "1326",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29146
            },
            {
                "value": "1407",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29147
            },
            {
                "value": "1210",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29150
            },
            {
                "value": "1503",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29151
            },
            {
                "value": "1487",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29152
            },
            {
                "value": "1498",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29153
            },
            {
                "value": "1500",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29154
            },
            {
                "value": "1502",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29155
            },
            {
                "value": "1498",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29156
            },
            {
                "value": "1471",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29157
            },
            {
                "value": "1608",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29158
            },
            {
                "value": "1709",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29159
            },
            {
                "value": "1779",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29160
            },
            {
                "value": "1936",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29161
            },
            {
                "value": "1820.2",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29162
            },
            {
                "value": "1967.2",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29163
            },
            {
                "value": "2122.7",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29164
            },
            {
                "value": "2345.3",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29165
            },
            {
                "value": "2487.9",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29166
            },
            {
                "value": "2765.5",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29167
            },
            {
                "value": "2990.7",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29168
            },
            {
                "value": "3175.2",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29169
            },
            {
                "value": "3470.3266768208",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29170
            },
            {
                "value": "3468.33",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29171
            },
            {
                "value": "3620.43578587817",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29172
            },
            {
                "value": "3693.62769293917",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29173
            },
            {
                "value": "3876.6671212396",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29174
            },
            {
                "value": "4181.59906522895",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29175
            },
            {
                "value": "4488.8755206551",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29176
            },
            {
                "value": "4855.60337615969",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29177
            },
            {
                "value": "5378.80318210812",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29178
            },
            {
                "value": "5622.53258446794",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29179
            },
            {
                "value": "6017.23726161136",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29180
            },
            {
                "value": "6233.46957383121",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29181
            },
            {
                "value": "6613.77240082663",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29182
            },
            {
                "value": "6961.97560875395",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29183
            },
            {
                "value": "7391.57427145912",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29184
            },
            {
                "value": "7874.52850842733",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29185
            },
            {
                "value": "8201.10104398937",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29186
            },
            {
                "value": "8373.98847522483",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29187
            },
            {
                "value": "8450.13196870144",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29188
            },
            {
                "value": "8679.62448377979",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29189
            },
            {
                "value": "8365.1264927962",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BOL",
                "dim_208": 221,
                "dim_29117": 29190
            },
            {
                "value": "37578.1694641113",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29138
            },
            {
                "value": "42383.9104309082",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29139
            },
            {
                "value": "47389.602355957",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29140
            },
            {
                "value": "54140.8365478515",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29141
            },
            {
                "value": "60859.0759277343",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29142
            },
            {
                "value": "67228.4118041992",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29143
            },
            {
                "value": "76181.0701904297",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29144
            },
            {
                "value": "85624.6003417969",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29145
            },
            {
                "value": "95461.0270385742",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29146
            },
            {
                "value": "107036.995178223",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29147
            },
            {
                "value": "118502.997741699",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29150
            },
            {
                "value": "121665.168518066",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29151
            },
            {
                "value": "128618.351257324",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29152
            },
            {
                "value": "138843.67565918",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29153
            },
            {
                "value": "154251.643920898",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29154
            },
            {
                "value": "167296.228637695",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29155
            },
            {
                "value": "180667.732299805",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29156
            },
            {
                "value": "186329.252197266",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29157
            },
            {
                "value": "197299.38293457",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29158
            },
            {
                "value": "205654.194580078",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29159
            },
            {
                "value": "210764.858154297",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29160
            },
            {
                "value": "217539.091796875",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29161
            },
            {
                "value": "222543.779052734",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29162
            },
            {
                "value": "233167.994750977",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29163
            },
            {
                "value": "241975.697265625",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29164
            },
            {
                "value": "256438.908813477",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29165
            },
            {
                "value": "268592.727539062",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29166
            },
            {
                "value": "285470.307250977",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29167
            },
            {
                "value": "297324.205688477",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29168
            },
            {
                "value": "305249.142578125",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29169
            },
            {
                "value": "321075.006103516",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29170
            },
            {
                "value": "298496.897094727",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29171
            },
            {
                "value": "312648.37",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29172
            },
            {
                "value": "329770.72",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29173
            },
            {
                "value": "346745.99",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29174
            },
            {
                "value": "361773.35",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29175
            },
            {
                "value": "375378.2",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29176
            },
            {
                "value": "394860.78",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29177
            },
            {
                "value": "409854.94",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29178
            },
            {
                "value": "407879.77",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29179
            },
            {
                "value": "437862.51",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29180
            },
            {
                "value": "456748.235533548",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29181
            },
            {
                "value": "472035.89",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29182
            },
            {
                "value": "486667.23",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29183
            },
            {
                "value": "499922.979787821",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29184
            },
            {
                "value": "490937.707855021",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29185
            },
            {
                "value": "491604.261473445",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29186
            },
            {
                "value": "498421.256574574",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29187
            },
            {
                "value": "506939.883134131",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29188
            },
            {
                "value": "512874.376055536",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29189
            },
            {
                "value": "508546.510784835",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "BRA",
                "dim_208": 222,
                "dim_29117": 29190
            },
            {
                "value": "6316",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29138
            },
            {
                "value": "7078",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29139
            },
            {
                "value": "7479",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29140
            },
            {
                "value": "7299",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29141
            },
            {
                "value": "7867",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29142
            },
            {
                "value": "7330",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29143
            },
            {
                "value": "7802",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29144
            },
            {
                "value": "8204",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29145
            },
            {
                "value": "8760",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29146
            },
            {
                "value": "9352",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29147
            },
            {
                "value": "9769",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29150
            },
            {
                "value": "10080",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29151
            },
            {
                "value": "9909",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29152
            },
            {
                "value": "10264",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29153
            },
            {
                "value": "11115",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29154
            },
            {
                "value": "11537",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29155
            },
            {
                "value": "12135",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29156
            },
            {
                "value": "12919",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29157
            },
            {
                "value": "13793",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29158
            },
            {
                "value": "14891",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29159
            },
            {
                "value": "15432",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29160
            },
            {
                "value": "16898",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29161
            },
            {
                "value": "19251",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29162
            },
            {
                "value": "20298",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29163
            },
            {
                "value": "21586",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29164
            },
            {
                "value": "24125",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29165
            },
            {
                "value": "26877",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29166
            },
            {
                "value": "29237",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29167
            },
            {
                "value": "30864",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29168
            },
            {
                "value": "34677.01171875",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29169
            },
            {
                "value": "36597.6744186046",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29170
            },
            {
                "value": "39379.0697674419",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29171
            },
            {
                "value": "40801.1627906977",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29172
            },
            {
                "value": "44319.7674418605",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29173
            },
            {
                "value": "46915.4999479187",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29174
            },
            {
                "value": "48044.0457126439",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29175
            },
            {
                "value": "50644.9377160494",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29176
            },
            {
                "value": "52945.4348397823",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29177
            },
            {
                "value": "53445.3977269106",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29178
            },
            {
                "value": "53874.6612652356",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29179
            },
            {
                "value": "54774.5150180882",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29180
            },
            {
                "value": "57880.4411929851",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29181
            },
            {
                "value": "62220.1345282494",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29182
            },
            {
                "value": "65067.8062046266",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29183
            },
            {
                "value": "65845.9280096",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29184
            },
            {
                "value": "66478.916973984",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29185
            },
            {
                "value": "69629.4212317759",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29186
            },
            {
                "value": "68892.4299707524",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29187
            },
            {
                "value": "73112.2043411222",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29188
            },
            {
                "value": "74201.8943595486",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29189
            },
            {
                "value": "71323.980079525",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "CHL",
                "dim_208": 224,
                "dim_29117": 29190
            },
            {
                "value": "5151.16284179688",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29138
            },
            {
                "value": "5383.72106933594",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29139
            },
            {
                "value": "5790.69763183594",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29140
            },
            {
                "value": "6000.00012207032",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29141
            },
            {
                "value": "6395.34875488282",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29142
            },
            {
                "value": "6709.30224609375",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29143
            },
            {
                "value": "7000.00000000001",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29144
            },
            {
                "value": "7651.16259765626",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29145
            },
            {
                "value": "7732.55810546876",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29146
            },
            {
                "value": "8104.65112304688",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29147
            },
            {
                "value": "8698.83715820313",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29150
            },
            {
                "value": "9395.34887695313",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29151
            },
            {
                "value": "10058.1394042969",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29152
            },
            {
                "value": "9627.90698242189",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29153
            },
            {
                "value": "10534.8837890625",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29154
            },
            {
                "value": "10651.1628417969",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29155
            },
            {
                "value": "11337.2092285156",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29156
            },
            {
                "value": "12023.2561035156",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29157
            },
            {
                "value": "11430.232421875",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29158
            },
            {
                "value": "10755.8139648438",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29159
            },
            {
                "value": "11790.6977539063",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29160
            },
            {
                "value": "12662.7907714844",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29161
            },
            {
                "value": "10444.4455566406",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29162
            },
            {
                "value": "11872.0930175781",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29163
            },
            {
                "value": "12372.0930175781",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29164
            },
            {
                "value": "12848.8369140625",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29165
            },
            {
                "value": "14059.958984375",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29166
            },
            {
                "value": "14790.146484375",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29167
            },
            {
                "value": "15905.0748291015",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29168
            },
            {
                "value": "16489.991241455",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29169
            },
            {
                "value": "17329.9181848226",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29170
            },
            {
                "value": "18252.8422423339",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29171
            },
            {
                "value": "19335.6124850254",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29172
            },
            {
                "value": "20206.0414320038",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29173
            },
            {
                "value": "21556.7993977024",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29174
            },
            {
                "value": "22739.138063074",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29175
            },
            {
                "value": "24393.4433644588",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29176
            },
            {
                "value": "26908.7024859449",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29177
            },
            {
                "value": "29249.6523862856",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29178
            },
            {
                "value": "29695.6359831365",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29179
            },
            {
                "value": "31596.677801676",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29180
            },
            {
                "value": "35125.5935425672",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29181
            },
            {
                "value": "36267.3089743667",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29182
            },
            {
                "value": "38278.2109449657",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29183
            },
            {
                "value": "39718.6457614466",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29184
            },
            {
                "value": "42110.2821976001",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29185
            },
            {
                "value": "45655.4305973504",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29186
            },
            {
                "value": "46458.9987357042",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29187
            },
            {
                "value": "48292.090173043",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29188
            },
            {
                "value": "49831.1886154005",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29189
            },
            {
                "value": "46022.5795262252",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PER",
                "dim_208": 244,
                "dim_29117": 29190
            },
            {
                "value": "186.162789642811",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29138
            },
            {
                "value": "201",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29139
            },
            {
                "value": "224",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29140
            },
            {
                "value": "273",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29141
            },
            {
                "value": "304",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29142
            },
            {
                "value": "321.511631309987",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29143
            },
            {
                "value": "369",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29144
            },
            {
                "value": "452",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29145
            },
            {
                "value": "556",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29146
            },
            {
                "value": "657",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29147
            },
            {
                "value": "763.953500539065",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29150
            },
            {
                "value": "865",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29151
            },
            {
                "value": "877",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29152
            },
            {
                "value": "922",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29153
            },
            {
                "value": "995",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29154
            },
            {
                "value": "1069.30229574442",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29155
            },
            {
                "value": "1189",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29156
            },
            {
                "value": "1407",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29157
            },
            {
                "value": "1645",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29158
            },
            {
                "value": "1730",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29159
            },
            {
                "value": "1939.63727092743",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29160
            },
            {
                "value": "2161",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29161
            },
            {
                "value": "2417.39995914698",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29162
            },
            {
                "value": "2745.1697486639",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29163
            },
            {
                "value": "3048.33026409149",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29164
            },
            {
                "value": "3581.17899549008",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29165
            },
            {
                "value": "3673.06044185162",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29166
            },
            {
                "value": "3907.59144204854",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29167
            },
            {
                "value": "4020.45977050065",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29168
            },
            {
                "value": "4274.12521016598",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29169
            },
            {
                "value": "4459.5",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29170
            },
            {
                "value": "4502.4",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29171
            },
            {
                "value": "4406.69",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29172
            },
            {
                "value": "4314.68",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29173
            },
            {
                "value": "4434.29",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29174
            },
            {
                "value": "4739.9",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29175
            },
            {
                "value": "5121.61",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29176
            },
            {
                "value": "5580.45",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29177
            },
            {
                "value": "5974.97",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29178
            },
            {
                "value": "6451.13",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29179
            },
            {
                "value": "6869.78",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29180
            },
            {
                "value": "7570.52",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29181
            },
            {
                "value": "8222.26",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29182
            },
            {
                "value": "9135.62",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29183
            },
            {
                "value": "10032.69",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29184
            },
            {
                "value": "10576.386186",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29185
            },
            {
                "value": "11012.04",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29186
            },
            {
                "value": "11554.89",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29187
            },
            {
                "value": "12503.6310914447",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29188
            },
            {
                "value": "12839.8008044291",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29189
            },
            {
                "value": "13718.9",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "PRY",
                "dim_208": 242,
                "dim_29117": 29190
            },
            {
                "value": "1783",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29138
            },
            {
                "value": "1944",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29139
            },
            {
                "value": "1829",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29140
            },
            {
                "value": "1875",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29141
            },
            {
                "value": "1876",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29142
            },
            {
                "value": "2020",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29143
            },
            {
                "value": "2143",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29144
            },
            {
                "value": "2275",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29145
            },
            {
                "value": "2486",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29146
            },
            {
                "value": "2558",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29147
            },
            {
                "value": "2779",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29150
            },
            {
                "value": "2971.29990196229",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29151
            },
            {
                "value": "2963.10000038146",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29152
            },
            {
                "value": "3039.89999961853",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29153
            },
            {
                "value": "3061.99997520447",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29154
            },
            {
                "value": "3152.69998741151",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29155
            },
            {
                "value": "3301.40006065369",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29156
            },
            {
                "value": "3494.50003623962",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29157
            },
            {
                "value": "3766.69998741151",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29158
            },
            {
                "value": "3638.79996299744",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29159
            },
            {
                "value": "3806.20004844665",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29160
            },
            {
                "value": "4188.90002441407",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29161
            },
            {
                "value": "4234.19990229608",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29162
            },
            {
                "value": "4573.80010986328",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29163
            },
            {
                "value": "4710.99987792969",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29164
            },
            {
                "value": "4998.30002593994",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29165
            },
            {
                "value": "5204.09354400635",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29166
            },
            {
                "value": "5582.04435729981",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29167
            },
            {
                "value": "5883.24217224121",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29168
            },
            {
                "value": "6198.39518737793",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29169
            },
            {
                "value": "6420.93023255814",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29170
            },
            {
                "value": "6410.1897704",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29171
            },
            {
                "value": "6162.4810583",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29172
            },
            {
                "value": "5970.5940278",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29173
            },
            {
                "value": "6260.1690011",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29174
            },
            {
                "value": "6474.1521139",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29175
            },
            {
                "value": "7248.6779461",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29176
            },
            {
                "value": "7891.7902362",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29177
            },
            {
                "value": "8376.7410951",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29178
            },
            {
                "value": "8570.954029",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29179
            },
            {
                "value": "8986.1277859",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29180
            },
            {
                "value": "9307.1024551",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29181
            },
            {
                "value": "9580.3961046",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29182
            },
            {
                "value": "9852.5268024",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29183
            },
            {
                "value": "10132.7981621",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29184
            },
            {
                "value": "10538.6683054",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29185
            },
            {
                "value": "11114.3293969",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29186
            },
            {
                "value": "10865.4577331",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29187
            },
            {
                "value": "11484.1480375",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29188
            },
            {
                "value": "11323.6607029",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29189
            },
            {
                "value": "11348.0826886",
                "source_id": 714,
                "notes_ids": "",
                "iso3": "URY",
                "dim_208": 258,
                "dim_29117": 29190
            }
        ],
        "dimensions": [
            {
                "id": 208,
                "name": "País__ESTANDAR",
                "order": 0,
                "position": 2,
                "members": [
                    {
                        "name": "Argentina",
                        "id": 216,
                        "in": 1,
                        "order": 40,
                        "parent": 208,
                        "selected": 1
                    },
                    {
                        "name": "Bolivia (Estado Plurinacional de)",
                        "id": 221,
                        "in": 1,
                        "order": 90,
                        "parent": 208,
                        "selected": 1
                    },
                    {
                        "name": "Brasil",
                        "id": 222,
                        "in": 1,
                        "order": 100,
                        "parent": 208,
                        "selected": 1
                    },
                    {
                        "name": "Chile",
                        "id": 224,
                        "in": 1,
                        "order": 110,
                        "parent": 208,
                        "selected": 1
                    },
                    {
                        "name": "Paraguay",
                        "id": 242,
                        "in": 1,
                        "order": 300,
                        "parent": 208,
                        "selected": 1
                    },
                    {
                        "name": "Perú",
                        "id": 244,
                        "in": 1,
                        "order": 310,
                        "parent": 208,
                        "selected": 1
                    },
                    {
                        "name": "Uruguay",
                        "id": 258,
                        "in": 1,
                        "order": 390,
                        "parent": 208,
                        "selected": 1
                    }
                ]
            },
            {
                "id": 29117,
                "name": "Años__ESTANDAR",
                "order": 1,
                "position": 3,
                "members": [
                    {
                        "name": "1970",
                        "id": 29138,
                        "in": 1,
                        "order": 1970,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1971",
                        "id": 29139,
                        "in": 1,
                        "order": 1971,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1972",
                        "id": 29140,
                        "in": 1,
                        "order": 1972,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1973",
                        "id": 29141,
                        "in": 1,
                        "order": 1973,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1974",
                        "id": 29142,
                        "in": 1,
                        "order": 1974,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1975",
                        "id": 29143,
                        "in": 1,
                        "order": 1975,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1976",
                        "id": 29144,
                        "in": 1,
                        "order": 1976,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1977",
                        "id": 29145,
                        "in": 1,
                        "order": 1977,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1978",
                        "id": 29146,
                        "in": 1,
                        "order": 1978,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1979",
                        "id": 29147,
                        "in": 1,
                        "order": 1979,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1980",
                        "id": 29150,
                        "in": 1,
                        "order": 1980,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1981",
                        "id": 29151,
                        "in": 1,
                        "order": 1981,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1982",
                        "id": 29152,
                        "in": 1,
                        "order": 1982,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1983",
                        "id": 29153,
                        "in": 1,
                        "order": 1983,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1984",
                        "id": 29154,
                        "in": 1,
                        "order": 1984,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1985",
                        "id": 29155,
                        "in": 1,
                        "order": 1985,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1986",
                        "id": 29156,
                        "in": 1,
                        "order": 1986,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1987",
                        "id": 29157,
                        "in": 1,
                        "order": 1987,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1988",
                        "id": 29158,
                        "in": 1,
                        "order": 1988,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1989",
                        "id": 29159,
                        "in": 1,
                        "order": 1989,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1990",
                        "id": 29160,
                        "in": 1,
                        "order": 1990,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1991",
                        "id": 29161,
                        "in": 1,
                        "order": 1991,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1992",
                        "id": 29162,
                        "in": 1,
                        "order": 1992,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1993",
                        "id": 29163,
                        "in": 1,
                        "order": 1993,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1994",
                        "id": 29164,
                        "in": 1,
                        "order": 1994,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1995",
                        "id": 29165,
                        "in": 1,
                        "order": 1995,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1996",
                        "id": 29166,
                        "in": 1,
                        "order": 1996,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1997",
                        "id": 29167,
                        "in": 1,
                        "order": 1997,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1998",
                        "id": 29168,
                        "in": 1,
                        "order": 1998,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "1999",
                        "id": 29169,
                        "in": 1,
                        "order": 1999,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2000",
                        "id": 29170,
                        "in": 1,
                        "order": 2000,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2001",
                        "id": 29171,
                        "in": 1,
                        "order": 2001,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2002",
                        "id": 29172,
                        "in": 1,
                        "order": 2002,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2003",
                        "id": 29173,
                        "in": 1,
                        "order": 2003,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2004",
                        "id": 29174,
                        "in": 1,
                        "order": 2004,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2005",
                        "id": 29175,
                        "in": 1,
                        "order": 2005,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2006",
                        "id": 29176,
                        "in": 1,
                        "order": 2006,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2007",
                        "id": 29177,
                        "in": 1,
                        "order": 2007,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2008",
                        "id": 29178,
                        "in": 1,
                        "order": 2008,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2009",
                        "id": 29179,
                        "in": 1,
                        "order": 2009,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2010",
                        "id": 29180,
                        "in": 1,
                        "order": 2010,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2011",
                        "id": 29181,
                        "in": 1,
                        "order": 2011,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2012",
                        "id": 29182,
                        "in": 1,
                        "order": 2012,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2013",
                        "id": 29183,
                        "in": 1,
                        "order": 2013,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2014",
                        "id": 29184,
                        "in": 1,
                        "order": 2014,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2015",
                        "id": 29185,
                        "in": 1,
                        "order": 2015,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2016",
                        "id": 29186,
                        "in": 1,
                        "order": 2016,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2017",
                        "id": 29187,
                        "in": 1,
                        "order": 2017,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2018",
                        "id": 29188,
                        "in": 1,
                        "order": 2018,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2019",
                        "id": 29189,
                        "in": 1,
                        "order": 2019,
                        "parent": 29117,
                        "selected": 1
                    },
                    {
                        "name": "2020",
                        "id": 29190,
                        "in": 1,
                        "order": 2020,
                        "parent": 29117,
                        "selected": 0
                    }
                ]
            }
        ],
        "sources": [
            {
                "id": 714,
                "description": "Sistema de Información Económica Energética (SIEE)",
                "publication_url": "http://sier.olade.org/",
                "organization_acronym": "OLADE",
                "organization_name": "Organización Latinoamericana de Energía",
                "organization_url": "http://www.olade.org"
            }
        ],
        "footnotes": [],
        "credits": [
            {
                "id": 0,
                "description": "2023-05-03"
            },
            {
                "id": 1,
                "description": "CEPALSTAT"
            },
            {
                "id": 2,
                "description": "Comisión Económica para América Latina y el Caribe – CEPAL"
            },
            {
                "id": 3,
                "description": "Naciones Unidas"
            }
        ]
    },
    "footer": {
        "records": 357,
        "elapsed_time": "0.11558",
        "ip": "181.209.105.59",
        "query": "http://api-cepalstat.cepal.org/cepalstat/api/v1/indicator/1754/data?members=216,221,222,224,242,244,258,29138,29139,29140,29141,29142,29143,29144,29145,29146,29147,29150,29151,29152,29153,29154,29155,29156,29157,29158,29159,29160,29161,29162,29163,29164,29165,29166,29167,29168,29169,29170,29171,29172,29173,29174,29175,29176,29177,29178,29179,29180,29181,29182,29183,29184,29185,29186,29187,29188,29189,29190&lang=es&format=json&in=1&app=dashboard"
    }
}



