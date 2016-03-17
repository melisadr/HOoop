"""
Define el similador del Radar
"""


class Radar(object):
    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector


    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """

        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)

        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        tiempo_final)

#        return self.detector.detectar(una_senal_reflejada)
        return una_senal_reflejada


    def plotear_senal(self,una_senal_reflejada,tiempo_inicial, tiempo_final):
        import matplotlib.pyplot as pp
        cantidad_muestras = len(una_senal_reflejada)
        muestras = range(cantidad_muestras)
        pp.figure()
        pp.plot( muestras, una_senal_reflejada, color='r', label='X' )
        pp.ylabel('Senal')
        pp.grid(True)
        pp.xlabel('Tiempo')
        pp.title('Senal Modelada')
        pp.show()
