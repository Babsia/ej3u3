from manejadorequpio import manejadorE
class menuu:
    __switcher=None
    __M=None

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
        
        
       
        
    def opcion2(self):
        print("opcion b")