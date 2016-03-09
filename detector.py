class Detector(object):

    def __init__(self, sensibilidad):
        self.sensibilidad = sensibilidad
        

    def detectar(self, senal):
        """
        Filtro 1: Filtra los valores menores al limite de deteccion
        """
        detectado = False
        for s in senal:
            if s > self.sensibilidad:
                detectado = True
        return detectado
