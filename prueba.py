class Cliente:
    def __init__(self,idProducto,tipo):
        self.__idProducto=idProducto
        self.__tipo=tipo
        # self.__listaClientes=[]

class Persona(Cliente):
    def __init__(self,nombre,telefono,direccion):
        self.__nombre=nombre
        self.__telefono=telefono
        self.__direccion=direccion
    
    def getnombre(self):
        return self.__nombre
    def setnombre(self,nombre):
        self.__nombre=nombre
    def gettelefono(self):
        return self.__telefono
    def settelefono(self,telefono):
        self.__telefono=telefono
    def getdireccion(self):
        return self.__direccion
    def settelefono(self,direccion):
        self.__direccion=direccion
    def getCliente(self):
        return self.__nombre

class Empresa(Cliente):
    def __init__(self,nombre,telefono,fax):
        self.__nombre=nombre
        self.__telefono=telefono
        self.__fax=fax
    
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

c1=Persona("Juan Salera",12347424,"Calle 1")
c2=Empresa("CocaCola", 303333333,"42363")
print(c1)
print(c2)