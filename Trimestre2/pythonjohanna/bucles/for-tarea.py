a=int(input("Ingrese el numero por el que quiere iniciar: "))
b=int(input("Ingrese el numero en el que quiere que termine: "))
c=int(input("Ingrese cuanto quiere que el numero aumente o decremente (para decrementar, escriba el numero en negativo): "))
for j in range (a, b, c):
    if j%a==0:
        print(f"{j} es multiplo de {a}")
    else:
        print(j)


