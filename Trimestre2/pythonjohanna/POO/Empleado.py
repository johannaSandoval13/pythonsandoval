class Empleado:
    contador = 0
    tSalarios= 0
    prom=0
    def __init__(self,nombre,cargo,salario):
        Empleado.contador+=1
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        Empleado.tSalarios+=salario
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
        self.__nombre = input("escriba su nombre: ")
    def añadeCargo(self):
        self.__cargo= input("escriba su cargo: ")   
    def añadeSalario(self):
        nv_salario = float(input("escriba su salario: "))
        Empleado.tSalarios += self.__salario
        self.__salario = nv_salario
        Empleado.tSalarios += self.__salario
    def muestraDatos(self):
        print("Los datos de la persona son: ")
        return ("-Nombre:", self.__nombre, "-Cargo:", self.__cargo, "-Salario:", self.__salario)
    def dividirSalario(self):
        d= self.__salario // 30
        return("este empleado gana",d,"por hora")
    def ipc(self):
        i=0
        if self.__salario > 1160000:
            i=self.__salario * 0.1312
            return("El salario de este empleado con IPC es:",i)
        else:
            i=self.__salario*0.4312
            return("El salario de este empleado con IPC es:",i)
    def registrarHorasExtra(self):
        horas_extra = int(input("Ingrese la cantidad de horas extra trabajadas (máximo 2): "))
        if horas_extra > 2:
            print("No es válido.")
        else:
            self.dividirSalario += int(0.25 * horas_extra)
            print("Se han registrado las horas extra correctamente.")
    def horasE(self):
        e= self.__salario // 30
        horas_extra = int(input("Ingrese la cantidad de horas extra trabajadas (máximo 2): "))
        if horas_extra > 2:
            print("No es válido.")
        else:
            e + int(0.25 * horas_extra)
            print("El valor de las horas extra es:",e)
    def salariosT():
        return Empleado.tSalarios
    def calcularProm():
        Empleado.prom = Empleado.tSalarios / Empleado.contador
    def resulProm():
        return Empleado.prom

empleado1 = Empleado("", "", 0)
empleado1.añadeNombre()
empleado1.añadeCargo()
empleado1.añadeSalario()
print(empleado1.muestraDatos())
print(empleado1.dividirSalario())
print(empleado1.ipc())
print(empleado1.horasE())
print(Empleado.contador)

empleado2 = Empleado("", "", 0)
empleado2.añadeNombre()
empleado2.añadeCargo()
empleado2.añadeSalario()
print(empleado2.muestraDatos())
print(empleado2.dividirSalario())
print(empleado2.ipc())
print(empleado2.horasE())

print("Total de salarios registrados:", Empleado.salariosT())
Empleado.calcularProm()
print("Promedio de salarios:", Empleado.resulProm())