from cli import *

class Empresa(Cliente):
    def __init__(self,nombre,telefono,direccion,tipo):
        super().__init__(nombre,telefono,tipo)
        self.__nombre=nombre
        self.__telefono=telefono
        self.__direccion=direccion
        self.__tipo=tipo
        self.__prod=[]

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getDireccion(self):
        return self.__direccion
    def setDireccion(self, direccion):
        self.__direccion=direccion
        
    def agregarProducto(self,producto):
        self.__prod.append(producto)
        
    def getProducto(self):
        return self.__prod
