class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud=amplitud
        self.tiempo_inicial=tiempo_inicial
        self.tiempo_final=tiempo_final

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
	"""
"""        
import datetime
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        if self.tiempo_inicial >= tiempo_final or \
        tiempo_final<=senal.tiempo_inicial:
	# puedo dejar la funcion sin nada, porque si los tiempos no se cruzan no devuelve senal, cierto?
            pass       
        elif tiempo_inicial > senal.tiempo_inicial:
            # aca deberia acortar los tiempos de la senal
            pass
        
        elif tiempo_final>senal.tiempo_final:
            # idem anterior
            pass
        else:
            #ver si es esto lo que significa amplitud pero entiendo que hay 
            # que cambiar la amplitud de la senal
            #como hago para pasarle los nuevos tiempos de esa senal?
            # pasa la senal completa 
           
            senalmodificada=self.amplitud*senal    
         
        return senalmodificada
