class Vehiculo:
    def __init__(self, modelo):
        self.modelo = modelo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo = None

    def comprar_vehiculo(self, vehiculo:Vehiculo):
        self.vehiculo = vehiculo

    def conducir_vehiculo(self):
        if self.vehiculo is not None:
            print(f"{self.nombre} está conduciendo un vehículo {self.vehiculo.modelo}")
        else:
            print(f"{self.nombre} no tiene un vehículo para conducir")

persona1 = Persona("Juan")
vehiculo1 = Vehiculo("Toyota")
persona1.comprar_vehiculo(vehiculo1)
persona1.conducir_vehiculo()

persona2 = Persona("Pedro")
persona2.conducir_vehiculo()

