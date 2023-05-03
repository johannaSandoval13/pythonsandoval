a=int(input("Ingrese un numero: "))

for j in range(1,a+1):
    if a%j==0:
        print (f"{j} es divisor de {a}")
    else:
        print(j)