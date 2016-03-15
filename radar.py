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

        return self.detector.detectar(una_senal_reflejada)


    def plotear_senal(self, tiempo_inicial, tiempo_final):
        import matplotlib.pyplot as pp
        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(cantidad_muestras)
        # agregar un ruido blanco a la senal (done)

        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]+ np.random.normal(0, 1, cantidad_muestras)

        return ret
        una_senal=self.generador.generar( tiempo_inicial, tiempo_final )
        pp.figure()
        pp.plot( muestras, una_senal, color='r', label='X' )
        pp.ylabel('Senal')
        pp.grid(True)
        pp.xlabel('Tiempo')
        pp.title('Senal Modelada')
        pp.show()
