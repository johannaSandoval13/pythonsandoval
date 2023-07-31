from individual import *
from empresa import *
from Producto import *

i1=Individual("Tommy", 123, "calle 3","Individual")
prod1= Producto("Papel",20000)
prod2= Producto("Esferos", 15000)
i1.agregarProducto(prod1)
i1.agregarProducto(prod2)
print("El nombre de la persona es:",i1.getNombre())
print("la direccion de la persona es:",i1.getDireccion())

for prod in i1.getProducto():
    print(prod.getNombre())
del i1

e1=Empresa("Panamericana",9999,"calle 8","Empresa")
prod1= Producto("Libros",110000)
prod2= Producto("Lapices",60000)
e1.agregarProducto(prod1)
e1.agregarProducto(prod2)
print("El nombre de la Empresa es:",e1.getNombre())
print("la direccion de la Empresa es:",e1.getDireccion())

for prod in e1.getProducto():
    print(prod.getNombre())

del e1