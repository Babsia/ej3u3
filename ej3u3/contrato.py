from jugadores import jugador
from equipos import equipo


class contrato:
    __fechaI=''
    __fechaF=''
    __pago=''
    __equipo=None
    __jugador=None
    def __init__(self,inicio,final) :
        self.__fechaI=inicio
        self.__fechaF=final
