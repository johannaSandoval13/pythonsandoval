n=int(input("Escriba el valor maximo: "))
sum=0
i=1
while sum <= n:
    sum+= i
    i += 1
print(f"El número más pequeño de la serie cuya suma excede {n} es {i-1}")