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
        #pass

    	#TODO WIP agregar el metodo plotear_senal
	
		def plotear_senal(self, tiempo_inicial, tiempo_final):

		"""
		Plotea una senal
		"""
		import matplotlib.pyplot as pp
		# general fechas para plotear
		
		
		pp.figure()
		pp.plot(fechas,senal, color='r',label='X')
		pp.ylabel('Senal')
		pp.grid(True)
		pp.xlabel('Tiempo')
		pp.title('Senal Modelada')
		pp.show()

