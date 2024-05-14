"""
Consumos eléctrico de los países de la región desde 1970
========================================================

Datos reales obtenidos de ONU: https://statistics.cepal.org/portal/cepalstat/dashboard.html?theme=3&lang=es
Para examinar los datos abrir con el navegador el archivo: ONU-consumo-energia-electrica.json

Estructura general de los datos:
--------------------------------
{
    "header": {
        ...
    },
    "body": {
        "metadata": {
            "indicator_id": 1754,
            "indicator_name": "Consumo de energía eléctrica", => Título
            "unit": "Gigavatios-hora",
        },
        "data": [
            {
                "value": "17875.47", => Dato que nos interesa
                "source_id": 714,
                "notes_ids": "",
                "iso3": "ARG",
                "dim_208": 216, => ID de país
                "dim_29117": 29138 => ID de año
            },
            ...
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
                    ...
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
                    ...
                ]
            }
        ],
        "sources": [
            ...
        ],
        "footnotes": [],
        "credits": [
            ...
        ]
    },
    "footer": {
        ...
    }
}


Construir:
==========

1) Reporte del histórico de consumo eléctrico de un país seleccionado:
  * Mostrar un listado de Países (iterando la Dimensión 0)
  * Pedir por teclado que ingrese el ID de país deseado
  * Mostrar el consumo eléctrico del país seleccionado desde 1970. 
     * Armar el título de reporte con data["body"]["metadata"]["indicator_name"] + el nombre del país
     * Listado de año y su consumo
     * Al final mostrar un promedio de consumo total

2) ¿En que año fue el máximo consumo de cada país?"""

from consumo_energia import data


