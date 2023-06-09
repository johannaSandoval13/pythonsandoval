from cli import *

class Empresa(Cliente):
    def __init__(self,nombre,telefono,fax):
        super().__init__(idProducto,tipo)
        self.__nombre=nombre
        self.__telefono=telefono
        self.__fax=fax
        self.__listaProductos=[]
    
    def getnombre(self):
        return self.__nombre
    def setnombre(self,nombre):
        self.__nombre=nombre
    def gettelefono(self):
        return self.__telefono
    def settelefono(self,telefono):
        self.__telefono=telefono
    def getfax(self):
        return self.__fax
    def setfax(self,fax):
        self.__fax=fax