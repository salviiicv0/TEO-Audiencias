from audiencias import *

def test_lee_audiencias(audiencias, nombre_programa):
    print(f"Audiencias del programa {nombre_programa}")
    print(audiencias[:20])

def main():
    '''
    Función principal
    '''
    #test de la función de lectura de ficheros----------------------
    audiencias_gh = lee_Audiencia('./data/GH.csv')
    test_lee_audiencias(audiencias_gh, "Gran Hermano")

    audiencias_masterchef = lee_Audiencia('./data/MasterChef.csv')
    test_lee_audiencias(audiencias_masterchef, "Master Chef")

if __name__ == "__main__":
    main()