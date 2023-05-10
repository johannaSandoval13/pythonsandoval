import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayorLista(lista):
    Nmayor = lista[0]
    for num in lista:
        if num>Nmayor:
            Nmayor=num
    return Nmayor
def menorLista(lista):
    Nmenor = lista[0]
    for num in lista:
        if num<Nmenor:
            Nmenor=num
    return Nmenor
def OrdenALista(lista):
    

l1=llenarLista(10,20)
print(l1)
print(sumaLista(l1))
print(promedioLista(l1))
print(mayorLista(l1))
print(menorLista(l1))