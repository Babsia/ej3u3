from menu import menuu
import numpy
if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a contratar jugador ")
        print("b opcion")
        print("c para salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='c'
        