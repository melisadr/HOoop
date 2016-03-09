#import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    # construir un nuevo genrador de senales
    generador1=generador.Generador(amplitud,fase,frecuencia)
    # construir un detector
    sensibilidad= 0.01
    detector1=detector.Detector(sensibilidad)
    # construir un nuevo radar
    miradar=radar.Radar(generador1,detector1)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #TODO construir un nuevo blanco
    nuevoblanco=blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco ,tiempo_final_del_blanco)

    #TODO construir un medio
    una_senal=generador1.Generador.generar(tiempo_inicial, tiempo_final)
    medio1=medio.Medio(una_senal, tiempo_inicial, tiempo_final)

    #TODO construir un radar


if __name__ == "__main__":
    main()
