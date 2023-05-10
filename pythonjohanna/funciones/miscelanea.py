import random
tam=(random.randint(10,15))
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

def ordenascendente (lista,tam):
    for i in range(len(lista)):
     for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
    return lista

l1=llenarLista(10,20)
l2=llenarLista(10,20)
print("Lista 1: ")
print(l1)
print(sumaLista(l1))
print(promedioLista(l1))
print(mayorLista(l1))
print(menorLista(l1))
print(ordenascendente(l1,tam))
print("Lista 2: ")
print(l2)
print(sumaLista(l2))
print(promedioLista(l2))
print(mayorLista(l2))
print(menorLista(l2))
print(ordenascendente(l2,tam))