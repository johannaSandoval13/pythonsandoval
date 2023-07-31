#!/usr/bin/env python3 
"""module : listas"""

import random
lista=[]
tam=random.randint(5,10)
for j in range(tam):
    num=random.randrange(25)
    lista.append(num)
print("Esta es una lista creada aleatoriamente :)",lista)
###
def sumar_lista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum
print("La suma de esta lista es: ",sumar_lista(lista))
###
def promedio_lista(lista):
    return sumar_lista(lista)/len(lista)
print("El promedio es: ",promedio_lista(lista))
###
def mayor_lista(lista):
    Nmayor = lista[0]
    for num in lista:
        if num>Nmayor:
            Nmayor=num
    return Nmayor
print("El numero mayor es: ",mayor_lista(lista))
###
def menor_lista(lista):
    Nmenor = lista[0]
    for num in lista:
        if num<Nmenor:
            Nmenor=num
    return Nmenor
print("El numero menor es: ",menor_lista(lista))
###
def orden_ascendente(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista
print("La lista en orden ascendente es: ",orden_ascendente(lista))

###
def orden_descendente(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i + 1, tam):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista
print("La lista en orden descendente es: ",orden_descendente(lista))