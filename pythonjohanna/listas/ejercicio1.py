import random
lista=[]
suma=0
tam=random.randint(10,20)
print("El tamaño de la lista es:",tam)
for j in range(tam):
    num=random.randrange(100)
    lista.append(num)
    suma += num
mayor=lista[0]
for j in range(tam):
    if lista[j]>mayor:
        mayor=lista[j]
menor=lista[0]
for j in range(tam):
    if lista[j]<menor:
        menor=lista[j]

   
print(lista)
print("La suma de los numeros en la lista es: ",suma)
print("El mayor de la lista es: ",mayor)
print("El menor de la lista es: ",menor)