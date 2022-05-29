class jugador:
    __nombre=''
    __dni=''
    __ciudad=''
    __pais=''
    __fechaN=''
    __contrato=None
    def __init__(self,nom,dni,city,pais,fechan):
        self.__nombre=nom
        self.__dni=dni
        self.__ciudad=city
        self.__pais=pais
        self.__fechaN=fechan
    def agregarcontrato(self,contrato):
        self.__contrato=contrato
    