from Persona import *

class Coordinador(Persona):
    def __init__(self,fechaIngreso,dirOficina,nombreCoordinacion,id,codigo,nombre,direccion,telefono):
        super().__init__(id,codigo,nombre,direccion,telefono)
        self._fechaIngreso = fechaIngreso
        self._dirOficina = dirOficina
        self._nombreCoordinacion = nombreCoordinacion

    def getfechaIngreso(self):
        return self._fechaIngreso
    def setfechaIngreso(self,fechaIngreso):
        self._fechaIngreso=fechaIngreso
    def getdirOficina(self):
        return self._dirOficina
    def setdirOficina(self,dirOficina):
        self._dirOficina=dirOficina
    def getnombreCoordinacion(self):
        return self._nombreCoordinacion
    def setnombreCoordinacion(self,nombreCoordinacion):
        self._nombreCoordinacion=nombreCoordinacion
        
    def muestraDatos(self):
        print("Los datos de la persona son: ")
        return ("-ID",self.id,"-Codigo",self.id,"-Nombre",self.nombre,"-Direccion oficina",self._dirOficina,"-Fecha de ingreso",self._fechaIngreso,
                "-Nombre de Coordinacion",self._nombreCoordinacion)

