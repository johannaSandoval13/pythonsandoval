from cli import *

class Persona(Cliente):
    def __init__(self,nombre,telefono,direccion):
        super().__init__(nombre,telefono)
        self.__nombre=nombre
        self.__telefono=telefono
        self.__direccion=direccion
        self.__prod=[]
        
    def agregarProducto(self,producto):
        self.__prod.append(producto)
        
    def getProducto(self):
        return self.__prod
