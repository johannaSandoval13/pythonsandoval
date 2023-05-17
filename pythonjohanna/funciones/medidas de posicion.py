import random

tam=(random.randint(200,10000))
def llenarLista():
    lista=[]
    lista=[random.randrange(100,500) for i in range(tam)]
    return lista
lista1=llenarLista()

def ordenascendente(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

print(lista1)