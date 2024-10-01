from audiencias import *

def test_lee_audiencias(audiencias, nombre_programa):
    print(f"Audiencias del programa {nombre_programa}")
    print(audiencias[:20])

def test_calcula_ediciones(audiencias, nombre_programa):
    ediciones = calcula_ediciones(audiencias)
    print(f"Número de ediciones del program {nombre_programa}: {ediciones}")

def test_filtra_por_ediciones(audiencias, ediciones, nombre_programa):
    filtradas = filtra_por_ediciones(audiencias, ediciones)
    print(f"Los datos de las ediciones {ediciones} del programa {nombre_programa} son: \n {filtradas}")

def test_agrupa_por_ediciones(audiencias, nombre_programa):
    dicc = agrupa_share_por_ediciones(audiencias)
    print(f"Agrupación por ediciones del programa {nombre_programa}: \n{dicc}")

def test_medias_por_ediciones(audiencias, nombre_programa):
    dicc = medias_por_ediciones(audiencias)
    print(f"La media por ediciones del programa {nombre_programa} es: \n{dicc}")

def main():
    '''
    Función principal
    '''
    #test de la función de lectura de ficheros----------------------
    audiencias_gh = lee_Audiencia('./data/GH.csv')
    test_lee_audiencias(audiencias_gh, "Gran Hermano")

    audiencias_masterchef = lee_Audiencia('./data/MasterChef.csv')
    test_lee_audiencias(audiencias_masterchef, "Master Chef")
    #test de la función calcula ediciones
    test_calcula_ediciones(audiencias_gh, "Gran Hermano")
    test_calcula_ediciones(audiencias_masterchef, "Master Chef")
    #test de la función filtra_por_ediciones
    test_filtra_por_ediciones(audiencias_gh, [1,2,3], "Gran Hermano")
    test_filtra_por_ediciones(audiencias_masterchef, [4,5], "Master Chef")
    #test de la función agrupa_por_ediciones
    test_agrupa_por_ediciones(audiencias_gh, "Gran Hermano")
    test_agrupa_por_ediciones(audiencias_masterchef, "Master Chef")
    #test de la función media_por_ediciones
    test_medias_por_ediciones(audiencias_gh, "Gran Hermano")
    test_medias_por_ediciones(audiencias_masterchef, "Master Chef")



if __name__ == "__main__":
    main()
