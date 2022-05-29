from ast import While
from contrato import contrato
from manejadorequpio import manejadorE
from datetime import date
from jugadores import jugador
from equipos import equipo
class menuu:
    __switcher=None
    __M=None
    __j=None
    __c=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.salir,
            }
        self.__M=manejadorE()
        self.__M.cargararre()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("opcion a CONTRATAR JUGADOR")
        nombrejugador=input('ingrese el nombre del jugador: ')
        dni=input('ingrese el dni: ')
        city=input('ingrese la ciudad: ')
        country=input('ingrese el pais: ')
        print('ingrese la fecha de nacimiento:')
        dia=int (input('ingrese el dia: '))
        mes=int(input(" ingrse el mes: "))
        year=int(input('ingrese el año: '))
        fecha=date(year,mes,dia)
        print(fecha)
        unjugador=jugador(nombrejugador,dni,city,country,fecha)
        idEQ=input('ingrese el nombre del equipo: ')
        i=self.__M.buscarequipo(idEQ)
        while(i==-1):
           idEQ= input('no se encontro ese equipo ingrese otro: ')
           i=self.__M.buscarequipo(idEQ)
        equipo=self.__M.extraerequipo(i)
        print('CREAR CONTRATO')
        
        print('Fecha de Inicio')
        diac=int(input('ingrese el dia: '))
        mesc=int(input('ingrese el mes: '))            
        yearc=int(input('ingrese el año: '))
        fechainicio=date(yearc,mesc,diac)
        print('Fecha final')
        diacf=int(input('ingrese el dia: '))
        mescf=int(input('ingrese el mes: '))            
        yearcf=int(input('ingrese el año: '))
        fechafinal=date(yearcf,mescf,diacf)
        while (fechainicio>fechafinal):
            print('fecha de inicio mayor que fecha final')
            print('Fecha de Inicio')
            diac=int(input('ingrese el dia: '))
            mesc=int(input('ingrese el mes: '))            
            yearc=int(input('ingrese el año: '))
            fechainicio=date(yearc,mesc,diac)
            print('Fecha final')
            diacf=int(input('ingrese el dia: '))
            mescf=int(input('ingrese el mes: '))            
            yearcf=int(input('ingrese el año: '))
            fechafinal=date(yearcf,mescf,diacf)
        uncontrato=contrato(fechainicio,fechafinal)
        










        
       
        
    def opcion2(self):
        print("opcion b")