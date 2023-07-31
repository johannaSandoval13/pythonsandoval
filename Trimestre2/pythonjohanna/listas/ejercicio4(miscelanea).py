#Llenar un arreglo de n elementos con números generados con la función random. No
#puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe,
#imprimirlo para anunciar que ese número ya está en el arreglo.
import random
n=int(input("Escribe un numero del uno al 20, si ya esta en la lista debes intentarlo de nuevo: "))

lista=[]
tam=random.randint(5,6)
for j in range(tam):
    num=random.randrange(20)
    lista.append(num)
#print(lista)
repetido=lista[0]
for j in range(tam):
 while n == lista[j]:
        repetido=lista[j]
        n=int(input("Escribe un numero del uno al 20, si ya esta en la lista debes intentarlo de nuevo: "))
print("El numero escrito no esta en la lista")
print("La lista es: ",lista)