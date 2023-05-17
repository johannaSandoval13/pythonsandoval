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


numCuart=int(input("Ingrese el numero de cuartil a calcular(1 al 4)="))
def calculaCuartil(lista):
    listaOrd = ordenascendente(lista[:]) 
    calcCuartil = int(numCuart * (len(listaOrd) + 1) / 4)
    return listaOrd[calcCuartil]
numQuint=int(input("Ingrese el numero de quintil a calcular(1 al 5)="))
def calculaQuintil(lista):
    listaOrd = ordenascendente(lista[:]) 
    calcQuint = int(numQuint * (len(listaOrd) + 1) / 5)
    return listaOrd[calcQuint]


def crearCuartil(lista, cuartil):
    nuevoCuartil = lista[:cuartil]
    return nuevoCuartil
def crearQuintil(lista, quintil):
    nuevoQuintil = lista[:quintil]
    return nuevoQuintil


def sumaCuartil(lista, cuartil):
    sum=0
    for x in cuartil:
        sum+=x
    return sum
def promedioCuartil(lista, cuartil):
    return sumaCuartil(lista, cuartil)/len(cuartil)


def sumaQuintil(lista, quintil):
    sum=0
    for x in quintil:
        sum+=x
    return sum
def promedioQuintil(lista, quintil):
    return sumaQuintil(lista, quintil)/len(quintil)


l1 = llenarLista(l1)
print(l1)
print("El tamaño de la lista es:", tam)

print("El cuartil que se solicito está en la posición:", calculaCuartil(l1))
cuartil = calculaCuartil(l1)
cuartil = crearCuartil(l1, cuartil)
print("El promedio de el cuartil solicitado es de:",promedioCuartil(l1, cuartil))

print("El quintil que se solicito está en la posición:", calculaQuintil(l1))
quintil= calculaQuintil(l1)
quintil = crearQuintil(l1, quintil)
print("El promedio de el quintil solicitado es de:",promedioQuintil(l1, quintil))