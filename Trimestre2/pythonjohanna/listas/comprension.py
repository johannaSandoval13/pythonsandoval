#par=raiz impar=elevado 

import random
from math import sqrt
tam=random.randint(10,20)
lista=[random.randrange(100) for i in range(tam)]
print(lista)
par=[x for x in lista if x%2==0]
print("Los numeros pares son: ",par)
impar=[x for x in lista if x%2!=0]
print("Los numeros impares son: ",impar)
raiz=[sqrt(i) for i in par]
print("La raiz de los numeros pares es:",raiz)
cuadrado=[i**2 for i in impar]
print("La elevacion al cuadrado de los numeros impares es:",cuadrado)