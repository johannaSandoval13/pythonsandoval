num=1
cont=0
#Aqui se le asigno el valor 0 al contador, por ahora
sum=0
#Aqui se le asigno el valor cero a la variable sum, por ahora
menor=0
#Aqui se establece que el menor numero del programa sera 0,
mayor=1000000
#y el mayor 1000000
while num!=0:
#Mientras que num sea diferente que 0
    num=int(input('ingrese numero'))
#El usuario debera ingresar un numero
    cont=cont+1
#Aqui el contador aumentara de uno en uno
    sum=sum+num
#y aqui el acumulador sumara todos los numeros almacenados en el contador
    if num>mayor:
        mayor=num
#Si num es mayor que el maximo valor disponible, se almacenara el valor maximo en num
    if num<menor and num!=0:
        menor=num
#y si num es menor que el menor valor disponible y este es distino de cero, se almacenara el valor minimo en num

print(f'fueron ingresados {cont-1} numeros')
#Aqui se imprimira el numero de numeros (Valga la redundancia) registrados
print(f'La suma es {sum}')
#Aqui se imprimira el resultado de la suma de los numeros registrados
print(f'El promedio es {sum/(cont-1)}')
#Aqui se imprimira el promedio de los numeros registrados
print(f'El mayor es {mayor}')
#Aqui se imprimira el mayor de los numeros registrados
print(f'El menor es {menor}')
#y por ultimo, se imprimira el menor de los numeros registrados