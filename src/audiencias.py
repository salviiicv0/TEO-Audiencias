import csv # Para leer los csv de datos
from matplotlib import pyplot as plt # Para mostrar gráficas, importamos matplotlib.pyplot, renombrándolo como plt
from collections import namedtuple # Para definir tuplas con nombre
Audiencia = namedtuple ("Audiencia", "edición, share")

def lee_Audiencia(fichero):
    '''
    Lee el fichero de entrada y devuelve una lista de audiencias.

    ENTRADA:
        @param fichero: nombre del fichero
        @type fichero: str
    SALIDA:
        @return : lista de audiencia
        @rtype: [Audiencia(int, float)]

    Cada línea del fichero se corresponde con la audiencia de un programa,
    y se representa con una tupla con los siguientes valores:
        - edición
        - audiencia
    Hay que transformar la entrada (cadena de caracteres) en valores numéricos
    para que puedan ser procesados posteriormente
    '''

    audiencias=[]
    with open(fichero, encoding='utf-8') as f:
        # Se crea un objeto lector (un iterator) que separará los valores por comas
        lector = csv.reader(f)
        for edicion, share in lector:
            edicion = int(edicion)
            share = float(share)
            audiencias.append(Audiencia(edicion, share))
        return audiencias