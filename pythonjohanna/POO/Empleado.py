class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo
    def getSalario(self):
        return self.__salario
    def setSalario(self,salario):
        self.__salario=salario
        
    def añadeNombre(self):
        nom = input("escriba su nombre: ")
    def añadeCargo(self):
        car = input("escriba su cargo: ")   
    def añadeSalario(self):
        car = input(int("escriba su salario: "))   

n1= Empleado(Empleado.añadeNombre,Empleado.añadeCargo,Empleado.añadeSalario)
n1.añadeNombre
n1.añadeCargo
n1.añadeSalario
