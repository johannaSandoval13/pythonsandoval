a=int(input("Escriba un numero: "))

for i in range (1,a,1):
    if i%5==0:
        print(f"{i} es multiplo de 5")
    else:
        print(i)
        