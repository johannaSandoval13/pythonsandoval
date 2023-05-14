import random

def verificar():
    n = int(input("Escribe un número del uno al 20, si ya está en la lista debes intentarlo de nuevo: "))
    lista = []
    tam = random.randint(5, 6)
    for j in range(tam):
        num = random.randrange(20)
        lista.append(num)
    repetido = lista[0]
    for j in range(tam):
        while n == lista[j]:
            repetido = lista[j]
            n = int(input("Escribe un número del uno al 20, si ya está en la lista debes intentarlo de nuevo: "))
    print("El número escrito no está en la lista.")
    print("La lista es:", lista)

verificar()
