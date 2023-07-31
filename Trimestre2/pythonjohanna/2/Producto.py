class Producto:
    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio

    def setNombre(self,nombre):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    def setPrecio(self,precio):
        self.__precio=precio
    def getPrecio(self):
        return self.__precio