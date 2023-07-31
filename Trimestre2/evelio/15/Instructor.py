from Persona import *

class Instructor(Persona):
    def __init__(self,profesion,especialidad,cargo,salario_basico,id,codigo,nombre,direccion,telefono):
        super().__init__(id,codigo,nombre,direccion,telefono)
        self.__profesion = profesion
        self.__especialidad = especialidad
        self.__cargo = cargo
        self.__salario_basico = salario_basico
        
    def getNombre(self):
        return self.__profesion
    def setNombre(self,profesion):
        self.__profesion=profesion
    def getEspecialidad(self):
        return self.__especialidad
    def setEspecialidad(self,especialidad):
        self.__especialidad=especialidad
    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo
    def getSalario(self):
        return self.__salario
    def setSalario(self,salario_basico):
        self.__salario_basico=salario_basico
        
    def muestraDatos(self):
        print("Los datos de la persona son: ")
        return ("-Id:", self.id, "-Codigo:", self.codigo, "-Nombre:", self.nombre, "-Direccion:", self.direccion,
                "-Telefono", self.telefono, "-Profesion:", self.__profesion, "-Especialidad:", self.__especialidad,
                "-Cargo:", self.__cargo, "-Salario:", self.__salario_basico)