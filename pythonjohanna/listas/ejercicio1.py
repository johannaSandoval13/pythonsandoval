import random
from math import sqrt
suma=0
suma2=0
raiz=0
lista=[]
tam=random.randint(10,20)
print("El tamaño de la lista es:",tam)
for j in range(tam):
    num=random.randrange(100)
    lista.append(num)
    suma += num
mayor=lista[0]
for j in range(tam):
    if lista[j]>mayor:
        mayor=lista[j]
menor=lista[0]
for j in range(tam):
    if lista[j]<menor:
        menor=lista[j]
moda=[]
for i in range (len(lista)):
    for u in range (len(lista)):
        if i != u:
            if lista[i]==lista[u] and lista[i] not in moda:
                moda.append(lista[i])
prom=suma // len(lista) 

desvi1=[]
for n in range(tam):
            resta=prom-num
            desvi1.append(resta)
desvi2=[]
for n in range(tam):
     cuadrado=resta**2
     desvi2.append(cuadrado)
     suma2+=cuadrado

raiz=sqrt(suma2//tam-1)


print(lista)
print("La suma de los numeros en la lista es: ",suma)
print("El mayor de la lista es: ",mayor)
print("El menor de la lista es: ",menor)
print("El promedio es: ",prom)
print("La moda es: ",moda)
print("//Desviacion estandar//")
print("La resta entre los numeros de la lista y el promedio es: ",desvi1)
print("El cuadrado de las restas es: ", desvi2)
print("La desviacion estandar es: ",raiz)