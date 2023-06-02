class Persona:
    def __init__(self,nombre,documento, cursos):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento
        
    def añadeCursos(self,cursos):
        while c != "salir":
            c=input("Añada los cursos a los que pertenece, escriba 'salir' para finalizar: ")
            c.append(cursos)
        return(cursos)
    def muestraDatos(self):
        print("Los datos de la persona son: ")
        return self.__nombre, self.__documento, self.__cursos
        

p=Persona("Timmy",678,2)
print(p.muestraDatos())

q=Persona("Billy",910,1)
print(q.muestraDatos())
