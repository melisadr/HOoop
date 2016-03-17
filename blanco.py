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
            print "caso 1"
            # vuelve como estaba
            senalmodificada = senal
        elif self.tiempo_inicial >= tiempo_inicial_s and \
        self.tiempo_final<=tiempo_final_s:
            print "caso 2"
            # aca deberia acortar los tiempos de la senal
            cantidad_muestras=len(senal)
            frecuencia_muestreo = (tiempo_final_s - tiempo_inicial_s).seconds/\
            cantidad_muestras
            muestra1=int(round((self.tiempo_inicial - tiempo_inicial_s).seconds/\
            frecuencia_muestreo))
            muestraf=int(round((self.tiempo_final - tiempo_inicial_s).seconds/\
            frecuencia_muestreo))
            rangodecambio=range(muestra1,muestraf+1,1)
            for muestra in rangodecambio:
                senalmodificada[muestra]=senal[muestra]*self.amplitud
        elif self.tiempo_inicial < tiempo_inicial_s and \
        self.tiempo_final>tiempo_final_s:
            print "caso 4"
            senalmodificada=senal*self.amplitud
        elif self.tiempo_inicial < tiempo_inicial_s:
            print "caso 3"
            cantidad_muestras=len(senal)
            frecuencia_muestreo = (tiempo_final_s - tiempo_inicial_s).seconds/\
            cantidad_muestras
            muestra1=1
            muestraf=int(round((self.tiempo_final - tiempo_inicial_s).seconds/\
            frecuencia_muestreo))
            #int(cantidad_muestras)
            print muestra1 
            print muestraf
            rangodecambio=range(muestra1,muestraf+1,1)
            print rangodecambio
            for muestra in rangodecambio:
                senalmodificada[muestra]=senal[muestra]*self.amplitud
        elif self.tiempo_final>tiempo_final_s:
            print "caso 4"
            cantidad_muestras=len(senal)
            frecuencia_muestreo = (tiempo_final_s - tiempo_inicial_s).seconds/\
            cantidad_muestras
            muestra1=int(round((self.tiempo_inicial - tiempo_inicial_s).seconds/\
            frecuencia_muestreo))
            muestraf=int(cantidad_muestras)
            rangodecambio=range(muestra1,muestraf,1)
            for muestra in rangodecambio:
                senalmodificada[muestra] = senal[muestra]*self.amplitud
        return senalmodificada
