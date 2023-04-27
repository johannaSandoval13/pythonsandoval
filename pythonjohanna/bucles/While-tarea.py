a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))

while a==b or b==a:
    print("Los numeros deben ser distintos, de nuevo por favor")
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese otro numero: "))
if a>b:
    print("La resta de los numeros escritos es:",a-b)
else:
    print("La resta de los numeros escritos es:",b-a)