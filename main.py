# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():
    import radar
    import medio
    import blanco
    import generador
    import datetime
    import detector
    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.4
    fase = 1
    frecuencia = 10*math.pi

    # construir un nuevo genrador de senales
    generador1=generador.Generador(amplitud,fase,frecuencia)
    # construir un detector
    sensibilidad= 0.04
    detector1=detector.Detector(sensibilidad)
    # construir un nuevo radar
    miradar=radar.Radar(generador1,detector1)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 10
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 3)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 6)
    #TODO construir un nuevo blanco
    una_senal=generador1.generar(tiempo_inicial,tiempo_final)
    nuevoblanco=blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco ,tiempo_final_del_blanco)
    una_senal_reflejada=nuevoblanco.reflejar(una_senal, tiempo_inicial, tiempo_final)
#    print una_senal
#    print una_senal_reflejada
    
    #TODO construir un medio
    medio1=medio.Medio(nuevoblanco)

    #TODO construir un radar
#    una_senal_reflejada = miradar.detectar(medio1, tiempo_inicial, tiempo_final)
    miradar.plotear_senal(una_senal_reflejada,tiempo_inicial, tiempo_final)
#    miradar.plotear_senal(una_senal,tiempo_inicial, tiempo_final)

if __name__ == "__main__":
     main()
