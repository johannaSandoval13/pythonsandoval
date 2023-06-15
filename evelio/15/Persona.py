class Persona:
    def __init__(self,id,codigo,nombre,direccion,telefono):
        self.id=id
        self.codigo=codigo
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
    def muestraDatos(self):
        print("Los datos de la persona son: ")
        return ("-Id:",self.id,"-Codigo:",self.codigo,"-Nombre:", self.nombre,"-Direccion:",self.direccion,"-Telefono",self.telefono)