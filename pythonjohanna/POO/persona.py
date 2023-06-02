class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento
    
p=Persona("Timmy",678)
print(p.getNombre())
print(p.getDocumento())

q=Persona("Billy",910)
print(q.getNombre())
print(q.getDocumento())