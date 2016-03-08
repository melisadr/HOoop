class Detector(object):

    def __init__(self, sensibilidad):
        #TODO: completar con la inicializacion de los parametros del objeto
        self.sensibilidad = sensibilidad
        

    def detectar(self, senal):
        detectado = False
        for s in senal:
            if s > self.sensibilidad:
                detectado = True
        #TODO: Completar (pasa si es true or false)
        return detectado
