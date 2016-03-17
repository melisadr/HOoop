class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """
    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial_s, tiempo_final_s):
        """
        refleja la senal para que sea detectada por el blanco
        """
        import datetime
        #inicializo senal
        senalmodificada = senal
        if self.tiempo_final <= tiempo_inicial_s or self.tiempo_inicial >= tiempo_final_s:
            # vuelve como estaba
           pass
        elif self.tiempo_inicial > tiempo_inicial_s and \
        self.tiempo_final>tiempo_final_s:
            # aca deberia acortar los tiempos de la senal
            # calculo cantidad_muestras
            print "aca"
            cantidad_muestras=len(senal)
            frecuencia_muestreo = (tiempo_final_s - tiempo_inicial_s).seconds/\
            cantidad_muestras
            muestra1=round((self.tiempo_inicial - tiempo_inicial_s).seconds/\
            frecuencia_muestreo)
            muestraf=round((self.tiempo_final - tiempo_inicial_s).seconds/\
            frecuencia_muestreo)
            rangodecambio=range(muestra1,1,muestraf+1)
            for muestra in rangodecambio:
                senalmodificada[muestra]=senal[muestra]*self.amplitud
        elif self.tiempo_inicial > tiempo_inicial_s:
            print "mal"
            cantidad_muestras=len(senal)
            frecuencia_muestreo = (tiempo_final_s - tiempo_inicial_s).seconds/\
            cantidad_muestras
            muestra1=round((self.tiempo_inicial - tiempo_inicial_s).seconds/\
            frecuencia_muestreo)
            muestraf=cantidad_muestras
            rangodecambio=range(muestra1,1,muestraf+1)
            for muestra in rangodecambio:
                senalmodificada[muestra]=senal[muestra]*self.amplitud
        elif self.tiempo_final>tiempo_final_s:
            print "muymal "   
            cantidad_muestras=len(senal)
            frecuencia_muestreo = (tiempo_final_s - tiempo_inicial_s).seconds/\
            cantidad_muestras
            muestra1=1
            muestraf=round((self.tiempo_final - tiempo_inicial_s).seconds/\
            frecuencia_muestreo)
            rangodecambio=range(muestra1,1,muestraf+1)
            for muestra in rangodecambio:
                senalmodificada[muestra] = senal[muestra]*self.amplitud

        return senalmodificada
