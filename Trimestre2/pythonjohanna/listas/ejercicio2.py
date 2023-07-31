import random
lista=[]
tam=random.randint(15,20)
print("El tamaño de la lista es:",tam)
for j in range(tam):
    num=random.randrange(0,9)
    lista.append(num)
print(lista)

ingreso=int(input("Ingrese un numero: "))

esta=lista[0]
for j in range(tam):
    if lista[j]==ingreso:
        print(f"{ingreso} Esta en la lista")
        break


for i in range(len(lista)):
    if ingreso == lista[i]:
        print(f'{lista[i]} esta en la posicion {i}')
