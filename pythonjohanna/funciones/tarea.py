import random
l1=[]

tam=(random.randint(200,2000))
def llenarLista(lista):
    lista=[]
    lista=[random.randrange(100,500) for i in range(tam)]
    return lista

def ordenascendente(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


numCuart=int(input("Ingrese el numero de cuartil a calcular="))
def calculaCuartil(lista):
    listaOrd = ordenascendente(lista[:]) 
    calcCuartil = int(numCuart * (len(listaOrd) + 1) / 4)
    return listaOrd[calcCuartil]


numQuint=int(input("Ingrese el numero de quintil a calcular="))
def calculaQuintil(lista):
    listaOrd = ordenascendente(lista[:]) 
    calcQuint = int(numQuint * (len(listaOrd) + 1) / 5)
    return listaOrd[calcQuint]

def crearNuevaLista(lista, cuartil):
    if numCuart != 1:
        nuevaLista = lista[calculaCuartil:cuartil]
    else:
        nuevaLista = lista[:cuartil]
        return nuevaLista



l1 = llenarLista(l1)
print(l1)
print("El tamaño de la lista es:", tam)
print("El cuartil que se solicito está en la posición:", calculaCuartil(l1))
cuartil = calculaCuartil(l1)
print("El quintil que se solicito está en la posición:", calculaQuintil(l1))
cuartil = crearNuevaLista(l1, cuartil)
print("Nueva lista:", cuartil)