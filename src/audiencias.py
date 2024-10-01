import csv # Para leer los csv de datos
from matplotlib import pyplot as plt # Para mostrar gráficas, importamos matplotlib.pyplot, renombrándolo como plt
from collections import namedtuple # Para definir tuplas con nombre
Audiencia = namedtuple ("Audiencia", "edicion, share")

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
    
def calcula_ediciones(audiencias):
    '''
    Calcula el número de ediciones presentes en una lista de audiencias

    ENTRADA:
        @param audiencias: lista de tuplas de audiencias
        @type audiencias: [Audiencias(int, float)]
    SALIDA:
        @return: El número de ediciones del programa
        @rtype: int

    Toma como entrada una lista de tuplas (edición, share) y produce como
    salida el número de ediciones del programa
    Solución utilizando una definición de audiencias por compresión
    '''

    #calculamos el conjunto de ediciones presentes
    ediciones = set()
    for a in audiencias:
        ediciones.add(a.edicion)

    #devolvemos el tamaño del conjunto
    return len(ediciones)

def filtra_por_ediciones(audiencias, ediciones):
    '''
    Selecciona las tuplas correspondientes a unas determinadas ediciones

    ENTRADA:
        @param audiencias: lista de audiencias
        @type audiencias: [Audiencia(int, float)]
        @param ediciones: lista de ediciones a seleccionar
        @type ediciones:  [int]

    SALIDA:
        @return: lista de tuplas de audiencias seleccionadas
        @rtype: [Audiencias(int, float)]
    '''
    filtradas = []
    for a in audiencias:
        if a.edicion in ediciones:
            filtradas.append(a)
    return filtradas

def agrupa_share_por_ediciones(audiencias):
    '''
    Para una lista de tuplas de audiencias, agrupa los valores de share por edición en un diccionario.

    ENTRADA:
        @param audiencias: lista de tuplas (edicion, share) con las audiencias de un programa de televisión
        @type audiencias: [Audiencias(int, float)]
    SALIDA:
        @return: Un diccionario en el que las claves son las ediciones y los valores son listas de shares de cada edición
        @rtype: {int:[float]}
    '''
    res = dict() #Crea diccionario vacío, también se puede hacer res = {}
    for a in audiencias:
        if a.edicion in res:
            #Si la edición ya está en el diccionario
            res[a.edicion].append(a.share) #Se añade el share a la lista de shares asociada a esa edición
        else:
            #Si la edición no está en el diccionario
            res[a.edicion] = [a.share] # Se crea una nueva lista con el share y se asocia a la edición
    return res

def medias_por_ediciones(audiencias):
    '''
    Calcula la media de audiencia para cada edición

    ENTRADA:
        @param audiencias: lista de audiencias
        @type audiencias: [Audiencia(int, float)]
    SALIDA:
        @return: medias de audiencia por cada edición
        @rtype: {int: float}

    Toma como entrada una lista de tuplas (edición, share) y produce como
    salida un diccionario en el que las claves son las ediciones y los
    valores son las medias de audiencia de cada edición.
    '''

    share_por_ediciones = agrupa_share_por_ediciones(audiencias)
    medias = dict()
    for edicion, lista_shares in share_por_ediciones.items():
        medias[edicion] = sum(lista_shares) / len(lista_shares)
    return medias