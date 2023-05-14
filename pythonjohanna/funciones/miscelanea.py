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

def ordenascendente(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def ordendescendente(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i + 1, tam):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def modaLista (lista):
    conteo = {}
    repeticiones = 0
    for i in lista:
        if i in conteo:
            conteo[i] += 1
        else:
            conteo[i] = 1
        if conteo[i] > repeticiones:
            repeticiones = conteo[i]
    moda = []
    for i, num_repeticiones in conteo.items():
        if num_repeticiones == repeticiones:
            moda.append(i)
def buscar(lista):
    while True:
        numero = int(input("Ingrese un número, le diremos si esta en la lista: "))
        if numero in lista:
            print("Sí, el número", numero, "está en la lista.")
            break
        else:
            print("El número", numero, "no está en la lista. Inténtalo nuevamente.")

l1=llenarLista(10,20)
l2=llenarLista(10,20)
print("Lista 1: ")
print(l1)
print("La suma de la lista es:",sumaLista(l1))
print("El promedio es: ",promedioLista(l1))
print("El numero mayor es: ",mayorLista(l1))
print("El numero menor es: ",menorLista(l1))
print("La lista en orden ascendente es: ",ordenascendente(l1))
print("La lista en orden descendente es: ",ordendescendente(l1))
print("La moda es: ",modaLista(l1))
print(buscar(l1))
print("Lista 2: ")
print(l2)
print("La suma de la lista es:",sumaLista(l2))
print("El promedio es: ",promedioLista(l2))
print("El numero mayor es: ",mayorLista(l2))
print("El numero menor es: ",menorLista(l2))
print("La lista en orden ascendente es: ",ordenascendente(l2))
print("La lista en orden descendente es: ",ordendescendente(l2))
print("La moda es: ",modaLista(l2))
print(buscar(l2))