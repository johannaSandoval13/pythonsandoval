n=int(input("Escriba un numero entre 0 y 100: "))
sumdiv=0
for s in range(1,n):
    if n%s==0:
        sumdiv+=s
if sumdiv==n:
    print(f"{n} es un numero perfecto")
else:
    print(f"{n} no es un numero perfecto")