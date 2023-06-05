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

    def añadeCursos(self):
        cursos = []
        while True:
            c = input("Añada los cursos , escriba 'salir' para finalizar: ")
            if c == "salir":
                break
            cursos.append(c)
        self.__cursos = cursos
        
    def muestraDatos(self):
        print("Los datos de la persona son: ")
        return ("-Nombre:", self.__nombre, "-Documento:", self.__documento, "-Cursos:", self.__cursos)
        
    def eliminaCursos(self):
        while True:
            e = input("escriba el indice a eliminar, escriba 'salir' para finalizar: ")
            if e == "salir":
                break
            index = int(e)
            del self.__cursos[index]
    def modificaCursos(self):
        cursos = []
        while True:
            m = input("escriba el indice a modificar, escriba 'salir' para finalizar: ")
            if m == "salir":
                break
            index = int(m)
            nvCurso = input("Ingrese el nuevo curso: ")
            self.__cursos[index] = nvCurso



p = Persona("Timmy", 678, [2])
p.añadeCursos()
print(p.muestraDatos())
p.eliminaCursos()
p.modificaCursos()
print(p.muestraDatos())

q = Persona("Billy", 910, [1])
q.añadeCursos()
print(q.muestraDatos())
q.eliminaCursos()
q.modificaCursos()
print(q.muestraDatos())
