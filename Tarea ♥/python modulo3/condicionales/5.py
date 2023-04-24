a=int(input("Ingrese el lado 1 del triangulo: "))
b=int(input("Ingrese el lado 2 del triangulo: "))
c=int(input("Ingrese el lado 3 del triangulo: "))

if a==b and b==c:
    print ("Triangulo equilatero")
elif a!=b and b!=c:
    print ("Triangulo escaleno")
else:
    print("Triangulo isosceles")
