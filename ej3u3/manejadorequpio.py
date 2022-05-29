import numpy 
import csv
from equipos import equipo


class manejadorE:
    __cantidad = 0
    __equipos = None
    __dimension= 0
    __incremento=5
    def __init__(self):
        self.__cantidad = 0
        self.__dimension=0
        self.__equipos = numpy.empty(0, dtype=equipo)
    
    def agregarequipo(self,equipos):
        if isinstance(equipos, equipo):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__camas.resize(self.__dimension)
            self.__equipos[self.__cantidad] = equipos
            self.__cantidad += 1
    def cargararre(self):
        archivo= open('Equipos.csv')
        reader=csv.reader(archivo,delimiter=';')
        cantidad=int(next(reader)[0])
        self.__dimension=cantidad
        self.__equipos.resize(cantidad)
        for fila in reader:
            e=equipo(fila[0],fila[1])
            self.agregarequipo(e)
    
    def buscarequipo(self,name):
        i = 0
        while i < len(self.__equipos) and self.__equipos[i].getname() != name:
            i += 1
        if i == len(self.__equipos):
            i = -1
        return i
    def extraerequipo(self,indice):
        return self.__equipos[indice]