import random

tam=(random.randint(10,15))
def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarLista(10,20)
l2=llenarLista(10,20)

print("Lista 1: ",l1)
print("Lista 2: ",l2)

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum
def comparaSuma(l1,l2):
    if sumaLista(l1)>sumaLista(l2):
        print("La lista con la suma mayor es la L1, que vale:",sumaLista(l1))
    else:
        print("La lista con la suma mayor es la L2, que vale:",sumaLista(l2))
print(comparaSuma(l1,l2))


def mayorLista(lista):
    Nmayor = lista[0]
    for num in lista:
        if num>Nmayor:
            Nmayor=num
    return Nmayor
def comparaMayor(l1,l2):
    if mayorLista(l1)>mayorLista(l2):
        print("La lista con el mayor numero es la L1, cuyo mayor es:",mayorLista(l1))
    else:
        print("La lista con el mayor numero es la L2, cuyo mayor es:",mayorLista(l2))        
print(comparaMayor(l1,l2))


def menorLista(lista):
    Nmenor = lista[0]
    for num in lista:
        if num<Nmenor:
            Nmenor=num
    return Nmenor
def comparaMenor(l1,l2):
    if menorLista(l1)<menorLista(l2):
        print("La lista con el menor numero es la L1, cuyo menor es:",menorLista(l1))
    else:
        print("La lista con el menor numero es la L2, cuyo menor es:",menorLista(l2))
print(comparaMenor(l1,l2))


def promedioLista(lista):
    return sumaLista(lista)/len(lista)
def unirPromedio(l1, l2):
    listaUnida = l1 + l2
    promedio = sum(listaUnida) / len(listaUnida)
    return promedio
print("El promedio de las listas unidas es: ",unirPromedio(l1,l2))


def comparaProm(l1,l2):
    if unirPromedio(l1,l2) < promedioLista(l1):
        print("El promedio de la lista 1 es mayor al promedio conjunto, su valor es: ",promedioLista(l1))
    elif unirPromedio(l1,l2) < promedioLista(l2):
        print("El promedio de la lista 2 es mayor al promedio conjunto, su valor es: ", promedioLista(l2))
    else:
        print("Ninguno de los promedios de las listas es mayor al promedio conjunto")
print(comparaProm(l1,l2))


def agrupaPares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
def comparaPares(l1,l2):
    if agrupaPares(l1) > agrupaPares(l2):
        print("La mayor cantidad de pares esta en la lista 1, la cantidad son:",len(agrupaPares(l1)),"y los numeros son:",agrupaPares(l1))
    else:
        print("La mayor cantidad de pares esta en la lista 2, la cantidad son:",len(agrupaPares(l2)),"y los numeros son:",agrupaPares(l2))
print(comparaPares(l1,l2))


def agrupaImpares(lista):
    impares = []
    for numero in lista:
        if numero % 2 != 0:
            impares.append(numero)
    return impares
def comparaImpares(l1,l2):
    if agrupaImpares(l1) > agrupaImpares(l2):
        print("La mayor cantidad de impares esta en la lista 1, la cantidad son:",len(agrupaImpares(l1)),"y los numeros son:",agrupaImpares(l1))
    else:
        print("La mayor cantidad de impares esta en la lista 2, la cantidad son:",len(agrupaImpares(l2)),"y los numeros son:",agrupaImpares(l2))
print(comparaImpares(l1,l2))

print("Fin del programa ♥")