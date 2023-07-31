import random
suma1=0
lista1=[]
tam=random.randint(10,15)
print("El tamaño de la lista 1 es:",tam)
for j in range(tam):
    num1=random.randrange(50)
    lista1.append(num1)
    suma1 += num1
print(lista1)
print("La suma de la lista 1 es: ",suma1)
mayor1=lista1[0]
for j in range(tam):
    if lista1[j]>mayor1:
        mayor1=lista1[j]
menor1=lista1[0]
for j in range(tam):
    if lista1[j]<menor1:
        menor1=lista1[j]
pares1=[]
n1=0
for n in lista1:
    if n % 2 ==n1:
        pares1.append(n1)
impares1=[]
i1=0
for i in lista1:
    if i % 2 !=i1:
        impares1.append(i1)
#####################################
suma2=0
lista2=[]
tam=random.randint(10,15)
print("El tamaño de la lista 2 es:",tam)
for j in range(tam):
    num2=random.randrange(50)
    lista2.append(num2)
    suma2 += num2
print(lista2)
print("La suma de la lista 2 es: ",suma2)
mayor2=lista2[0]
for j in range(tam):
    if lista2[j]>mayor2:
        mayor2=lista2[j]
menor2=lista2[0]
for j in range(tam):
    if lista2[j]<menor2:
        menor2=lista2[j]
prom1=suma1 / len(lista1)
prom2=suma2 / len(lista2)
pares2=[]
n2=0
for n in lista2:
    if n % 2 ==n2:
        pares2.append(n2)
impares2=[]
i2=0
for i in lista2:
    if i % 2 !=i2:
        impares2.append(i2)
#######################################

if mayor2<mayor1:
    print(f"El numero mayor entre las dos listas es {mayor1} y esta en la lista 1")
else:
    print(f"El numero mayor entre las dos listas es {mayor2} y esta en la lista 2")

if menor2>menor1:
    print(f"El numero menor entre las dos listas es {menor1} y esta en la lista 1")
else:
    print(f"El numero menor entre las dos listas es {menor2} y esta en la lista 2")

if suma2<suma1:
    print(f"La suma de la lista 1 es mayor y es {suma1}")
else: 
    print(f"La suma de la lista 2 es mayor y es {suma2}")

print("El promedio de ambas listas es: ",prom1+prom2)

if len(pares2)<len(pares1):
    print (f"La lista 1 tiene mas numeros pares: {len(pares1)}")
else:
    print(f"La lista 2 tiene mas numeros pares: {len(pares2)}")
if len(impares2)<len(impares1):
    print (f"La lista 1 tiene mas numeros impares: {len(impares1)}")
else:
    print(f"La lista 2 tiene mas numeros impares: {len(impares2)}")
