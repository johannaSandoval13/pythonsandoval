from Persona import *
from Coordinador import *

print("Instructor 1")
id = input("Ingrese el ID: ")
codigo = input("Ingrese el codigo: ")
nombre = input("Ingrese el nombre: ")
direccion = input("Ingrese la direccion: ")
telefono = input("Ingrese el telefono: ")
fechaIngreso = input("Ingrese la fecha de ingreso: ")
dirOficina = input("Ingrese la direccion de la oficina: ")
nombreCoordinacion = input("Ingrese el nombre de la coordinacion: ")

coordinador1 = Coordinador(id, codigo, nombre, direccion, telefono, fechaIngreso, dirOficina, nombreCoordinacion)
print(coordinador1.muestraDatos())

print("Instructor 2")
id = input("Ingrese el ID: ")
codigo = input("Ingrese el codigo: ")
nombre = input("Ingrese el nombre: ")
direccion = input("Ingrese la direccion: ")
telefono = input("Ingrese el telefono: ")
fechaIngreso = input("Ingrese la fecha de ingreso: ")
dirOficina = input("Ingrese la direccion de la oficina: ")
nombreCoordinacion = input("Ingrese el nombre de la coordinacion: ")


coordinador2 = Coordinador(id, codigo, nombre, direccion, telefono, fechaIngreso, dirOficina, nombreCoordinacion)
print(coordinador2.muestraDatos())
